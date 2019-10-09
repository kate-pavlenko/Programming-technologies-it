import requests
import json
import logging
from requests.exceptions import HTTPError
import time

logging.basicConfig(
    filename="server.log",
    filemode='a',
    level=logging.INFO,
    format='{levelname} {asctime} {name} : {message}',
    style='{'
)
log = logging.getLogger(__name__)
def runminute():
    main("http://localhost:8000/health")

def main(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
    except HTTPError as http_err:
        logging.error("HTTP помилка: : %s", http_err)
    except Exception as err:
        logging.error("Якась помилка: : %s", err)
    else:
        if r.status_code == 200:
            data = json.loads(r.content)
            logging.info("Сервер доступний. Час на сервері: %s", data['date'])
            logging.info("Запитувана сторінка: : %s", data['current_page'])
            logging.info("Інформація про сервер: : %s", data['server_info'])
            logging.info("Інформація про користувача: : %s", data['client_info'])

    while True:
        time.sleep(60)
        runminute()
'''
    logging.info("Відповідь сервера місти наступні поля:")
    for key in data.keys():
        logging.info("Ключ: %s, Значення: %s", key, data[key])
'''

if __name__ == '__main__':
    runminute()