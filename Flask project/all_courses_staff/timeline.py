import datetime


def start_of_courses(year: int, month: int, day: int) -> str:
    start_date = datetime.datetime(year, month, day)
    if start_date > datetime.datetime.now():
        return start_date.strftime("%m/%d/%Y")
    else:
        raise ValueError("Дата должна быть в будущем времени")