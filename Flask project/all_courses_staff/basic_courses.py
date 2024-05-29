from all_enams import *
import datetime


class BasicCourses:
    def __init__(self):
        self.__price: int = None  # Courses price
        self.__level: CoursesLevel = None  # Courses difficult level
        self.__duration: CoursesDuration = None  # Courses duration
        self.__language: CoursesLanguage = None  # Courses language
        self.__direction: str = None  # Courses direction study
        self.__date_start_course: datetime = None  # Courses date of start

    def set_price(self, price: int):
        self.__price = price

    def get_price(self):
        return self.__price

    def set_level(self, level: CoursesLevel):
        self.__level = level

    def get_level(self):
        return self.__level.value

    def set_duration(self, duration: CoursesDuration):
        self.__duration = duration

    def get_duration(self):
        return self.__duration.value

    def set_language(self, language: CoursesLanguage):
        self.__language = language

    def get_language(self):
        return self.__language.value

    def set_direction(self, direction: str):
        self.__direction = direction

    def get_direction(self):
        return self.__direction

    def set_start_course(self, start_course):
        self.__date_start_course = start_course

    def get_start_course(self):
        return self.__date_start_course
