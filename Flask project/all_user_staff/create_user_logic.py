import datetime
from flask import request, jsonify
from all_enams import UserAge
from all_user_staff.user import User
from create_db import UserTable


def create_user_logic(data):
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

    profile_user.set_profession(data.get("profession"))

    date = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    profile_user.set_date(date)

    new_record_table_user = UserTable(
        user_table_name=profile_user.get_name(),
        user_table_username=profile_user.get_username(),
        user_table_age=profile_user.get_age(),
        user_table_profession=profile_user.get_profession(),
        user_table_date=profile_user.get_date()
    )
    new_record_table_user.save()

    return jsonify(new_record_table_user.serialize())
