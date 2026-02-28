import sys
import logging
import os
import time

from db import DbController

from parser import VacansyParsers
from parser.proxy import ProxySetting
import logger


dbCon = DbController(
    os.getenv('POSTGRES_USER'),
    os.getenv('POSTGRES_PASS'),
    os.getenv('POSTGRES_DB'),
    os.getenv('POSTGRES_HOST'),
    os.getenv('POSTGRES_PORT')
)


err = dbCon.create_engine()

if err:
    logging.error('Error while create engine: {}'.format(err))
    sys.exit()



if bool(int(os.getenv('PROXY_USE'))):
    proxy_settings = ProxySetting(
        port=os.getenv('PROXY_PORT'),
        proxy_ip=os.getenv('PROXY_ID')
    )

    vp = VacansyParsers(
        proxy=proxy_settings
    )

else:
    vp = VacansyParsers()


# Логика для цикла

def main():
    time.sleep(30)
    while True:

        err = dbCon.delete_all_vacancies()
        if err:
            logging.error('error while delete all vacancies from db: {}'.format(err))
            sys.exit()
        else:
            err, res = vp.get_all_vacansy()

            if err:
                logging.error('Error while get_all_vacansy: {}'.format(err))
            else:
                res = res.json()

                err, filter_vacancies = vp.filter_vacansy_in_districs(
                    res['vacancies']
                )

                if err:
                    logging.error('while filtering vacansy for our region {}'.format(err))

                else:
                    for fv in filter_vacancies:
                        err = dbCon.create_vacansy_from_dict(fv)

                        if err:
                            logging.error('while add vacansy into db {}'.format(err))

        logging.info('finish get vacansy from open data')
        time.sleep(3600)


if __name__ == '__main__':
    main()