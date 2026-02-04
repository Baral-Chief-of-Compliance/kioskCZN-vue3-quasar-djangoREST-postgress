import os
import logging


os.makedirs('logs', exist_ok=True)

logging.basicConfig(
    level=logging.INFO, 
    filename="logs/staff-scraper.log",filemode="w",
    format="%(asctime)s %(levelname)s %(message)s"
)