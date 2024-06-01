from application.salary import calculate_salary
from application.db.people import get_employees
from req import get_ya_ru


if __name__ == "__main__":
    calculate_salary()
    get_employees()

    get_ya_ru()