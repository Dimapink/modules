from datetime import datetime


def get_employees():
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(now, "Вызов функции get_employees", sep=" -- ")
