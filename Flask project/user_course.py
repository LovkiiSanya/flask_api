from playhouse.shortcuts import model_to_dict
from all_courses_staff.courses import *
from flasgger import swag_from

from create_db import UserTable, UserCourse
from serializer import *

user_course_bp = Blueprint('user_course', __name__)


def add_user_course(user_id: int, course_id: int):
    user = UserTable.get_or_none(UserTable.id == user_id)
    course = CoursesTable.get_or_none(CoursesTable.id == course_id)

    if not user:
        return {"error": f"Пользователь с  ID {user_id} не найден."}
    if not course:
        return {"error": f"Курс с  ID {course_id} не найден."}

    new_user_course = UserCourse.create(user=user, course=course)

    user_dict = model_to_dict(user)
    course_dict = model_to_dict(course)
    print(f"User {user_dict['user_table_name']} записан на курс {course_dict['courses_table_direction']}")

    return {"message": f"User {user.user_table_name} записан на курс {course.courses_table_direction}"}


@user_course_bp.route('/', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'UserCourse',
                'required': ['user_id', 'course_id'],
                'properties': {
                    'user_id': {'type': 'integer', 'description': 'The ID of the user'},
                    'course_id': {'type': 'integer', 'description': 'The ID of the course'}
                }
            }
        }
    ],
    'responses': {
        201: {'description': 'User course entry created'},
        400: {'description': 'Invalid input'}
    }
})
def create_user_course():
    data = request.get_json()
    user_id = data.get("user_id")
    course_id = data.get("course_id")
    if not user_id or not course_id:
        return jsonify({"error": "Отстутвует user_id или course_id"}), 400

    result = add_user_course(user_id, course_id)
    if "error" in result:
        return jsonify(result), 404
    return jsonify(result), 200


@user_course_bp.route('/<int:user_id>/<int:course_id>', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Fetch a user course entry given its identifiers',
            'schema': {
                'id': 'UserCourse',
                'properties': {
                    'user_id': {'type': 'integer', 'description': 'The ID of the user'},
                    'course_id': {'type': 'integer', 'description': 'The ID of the course'}
                }
            }
        },
        404: {'description': 'User course not found'}
    }
})
def get_user_course(user_id, course_id):
    user_course = UserCourse.get_or_none((UserCourse.user == user_id) & (UserCourse.course == course_id))
    if not user_course:
        return jsonify({"error": "Запись не найдена"}), 404

    user = UserTable.get_or_none(UserTable.id == user_id)
    course = CoursesTable.get_or_none(CoursesTable.id == course_id)

    if not user or not course:
        return jsonify({"error": "Пользователь или курс не найдены"}), 404

    user_course_serializer = UserCourseSerializer(user_course)
    return jsonify(user_course_serializer.serialize())


@user_course_bp.route('/<int:user_id>/<int:course_id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'UserCourse',
                'required': ['user_id', 'course_id'],
                'properties': {
                    'user_id': {'type': 'integer', 'description': 'The ID of the user'},
                    'course_id': {'type': 'integer', 'description': 'The ID of the course'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'User course entry updated'},
        404: {'description': 'User course not found'}
    }
})
def update_user_course(user_id, course_id):
    data = request.get_json()
    new_user_id = data.get("user_id")
    new_course_id = data.get("course_id")
    if not new_user_id or not new_course_id:
        return jsonify({"error": "Отстутвует user_id или course_id"}), 400

    user_course = UserCourse.get_or_none((UserCourse.user == user_id) & (UserCourse.course == course_id))
    if user_course:
        user_course.user = new_user_id
        user_course.course = new_course_id
        user_course.save()
        return jsonify({"message": "Запись обновлена"}), 200
    else:
        return jsonify({"error": "Запись не найдена"}), 404


@user_course_bp.route('/<int:user_id>/<int:course_id>', methods=['DELETE'])
@swag_from({
    'responses': {
        204: {'description': 'User course deleted'},
        404: {'description': 'User course not found'}
    }
})
def delete_user_course(user_id, course_id):
    user_course = UserCourse.get_or_none((UserCourse.user == user_id) & (UserCourse.course == course_id))
    if user_course:
        user_course.delete_instance(recursive=True)
        return jsonify({"message": "Запись удалена"}), 200
    else:
        return jsonify({"error": "Запись не найдена"}), 404
