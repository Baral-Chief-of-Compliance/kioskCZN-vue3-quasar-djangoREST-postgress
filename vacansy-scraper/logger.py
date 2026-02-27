import os
import logging


os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    filename="logs/vacansy-scraper.log",filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
)