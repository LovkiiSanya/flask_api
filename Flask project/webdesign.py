from courses import BasicCourses
from all_enams import *


class WebDesign(BasicCourses):
    def __init__(self):
        super().__init__()
        self.__design_language: DesignLanguage = None
        self.__design_programs: str = None

    def set_design_language(self, design_language: DesignLanguage):
        self.__design_language = design_language

    def get_design_language(self):
        return self.__design_language

    def set_design_programs(self, design_programs: DesignPrograms):
        self.__design_programs = design_programs

    def get_design_programs(self):
        return self.__design_programs
