from courses import BasicCourses
from all_enams import *


class Language(BasicCourses):
    def __init__(self):
        super().__init__()
        self.__group: LangGroups = None

    def set_lang_group(self,lang_group:LangGroups):
        self.__group = lang_group
    def get_lang_group(self):
        return self.__group