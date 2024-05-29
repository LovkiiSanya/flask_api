import enum
from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource
from flasgger import swag_from
enams_bp = Blueprint("enams", __name__)


class UserAge(enum.Enum):
    LIL = "Диапазон возраста : 16 - 20"
    MID = "Диапазон возраста : 21 - 25"
    OLD = "Диапазон возраста : 26 - 30"
    OLD_BUT_GOLD = "Диапазон возраста : 31 - 40"
    WTF = "Диапазон возраста : 41+"


class CoursesLevel(enum.Enum):
    NOOB = "Нет никаких знаний"
    BEGINNER = "Начальный уровень знаний"
    MIDDLE = "Базовый уровень знаний"
    PRO = "Продвинутый уровень знаний"
    EXPERT = "Умнек бл##ь"


class CoursesDuration(enum.Enum):
    SHORT = "Вводный курс на 1 месяц"
    NORMAL = "Базовый курс на 3 месяца"
    LONG = "Продвинутый курс на 6 месяцев"


class CoursesLanguage(enum.Enum):
    ENG = "English language"
    RUS = "Русский язык"
    UKR = "Українська мова"
    DEU = "Deutsche Sprache"
    ESP = "Español"


def enum_to_dict(enum_class):
    return {item.name: item.value for item in enum_class}


@enams_bp.route('/user_ages', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Fetch all user age ranges',
            'schema': {
                'type': 'object',
                'properties': {
                    'LIL': {
                        'type': 'string',
                        'example': 'Диапазон возраста : 16 - 20'
                    },
                    'MID': {
                        'type': 'string',
                        'example': 'Диапазон возраста : 21 - 25'
                    },
                    'OLD': {
                        'type': 'string',
                        'example': 'Диапазон возраста : 26 - 30'
                    },
                    'OLD_BUT_GOLD': {
                        'type': 'string',
                        'example': 'Диапазон возраста : 31 - 40'
                    },
                    'WTF': {
                        'type': 'string',
                        'example': 'Диапазон возраста : 41+'
                    }
                }
            }
        }
    }
})
def get_user_ages():
    return jsonify(enum_to_dict(UserAge))


@enams_bp.route('/course_levels', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Fetch all course levels',
            'schema': {
                'type': 'object',
                'properties': {
                    'NOOB': {
                        'type': 'string',
                        'example': 'Нет никаких знаний'
                    },
                    'BEGINNER': {
                        'type': 'string',
                        'example': 'Начальный уровень знаний'
                    },
                    'MIDDLE': {
                        'type': 'string',
                        'example': 'Базовый уровень знаний'
                    },
                    'PRO': {
                        'type': 'string',
                        'example': 'Продвинутый уровень знаний'
                    },
                    'EXPERT': {
                        'type': 'string',
                        'example': 'Умнек бл##ь'
                    }
                }
            }
        }
    }
})
def get_course_levels():
    return jsonify(enum_to_dict(CoursesLevel))


@enams_bp.route('/course_durations', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Fetch all course durations',
            'schema': {
                'type': 'object',
                'properties': {
                    'SHORT': {
                        'type': 'string',
                        'example': 'Вводный курс на 1 месяц'
                    },
                    'NORMAL': {
                        'type': 'string',
                        'example': 'Базовый курс на 3 месяца'
                    },
                    'LONG': {
                        'type': 'string',
                        'example': 'Продвинутый курс на 6 месяцев'
                    }
                }
            }
        }
    }
})
def get_course_durations():
    return jsonify(enum_to_dict(CoursesDuration))


@enams_bp.route('/course_languages', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Fetch all course languages',
            'schema': {
                'type': 'object',
                'properties': {
                    'ENG': {
                        'type': 'string',
                        'example': 'English language'
                    },
                    'RUS': {
                        'type': 'string',
                        'example': 'Русский язык'
                    },
                    'UKR': {
                        'type': 'string',
                        'example': 'Українська мова'
                    },
                    'DEU': {
                        'type': 'string',
                        'example': 'Deutsche Sprache'
                    },
                    'ESP': {
                        'type': 'string',
                        'example': 'Español'
                    }
                }
            }
        }
    }
})
def get_course_languages():
    return jsonify(enum_to_dict(CoursesLanguage))
