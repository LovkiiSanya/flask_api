import datetime


# def start_of_courses():
#     print("Давайте определимся с датой начала вашего оучения!")
#     try:
#         year = int(input("Начнем с года:"))
#     except ValueError:
#         year = datetime.datetime.now().year
#         print("Установлен текущий год,", year)
#     try:
#         month = int(input("Теперь месяц:"))
#     except ValueError:
#         month = datetime.datetime.now().month + 1
#         print("Значит врываемся в учебу со следующего месяца", month)
#     try:
#         day = int(input("День:"))
#     except ValueError:
#         day = datetime.datetime.now().day + 1
#         print("Все,начинаем завтра")
#     if datetime.datetime(year, month, day) - datetime.datetime.now() > datetime.timedelta(0):
#         print(datetime.datetime(year, month, day).strftime("%m/%d/%Y"))
#         return datetime.datetime(year, month, day).strftime("%m/%d/%Y")
#     else:
#         print("Кажется вы ввели что-то не то,давайте еще разок")
#         start_of_courses()


def start_of_courses(year: int, month: int, day: int) -> str:
    start_date = datetime.datetime(year, month, day)
    if start_date > datetime.datetime.now():
        return start_date.strftime("%m/%d/%Y")
    else:
        raise ValueError("Дата должна быть в будущем времени")