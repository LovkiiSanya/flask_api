from all_enams import *
import datetime
from timeline import *
from create_db import *
from users import *


courses_bp = Blueprint('courses', __name__)
api = Api(courses_bp)


class BasicCourses:
    def __init__(self):
        self.__price: CoursesPrise = None  # Courses price
        self.__level: CoursesLevel = None  # Courses difficult level
        self.__duration: CoursesDuration = None  # Courses duration
        self.__language: CoursesLanguage = None  # Courses language
        self.__direction: CoursesDirection = None  # Courses direction study
        self.__date_start_course: datetime = None  # Courses date of start

    def set_price(self, price: CoursesPrise):
        self.__price = price

    def get_price(self):
        return self.__price.value

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

    def set_direction(self, direction: CoursesDirection):
        self.__direction = direction

    def get_direction(self):
        return self.__direction.value

    def set_start_course(self, start_course):
        self.__date_start_course = start_course

    def get_start_course(self):
        return self.__date_start_course


# def set_courses_info() -> CoursesTable:
#     profile_courses = BasicCourses()
#     price = input("Выберите подходящий вам пакет: \nECO(1000$)\nSTANDART(2000$)"
#                   "\nPREMIUM(3000%)\nPREMIUM_PRO(5000$)\n").lower()
#     try:
#         new_price = CoursesPrise[price.upper()]
#     except KeyError:
#         print("Походу вы нищий, подключен пакет ECO")
#         new_price = CoursesPrise.ECO
#     profile_courses.set_price(new_price)
#     level = input("Какую сложность курса вы хотите пройти?: \nNOOB\nBEGINNER\nMIDDLE\nPRO\nEXPERT\n").lower()
#     try:
#         courses_level = CoursesLevel[level.upper()]
#     except KeyError:
#         print("Установлен начальный уровень знаний")
#         courses_level = CoursesLevel.BEGINNER
#     profile_courses.set_level(courses_level)
#     duration = input("Теперь надо выбрать продолжителность обучения: \nSHORT\nNORMAL\nLONG\n").lower()
#     try:
#         courses_duration = CoursesDuration[duration.upper()]
#     except KeyError:
#         print("Будем учиться по стандартной схеме NORMAL")
#         courses_duration = CoursesDuration.NORMAL
#     profile_courses.set_duration(courses_duration)
#     language = input("На каком языке преподавать вам курс ? \nENG\nRUS\nUKR\nDEU\nESP\n").lower()
#     try:
#         courses_language = CoursesLanguage[language.upper()]
#     except KeyError:
#         print("Установлен Испанский,Cómo estás?")
#         courses_language = CoursesLanguage.ESP
#     profile_courses.set_language(courses_language)
#     direction = input("Какое направление вас интересует? \nBACKEND\nFRONTEND\nWEB_DESIGN\nLANGUAGE\nQA\n")
#     try:
#         courses_direction = CoursesDirection[direction.upper()]
#     except KeyError:
#         print("Сделаем из вас бекендера,станете человеком!")
#         courses_direction = CoursesDirection.BACKEND
#     profile_courses.set_direction(courses_direction)
#     date_start = start_of_courses()
#     profile_courses.set_start_course(date_start)
#     new_record_table_courses = CoursesTable(
#         courses_table_price=profile_courses.get_price(),
#         courses_table_direction=profile_courses.get_direction(),
#         courses_table_level=profile_courses.get_level(),
#         courses_table_duration=profile_courses.get_duration(),
#         courses_table_language=profile_courses.get_language(),
#         courses_table_date=profile_courses.get_start_course()
#     )
#     new_record_table_courses.save()
#     new_record_id = new_record_table_courses.id
#     print("Ваш персональный ID", new_record_id)
#     return new_record_table_courses


# set_courses_info()

class CoursesListResource(Resource):
    def post(self):
        data = request.get_json()

        profile_courses = BasicCourses()
        price = data.get("price").lower()
        try:
            price_group = CoursesPrise[price.upper()]
        except KeyError:
            price_group = CoursesPrise.STANDART
        profile_courses.set_price(price_group)

        direction = data.get("direction").lower()
        try:
            direction_group = CoursesDirection[direction.upper()]
        except KeyError:
            direction_group = CoursesDirection.BACKEND
        profile_courses.set_direction(direction_group)

        level = data.get("level").lower()
        try:
            level_group = CoursesLevel[level.upper()]
        except KeyError:
            level_group = CoursesLevel.BEGINNER
        profile_courses.set_level(level_group)

        duration = data.get("duration").lower()
        try:
            duration_group = CoursesDuration[duration.upper()]
        except KeyError:
            duration_group = CoursesDuration.NORMAL
        profile_courses.set_duration(duration_group)

        language = data.get("language").lower()
        try:
            language_group = CoursesLanguage[language.upper()]
        except KeyError:
            language_group = CoursesLanguage.ESP
        profile_courses.set_language(language_group)

        year = data.get("year")
        month = data.get("month")
        day = data.get("day")
        if not (isinstance(year, int) and isinstance(month, int) and isinstance(day, int)):
            return jsonify({"error": "Только числа,чел"}), 400
        try:
            date_start = start_of_courses(year, month, day)
        except ValueError:
            return jsonify({"error"}), 400

        profile_courses.set_start_course(date_start)

        new_record_table_courses = CoursesTable(
            courses_table_price=profile_courses.get_price(),
            courses_table_direction=profile_courses.get_direction(),
            courses_table_level=profile_courses.get_level(),
            courses_table_duration=profile_courses.get_duration(),
            courses_table_language=profile_courses.get_language(),
            courses_table_date=profile_courses.get_start_course()
        )
        new_record_table_courses.save()
        return jsonify({"id": new_record_table_courses.id})

    def get(self, course_id):
        courses = CoursesTable.get_or_none(CoursesTable.id == course_id)
        if courses:
            return jsonify({
                "id": courses.id,
                "price": courses.courses_table_price,
                "direction": courses.courses_table_direction,
                "level": courses.courses_table_level,
                "duration": courses.courses_table_duration,
                "language": courses.courses_table_language,
                "start_course": courses.courses_table_date
            })
        else:
            return jsonify({"error": "Курс не найден"}), 404

    def put(self, course_id):
        data = request.get_json()
        course = CoursesTable.get_or_none(CoursesTable.id == course_id)
        if course:
            # Обновляем курс
            course.courses_table_price = data.get('price', course.courses_table_price)
            course.courses_table_direction = data.get('direction', course.courses_table_direction)
            course.courses_table_level = data.get('level', course.courses_table_level)
            course.courses_table_duration = data.get('duration', course.courses_table_duration)
            course.courses_table_language = data.get('language', course.courses_table_language)
            course.courses_table_date = data.get('start_course', course.courses_table_date)
            course.save()
            return jsonify({"message": "Курс обновлен"}), 200
        else:
            return jsonify({"error": "Курс не найден"}), 404

    def delete(self, course_id):
        course = CoursesTable.get_or_none(CoursesTable.id == course_id)
        if course:
            course.delete_instance(recursive=True)
            return jsonify({"message": "Курс удален"}), 200
        else:
            return jsonify({"error": "Курс не найден"}), 404


api.add_resource(CoursesListResource, '/courses', '/courses/<int:course_id>')

if __name__ == "__main__":
    app.run(debug=True)
