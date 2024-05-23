from courses import BasicCourses
from all_enams import *


class QualityAssurance(BasicCourses):
    def __init__(self):
        super().__init__()
        self.__qa_language: QAlanguage = None
        self.__qa_technology: QAtechnology = None

    def set_qa_language(self, qa_language: QAlanguage):
        self.__qa_language = qa_language

    def get_qa_language(self):
        return self.__qa_language

    def set_qa_technology(self, qa_technology: QAtechnology):
        self.__qa_technology = qa_technology

    def get_qa_technology(self):
        return self.__qa_technology
