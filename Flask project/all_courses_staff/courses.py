from create_db import CoursesTable
from all_courses_staff.timeline import *
from serializer import *
from all_courses_staff.basic_courses import *
from all_courses_staff.create_course_logic import *

courses_bp = Blueprint('courses', __name__)


@courses_bp.route('/', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'courses',
                'required': ['price', 'direction', 'duration', 'language', 'level', 'year', 'month', 'day'],
                'properties': {
                    'price': {'type': 'integer', 'description': 'Course price', 'example': '1000 in USD'},
                    'direction': {'type': 'string', 'description': 'Course direction', 'example': 'music'},
                    'level': {'type': 'string', 'description': 'Course level', 'example': 'pro'},
                    'duration': {'type': 'string', 'description': 'Course duration', 'example': 'normal'},
                    'language': {'type': 'string', 'description': 'Course language', 'example': 'eng'},
                    'year': {'type': 'integer', 'description': 'Course year start', 'example': 2024},
                    'month': {'type': 'integer', 'description': 'Course month start', 'example': 2},
                    'day': {'type': 'integer', 'description': 'Course day start', 'example': 24}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Course created',
            'schema': {
                'id': 'courses',
                'properties': {
                    'id': {'type': 'integer', 'description': 'The unique identifier of a course'},
                    'price': {'type': 'integer', 'description': 'Course price'},
                    'direction': {'type': 'string', 'description': 'Course direction'},
                    'duration': {'type': 'string', 'description': 'Course duration'},
                    'level': {'type': 'string', 'description': 'Course level'},
                    'language': {'type': 'string', 'description': 'Course language'},
                    'year': {'type': 'integer', 'description': 'Course year start'},
                    'month': {'type': 'integer', 'description': 'Course month start'},
                    'day': {'type': 'integer', 'description': 'Course day start'}
                }
            }
        }
    }
})
def create_course():
    data = request.get_json()
    return create_course_logic(data)


@courses_bp.route('/<int:course_id>', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Fetch a course given its identifier',
            'schema': {
                'id': 'courses',
                'properties': {
                    'id': {'type': 'integer', 'description': 'The unique identifier of a course'},
                    'price': {'type': 'integer', 'description': 'Course price'},
                    'direction': {'type': 'string', 'description': 'Course direction'},
                    'duration': {'type': 'string', 'description': 'Course duration'},
                    'level': {'type': 'string', 'description': 'Course level'},
                    'language': {'type': 'string', 'description': 'Course language'},
                    'year': {'type': 'string', 'description': 'Course year start'},
                    'month': {'type': 'string', 'description': 'Course month start'},
                    'day': {'type': 'string', 'description': 'Course day start'}
                }
            }
        },
        404: {'description': 'Course not found'}
    }
})
def get_course(course_id):
    courses = CoursesTable.get_or_none((CoursesTable.id == course_id) & (CoursesTable.is_deleted == False))
    if courses:
        course_serializer = CourseSerializer(courses)
        return jsonify(course_serializer.serialize())
    else:
        return jsonify({"error": "Курс не найден"}), 404


@courses_bp.route("/<int:course_id>", methods=["PUT"])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'courses',
                'required': ['price', 'direction', 'duration', 'language', 'level', 'year', 'month', 'day'],
                'properties': {
                    'price': {'type': 'integer', 'description': 'Course price', 'example': '1000 USD'},
                    'direction': {'type': 'string', 'description': 'Course direction', 'example': 'music'},
                    'level': {'type': 'string', 'description': 'Course level', 'example': 'pro'},
                    'duration': {'type': 'string', 'description': 'Course duration', 'example': 'normal'},
                    'language': {'type': 'string', 'description': 'Course language', 'example': 'eng'},
                    'year': {'type': 'integer', 'description': 'Course year start', 'example': '2024'},
                    'month': {'type': 'integer', 'description': 'Course month start', 'example': '2'},
                    'day': {'type': 'integer', 'description': 'Course day start', 'example': '24'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Course updated'},
        404: {'description': 'Course not found'}
    }
})
def put_course_logic(course_id):
    data = request.get_json()
    course = CoursesTable.get_or_none((CoursesTable.id == course_id) & (CoursesTable.is_deleted == False))
    if course:
        course.courses_table_price = data.get('price', course.courses_table_price)
        course.courses_table_language = data.get('language', course.courses_table_language)
        course.courses_table_date = data.get('start_course', course.courses_table_date)
        level = data.get("level")
        if level is not None:
            level = level.lower()
            try:
                level_group = CoursesLevel[level.upper()]
            except KeyError:
                level_group = CoursesLevel.BEGINNER
            course.courses_table_level = level_group.value
        duration = data.get("duration")
        if duration is not None:
            duration = duration.lower()
            try:
                duration_group = CoursesDuration[duration.upper()]
            except KeyError:
                duration_group = CoursesDuration.NORMAL
            course.courses_table_duration = duration_group.value
        language = data.get("language")
        if language is not None:
            language = language.lower()
            try:
                language_group = CoursesLanguage[language.upper()]
            except KeyError:
                language_group = CoursesLanguage.ENG
            course.courses_table_language = language_group.value

        course.save()
        return jsonify({"message": "Курс обновлен"}), 200
    else:
        return jsonify({"error": "Курс не найден"}), 404


@courses_bp.route("/<int:course_id>/", methods=["DELETE"])
@swag_from({
    'responses': {
        204: {'description': 'Course deleted'},
        404: {'description': 'Course not found'}
    }
})
def delete_course(course_id):
    course = CoursesTable.get_or_none(CoursesTable.id == course_id)
    if course:
        course.is_deleted = True
        course.save()
        return jsonify({"message": "Курс удален"}), 200
    else:
        return jsonify({"error": "Курс не найден"}), 404
