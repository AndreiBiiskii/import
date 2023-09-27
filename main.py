from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime as dt

if __name__ == "__main__":
    calculate_salary(10, 5)
    get_employees(count=10)
    print(f'Сегоднешняя дата:{dt.date(dt.now())}')