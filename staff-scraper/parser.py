import json
import time
from datetime import date
import logging
import os
from typing import Tuple, Optional

from bs4 import BeautifulSoup
import requests

import logger


class WorkeParser(object):
    """Класс для сбора данных о сотрудниках цзг
    с телефонного справочника"""

    __DEPARTMENT_CLASS_NAME : str = 'spDepartment' #класс для наименований отделов КЦ

    __MAIN_WORKER_CLASS_NAME : str = 'spEven' #Глава отдела
    __COMMON_WORKER_CLASS_NAME : str = 'spOdd' #Обычный сотрудник
    __WORKER_CLASS_NAME : str = 'cellFlex' #класс, который позволяет идентифицировать div с информацией о сотрдуниках
    __WORKER_OUT_CLASS_NAME : str = 'out' #класс, который указывает, что сотрдник либо в отпуске, либо на больничном

    __ROOM_WORKER_CLASS_NAME : str = 'spRoom'
    __PHONE_WORKER_CLASS_NAME : str = 'spInnerNum'
    __FIO_WORKER_CLASS_NAME : str = 'spFIOtxt'
    __POST_WORKER_CLASS_NAME : str = 'spPost'
    __EMAIL_WORKER_CLASS_NAME : str = 'spEmail'

    __BASE_URL_PHONE_BOOK : str = 'http://172.25.31.33/phones2/' #основа url для парсинга работников со справочника
    __PERSONAL_CENTERS : list = [
        {
              'name': 'Управляющий центр',
              'page_id': 1
        },
        {
              'name': 'Мурманский КЦ',
              'page_id': 2
        },
        {
              'name': 'Кандалакшский КЦ',
              'page_id': 3
        },
        {
              'name': 'Полярнозоринский КЦ',
              'page_id': 4
        },
        {
              'name': 'Терский КЦ',
              'page_id': 5
        },
        {
              'name': 'Ковдорский КЦ',
              'page_id': 6
        },
        {
              'name': 'Кировский КЦ',
              'page_id': 7
        },
        {
              'name': 'Апатитский КЦ',
              'page_id': 8
        },
        {
              'name': 'Мончегорский КЦ',
              'page_id': 9
        },
        {
              'name': 'Оленегорский КЦ',
              'page_id': 10
        },
        {
              'name': 'Ловозерский КЦ',
              'page_id': 11
        },
        {
              'name': 'Кольский КЦ',
              'page_id': 12
        },
        {
              'name': 'Североморский КЦ',
              'page_id': 13
        },
        {
              'name': 'Александровский КЦ',
              'page_id': 14
        },
        {
              'name': 'Печенгский КЦ',
              'page_id': 15
        }
    ]

    def __init__(self, 
                url_rest_rooms: str,
                url_rest_workers_in_deps: str,
                url_rest_workers: str,
                url_rest_posts: str,
                url_rest_deps: str
                ):
        """Конструктор класс парсера"""
        #url для rest взаимодействия с кабинетами кадрового центра
        self.url_rest_rooms = url_rest_rooms

        #url для rest взаимодействия с работниками отделов в бд
        self.url_rest_workers_in_deps = url_rest_workers_in_deps

        # url для rest взаимодействия с работниками в бд
        self.url_rest_workers = url_rest_workers

        # url для rest взаимодейсвия с должностями в бд
        self.url_rest_posts = url_rest_posts

        # url для rest взаимодействия с отделами в бд
        self.url_rest_deps = url_rest_deps


    def get_data_about_all_personal_center(self):
        """Получить данные с каждого персонального центра"""
        for pc in self.__PERSONAL_CENTERS:

            # todo
            # обработать данные 
            # и отправлТь их не бекенд
            # предварительно сделать методы добавляние, отделов, постов, сотрудников
            # с учето
            html_from_page = f"phones_book_page/{pc['page_id']}.html"
            self.get_from_html_data(
                html_page_path=html_from_page,
                test=True
            )
            data_from_page = self.get_departments_name()

            for dep_name in data_from_page.keys():
                dep_payload = {
                    'pc': pc['page_id'],
                    'name': dep_name
                }
                try:
                    res = requests.get(
                        url=self.url_rest_deps,
                        params=dep_payload
                    )

                    if res.status_code != 200:
                        logging.error(f'status code from dep rest {res.status_code} error: {res.text}')
                    else:
                        res_json = res.json()
                        deps = res_json

                        current_dep = None #текущий отдел
                        if len(deps) == 0:
                            # Значит этого отдела надо добавить
                            res = requests.post(
                                url=self.url_rest_deps,
                                data=json.dumps({
                                    'name': dep_name,
                                    'pc': pc['page_id']
                                }),
                                headers={'Content-Type': 'application/json'}
                            )

                            if res.status_code != 201:
                                logging.error(f"status code from dep rest {res.status_code} error: {res.text}")
                            else:
                                logging.info(f"add {dep_name} to pc with id={ pc['page_id']}")
                                current_dep = res.json()
                        else:
                            current_dep = deps[0]

                        # Проходим сотрудников отдела
                        if current_dep:
                            for em in data_from_page[dep_name]:
                                # Проверка должности
                                em_post = None
                                try:
                                    post_payload = {
                                        'name': em['post']
                                    }
                                    res = requests.get(
                                        url=self.url_rest_posts,
                                        params=post_payload
                                    )

                                    if res.status_code != 200:
                                        logging.error(f'status from post rest code {res.status_code} error: {res.text}')
                                    else:
                                        res_json = res.json()
                                        posts = res_json

                                        if len(posts) == 0:
                                            #Значит данную должность надо добавить
                                            res = requests.post(
                                                url=self.url_rest_posts,
                                                data=json.dumps({
                                                    'name': em['post'],
                                                }),
                                                headers={'Content-Type': 'application/json'}
                                            )
                                            if res.status_code != 201:
                                                logging.error(f"status code from post rest {res.status_code} error: {res.text}")
                                            else:
                                                logging.info(f"add post {em['post']} to system")
                                                em_post = res.json()
                                        else:
                                            em_post = posts[0]
                                except Exception as ex:
                                    logging.error(f'error while make check exist post: {ex }')


                                # Есть ли в спарсенных данных кабинет у сотрудника
                                # Проверка кабинета
                                em_room = None
                                if em['room']: 
                                    try:
                                        room_payload = {
                                            'pc': pc['page_id'],
                                            'name': em['room']
                                        }
                                        res = requests.get(
                                            url=self.url_rest_rooms,
                                            params=room_payload
                                        )

                                        if res.status_code != 200:
                                            logging.error(f'status from room rest code {res.status_code} error: {res.text}')
                                        else:
                                            res_json = res.json()
                                            rooms = res_json

                                            if len(rooms) == 0:
                                                #Значит данный кабинет надо добавить
                                                res = requests.post(
                                                    url=self.url_rest_rooms,
                                                    data=json.dumps({
                                                        'name': em['room'],
                                                        'pc': pc['page_id']
                                                    }),
                                                    headers={'Content-Type': 'application/json'}
                                                )
                                                if res.status_code != 201:
                                                    logging.error(f"status code from room rest {res.status_code} error: {res.text}")
                                                else:
                                                    logging.info(f"add room {em['room']} to pc id={pc['page_id']}")
                                                    em_room = res.json()
                                            else:
                                                em_room = rooms[0]
                                    except Exception as ex:
                                        logging.error(f'error while make check exist room: {ex}')

                                # Проверка Сотрудника
                                employer = None

                                try:
                                    employer_payload = {
                                        'id': em['id']
                                    }
                                    
                                    res = requests.get(
                                        url=self.url_rest_workers,
                                        params=employer_payload
                                    )

                                    if res.status_code != 200:
                                        logging.error(f'status from worker rest code {res.status_code} error: {res.text}')
                                    else:
                                        res_json = res.json()
                                        employers = res_json
                                        # Для добавления и обновления сотрудника
                                        emp_info = {
                                            'id': em['id'],
                                            'fio': em['fio'],
                                            # 'date_get_info': em['date_of_get_info'],
                                            'absent': em['absent']
                                        }

                                        if em['phone']:
                                            emp_info['phone'] = em['phone']

                                        if em['room']:
                                            emp_info['room'] = em_room['id']

                                        if em['email']:
                                            emp_info['email'] = em['email']
                                        if len(employers) == 0:
                                            # Необходимо добавить сотрудника
                                            res = requests.post(
                                                url=self.url_rest_workers,
                                                data=json.dumps(emp_info),
                                                headers={'Content-Type': 'application/json'}
                                            )
                                            if res.status_code != 201:
                                                logging.error(f"status code from worker rest {res.status_code} error: {res.text}")
                                            else:
                                                logging.info(f"add worker {em['fio']} in system ")
                                                employer = res.json()

                                        else:
                                            employer = employers[0]
                                            # Если сотрудник есть в базе, то ему необходимо обновить данные
                                            res = requests.patch(
                                                url=f"{self.url_rest_workers}{em['id']}/",
                                                data=json.dumps(emp_info),
                                                headers={'Content-Type': 'application/json'}
                                            )

                                            if res.status_code != 200:
                                                logging.error(f"status code from worker rest patch {res.status_code} error: {res.text}")

                                except Exception as ex:
                                    logging.error(f'error while make check exist employer: {ex}')


                                # Проверка сотрудника в отделе
                                if employer:
                                    try:
                                        # Если сотрудник есть, то теперь мы добавим сотрудника в отдел
                                        # Точнее проверим есть ли он в отделе, если есть, то обновим его,
                                        # если нет, то добавим его

                                        employer_in_dep = None
                                        employer_in_dep_payload = {
                                            'worker': em['id'],
                                            'dep': current_dep['id']
                                        }

                                        res = requests.get(
                                            url=self.url_rest_workers_in_deps,
                                            params=employer_in_dep_payload
                                        )

                                        if res.status_code != 200:
                                            logging.error(f'status from worker_deps rest code {res.status_code} error: {res.text}')
                                        else:
                                            res_json = res.json()
                                            employers_deps = res_json

                                            emp_in_deps_info = {
                                                'worker': em['id'],
                                                'dep': current_dep['id'],
                                                'post': em_post['id'],
                                                'head_of_dep': em['head_of_department'],
                                            }

                                            if len(employers_deps) == 0:
                                                # Необходимо его добавить в отделе в базе

                                                res = requests.post(
                                                    url=self.url_rest_workers_in_deps,
                                                    data=json.dumps(emp_in_deps_info),
                                                    headers={'Content-Type': 'application/json'}
                                                )

                                                if res.status_code != 201:
                                                    logging.error(f"status code from worker rest {res.status_code} error: {res.text}")
                                                else:
                                                    logging.info(f"add worker {em['fio']} in system ")
                                            else:
                                                employer_in_dep_id = employers_deps[0]['id']
                                                # Если сотрудник есть в базе, то ему необходимо обновить данные
                                                res = requests.patch(
                                                    url=f"{self.url_rest_workers_in_deps}{employer_in_dep_id}/",
                                                    data=json.dumps(emp_in_deps_info),
                                                    headers={'Content-Type': 'application/json'}
                                                )

                                                if res.status_code != 200:
                                                    logging.error(f"status code from worker_in_deps rest patch {res.status_code} error: {res.text}")

                                    except Exception as ex:
                                        logging.error(f'error while make check exist worker_deps: {ex}')

                except Exception as ex:
                    logging.error(f'error while make check exist dep: {ex}')
                time.sleep(1)






    def get_data_from_url(self, url: str) -> Tuple[bool, Optional[str]]:
        """Получить данные с страницы"""
        # http://main.z51.local/phones2/1.html
        proxies = {}
        headers = {
            'Content-Type': 'application/json'
        }
        if bool(int(os.getenv('PROXY_USE'))):
            proxies['http'] = os.getenv('PROXY_PATH')
            proxies['https'] = os.getenv('PROXY_PATH')
            
        logging.info(f'proxy {proxies}')   

        response = requests.get(
            headers=headers,
            proxies=proxies,
            url=url
        )
        if response.status_code == 200:
            return False, response.text
        
        else:
            logging.error(
                'error while get data from phone book \
                {} code: {} error: {}'.format(
                    url,
                    response.status_code,
                    response.text
                )
            )
            return True, None


    def get_from_html_data(self, html_page_path : str = 'test.html', test=False):
        """Получить данные страницы с html страницы, которая уже скачена"""
        if not test:
            self.bs4_data = BeautifulSoup(html_page_path, features='html.parser')
        else:
            try:
                with open(html_page_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    self.bs4_data = BeautifulSoup(content, features='html.parser')
            except FileNotFoundError:
                logging.error("{} is not found".format(html_page_path))
            except PermissionError:
                logging.error("You do not have permission to read this file {}".format(html_page_path))


    def show_bs4_data(self):
        """Отобразить bs4 результат, которые получился, для теста"""
        return self.bs4_data.prettify()
    

    def get_departments_name(self) -> dict:
        """Получить все отделы КЦ со страницы c сотрудниками"""
        res = self.bs4_data.find_all('div')

        personnel_center_deps_info : dict = {}
        curent_department = ''
        for r in res:
            if 'class' in r.attrs:
                if self.__DEPARTMENT_CLASS_NAME in r.attrs['class']:
                    curent_department = r.text
                    if not curent_department in personnel_center_deps_info:
                        personnel_center_deps_info[curent_department] = []

                if self.__WORKER_CLASS_NAME in r.attrs['class']:
                    worker_info : dict = {
                        'id': 0,
                        'fio': '',
                        'head_of_department' : False,
                        'absent': False,
                        'post' : None,
                        'phone': None,
                        'room': None,
                        'email': None,
                        'date_of_get_info': date.today()
                    }
                    if self.__MAIN_WORKER_CLASS_NAME in r.attrs['class']:
                        worker_info['head_of_department'] = True
                    elif self.__COMMON_WORKER_CLASS_NAME in r.attrs['class']:
                        worker_info['head_of_department'] = False

                    if self.__WORKER_OUT_CLASS_NAME in r.attrs['class']:
                        worker_info['absent'] = True
                    else:
                        worker_info['absent'] = False

                    r_divs = r.find_all('div')
                    for rd in r_divs:
                        if self.__ROOM_WORKER_CLASS_NAME in rd.attrs['class']:
                            worker_info['room'] = rd.text
                        elif self.__PHONE_WORKER_CLASS_NAME in rd.attrs['class']:
                            worker_info['phone'] = int(rd.text[2:])
                        elif self.__POST_WORKER_CLASS_NAME in rd.attrs['class']:
                            worker_info['post'] = rd.text
                        elif self.__FIO_WORKER_CLASS_NAME in rd.attrs['class']:
                            worker_info['id'] = int(rd['id'][7:])
                            fio : str = rd.text
                            fio = fio.replace(' ', '')
                            new_fio = ''
                            for index, l  in enumerate(fio):
                                if l.isupper() and index !=0:
                                    new_fio += ' {}'.format(l)
                                else:
                                    new_fio += l
                            worker_info['fio'] = new_fio

                        elif self.__EMAIL_WORKER_CLASS_NAME in rd.attrs['class']:
                            worker_info['email'] = rd.text

                    personnel_center_deps_info[curent_department].append(worker_info)

        return personnel_center_deps_info