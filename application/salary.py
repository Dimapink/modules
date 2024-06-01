from datetime import datetime


def calculate_salary():
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(now, "Вызов вункции calculate_selary", sep=" -- ")
