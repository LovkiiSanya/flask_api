from playhouse.shortcuts import model_to_dict

from users import *
from courses import *

user_course_bp = Blueprint('user_course', __name__)
api = Api(user_course_bp)


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


class UserCourseResource(Resource):
    def post(self):
        data = request.get_json()
        user_id = data.get("user_id")
        course_id = data.get("course_id")
        if not user_id or not course_id:
            return jsonify({"error": "Отстутвует user_id или course_id"}), 400

        result = add_user_course(user_id, course_id)
        if "error" in result:
            return jsonify(result), 404
        return jsonify(result), 200


api.add_resource(UserCourseResource, '/user_course')

if __name__ == "__main__":
    app.run(debug=True)
