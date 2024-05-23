import datetime
from typing import Tuple

from all_enams import *
from create_db import *
from flask import Flask, jsonify, request, Response,Blueprint
from flask_restful import Api, Resource

users_bp = Blueprint('users', __name__)
api = Api(users_bp)


class User:
    def __init__(self) -> None:
        self.__name: str = None  # User name
        self.__username: str = None  # Username on courses
        self.__age: UserAge = None  # User age
        self.__level: UserLevel = None  # User knowledge level
        self.__date: datetime = None  # User registration

    def set_name(self, name: str):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_username(self, username: str):
        self.__username = username

    def get_username(self):
        return self.__username

    def set_age(self, age: UserAge):
        self.__age = age

    def get_age(self):
        return self.__age.value

    def set_level(self, level: UserLevel):
        self.__level = level

    def get_level(self):
        return self.__level.value

    def set_date(self, date: datetime):
        self.__date = date

    def get_date(self):
        return self.__date


# @app.route("/set_user_info/")
# def set_user_info() -> UserTable | tuple[Response, int]:
#     profile_user = User()
#     name = input("Охаё, представьтесь пожалуйста: ")
#     profile_user.set_name(name)
#     username = input("Отлично, " + profile_user.get_name() + " теперь надо придумать никнейм! ")
#     profile_user.set_username(username)
#     age = input("Теперь надо узнать к какой возрастной группе вы относитесь: \nLIL(16-20)\nMID(21-25)\nOLD("
#                 "26-30)\nOLD_BUT_GOLD(31-40)\nWTF(40)\n").lower()
#     try:
#         age_group = UserAge[age.upper()]
#     except KeyError:
#         print("Вы не попадаете по кнопкам,значит записаны в деды :)")
#         age_group = UserAge.WTF
#     profile_user.set_age(age_group)
#     level = input("Теперь давайте оценим ваш уровень знаний: \nNOOB\nBEGINNER\nMIDDLE\nPRO\nEXPERT\n").lower()
#     try:
#         user_level = UserLevel[level.upper()]
#     except KeyError:
#         print("Установлен начальный уровень знаний")
#         user_level = UserLevel.BEGINNER
#     profile_user.set_level(user_level)
#     date = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
#     profile_user.set_date(date)
#     new_record_table_user = UserTable(
#         user_table_name=profile_user.get_name(),
#         user_table_username=profile_user.get_username(),
#         user_table_age=profile_user.get_age(),
#         user_table_level=profile_user.get_level(),
#         user_table_date=profile_user.get_date()
#     )
#     new_record_table_user.save()
#     new_record_id = new_record_table_user.id
#     print("Ваш персональный ID", new_record_id)
#     return new_record_table_user


class UserListResource(Resource):
    def post(self):
        data = request.get_json()

        profile_user = User()
        profile_user.set_name(data.get("name"))
        profile_user.set_username(data.get("username"))

        age = data.get("age").lower()
        try:
            age_group = UserAge[age.upper()]
        except KeyError:
            age_group = UserAge.WTF
        profile_user.set_age(age_group)

        level = data.get("level", "").lower()
        try:
            user_level = UserLevel[level.upper()]
        except KeyError:
            user_level = UserLevel.BEGINNER
        profile_user.set_level(user_level)

        date = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        profile_user.set_date(date)

        new_record_table_user = UserTable(
            user_table_name=profile_user.get_name(),
            user_table_username=profile_user.get_username(),
            user_table_age=profile_user.get_age(),
            user_table_level=profile_user.get_level(),
            user_table_date=profile_user.get_date()
        )
        new_record_table_user.save()

        return jsonify({"id": new_record_table_user.id})

    def get(self, user_id):
        user = UserTable.get_or_none(UserTable.id == user_id)
        if user:
            return jsonify({
                "id": user.id,
                "name": user.user_table_name,
                "username": user.user_table_username,
                "age": user.user_table_age,
                "level": user.user_table_level,
                "registration_date": user.user_table_date
            })
        else:
            return jsonify({"error": "Пользователь не найден"}), 404

    def put(self, user_id):
        data = request.get_json()
        user = UserTable.get(UserTable.id == user_id)
        user.name = data['name']
        user.username = data['username']
        user.save()
        return jsonify({"message": "Информация обновлена"}), 200

    def delete(self, user_id):
        user = UserTable.get_or_none(UserTable.id == user_id)
        if user:
            user.delete_instance(recursive=True)
            return jsonify({"message": "Пользователь удален"}), 200
        else:
            return jsonify({"error": "Пользователь не найден"}), 404


api.add_resource(UserListResource, '/users', '/users/<int:user_id>')

if __name__ == "__main__":
    app.run(debug=True)
