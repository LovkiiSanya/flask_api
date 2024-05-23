from courses import BasicCourses
from all_enams import *


class Backend(BasicCourses):
    def __init__(self) -> None:
        super().__init__()
        self.__back_language: BackendLanguage = None
        self.__back_framework: BackendFrameworks = None
        self.__back_database: BackendDatabase = None

    def set_back_lang(self, back_language: BackendLanguage):
        self.__back_language = back_language

    def get_back_lang(self):
        return self.__back_language

    def set_back_framework(self, back_framework: BackendFrameworks):
        self.__back_framework = back_framework

    def get_back_framework(self):
        return self.__back_framework

    def set_back_database(self, back_database: BackendDatabase):
        self.__back_database = back_database

    def get_back_database(self):
        return self.__back_database

