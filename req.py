import requests
from datetime import datetime


def get_ya_ru():
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    a = requests.get("https://ya.ru")
    print("Вызов функции get_ya_ru")
    print(now, f"{a.status_code=}")
