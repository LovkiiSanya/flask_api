import datetime
from flask import request, jsonify
from all_enams import *
from all_courses_staff.basic_courses import BasicCourses
from create_db import CoursesTable
from all_courses_staff.timeline import *


def create_course_logic(data):
    data = request.get_json()

    profile_courses = BasicCourses()
    profile_courses.set_price(data.get("price"))
    profile_courses.set_direction(data.get("direction"))
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
    return jsonify(new_record_table_courses.serialize())
