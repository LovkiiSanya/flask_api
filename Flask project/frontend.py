from courses import BasicCourses
from all_enams import *


class Frontend(BasicCourses):
    def __init__(self) -> None:
        super().__init__()
        self.__front_language: FrontendLanguage = None
        self.__front_framework: FrontendFrameworks = None

    def set_front_language(self, front_language: FrontendLanguage):
        self.__front_language = front_language

    def get_front_language(self):
        return self.__front_language

    def set_front_framework(self, front_framework: FrontendFrameworks):
        self.__front_framework = front_framework

    def get_front_framework(self):
        return self.__front_framework
