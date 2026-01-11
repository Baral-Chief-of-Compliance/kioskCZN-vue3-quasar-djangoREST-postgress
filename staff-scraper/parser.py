import json
from datetime import date

from bs4 import BeautifulSoup


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
                 url_rest_users : str,
                 url_rest_posts : str,
                 url_rest_deps : str,
                 ):
        """Конструктор класс парсера"""

        self.url_rest_users = url_rest_users
        self.url_rest_posts = url_rest_posts
        self.url_rest_deps = url_rest_deps


    def get_data(self):
        """Получить данные с страницы"""
        pass
    # http://main.z51.local/phones2/1.html

    def get_test_data(self, html_page_path : str = 'test.html'):
        """Получить данные страницы с html страницы, которая уже скачена"""
        try:
            with open(html_page_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.bs4_data = BeautifulSoup(content, features='html.parser')
        except FileNotFoundError:
            print("{} is not found".format(html_page_path))
        except PermissionError:
            print("You do not have permission to read this file {}".format(html_page_path))


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