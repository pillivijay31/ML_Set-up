import logging
from datetime import datetime
import os

LOG_DIR="housing_logs"

CURRENT_TIME_STAMP= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME= f"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE_PATH= os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
)
"""
%(acstime)s - timestamp[2022-08-04 08:34:14,322] 
%(name)s - werkzeug - 
%(levelname)s - INFO - 127.0.0.1 -
%(message)s - [04/Aug/2022 08:34:14] "[33mGET /favicon.ico HTTP/1.1[0m" 404 -
"""