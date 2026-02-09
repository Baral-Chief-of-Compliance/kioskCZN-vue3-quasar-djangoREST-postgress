import os
import time
import logging

from parser import WorkeParser
import logger



def main():
    wp = WorkeParser(
        os.getenv('URL_REST_USERS', ''),
        os.getenv('URL_REST_POSTS', ''),
        os.getenv('URL_REST_DEPS', '')
    )

    logging.info('start work staff-scraper')

    while True:
        try:
            logging.info('start scraping data from phone book')
            wp.get_data_about_all_personal_center()

            logging.info('finish scraping data from phone book')
        except Exception as ex:
            logging.error(ex)
        
        time.sleep(3600)


if __name__ == "__main__":
    main()
