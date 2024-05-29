from all_enams import UserAge
import datetime


class User:
    def __init__(self) -> None:
        self.__name: str = None  # User name
        self.__username: str = None  # Username on courses
        self.__age: UserAge = None  # User age
        self.__profession: str = None  # User profession
        self.__date: datetime = None  # User registration

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_username(self, username: str):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_age(self, age: UserAge):
        self.__age = age

    def get_age(self):
        return self.__age.value

    def set_profession(self, profession: str):
        self.__profession = profession

    def get_profession(self):
        return self.__profession

    def set_date(self, date: datetime):
        self.__date = date

    def get_date(self):
        return self.__date
