
from all_enams import *
from flask import Blueprint
from flask_restful import Api
from serializer import *
from all_user_staff.create_user_logic import *

users_bp = Blueprint('users', __name__)
api = Api(users_bp)


@users_bp.route('/', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'users',
                'required': ['name', 'username', 'age', 'profession'],
                'properties': {
                    'id': {'type': 'integer', 'description': 'The unique identifier of a user'},
                    'name': {'type': 'string', 'description': 'User name'},
                    'username': {'type': 'string', 'description': 'User username'},
                    'age': {'type': 'string', 'description': 'User age group'},
                    'profession': {'type': 'string', 'description': 'User profession'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'User created',
            'schema': {
                'id': 'users',
                'properties': {
                    'id': {'type': 'integer', 'description': 'The unique identifier of a user'},
                    'name': {'type': 'string', 'description': 'User name'},
                    'username': {'type': 'string', 'description': 'User username'},
                    'age': {'type': 'string', 'description': 'User age group'},
                    'profession': {'type': 'string', 'description': 'User profession'},
                    'date': {'type': 'string', 'description': 'Date of registration'}
                }
            }
        },
        400: {
            'description': 'Invalid input'
        }
    }
})
def create_user():
    data = request.get_json()

    return create_user_logic(data)


@users_bp.route('/<int:user_id>', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'Fetch a user given its identifier',
            'schema': {
                'id': 'users',
                'properties': {
                    'id': {'type': 'integer', 'description': 'The unique identifier of a user'},
                    'name': {'type': 'string', 'description': 'User name'},
                    'username': {'type': 'string', 'description': 'User username'},
                    'age': {'type': 'string', 'description': 'User age group'},
                    'profession': {'type': 'string', 'description': 'User profession'},
                    'date': {'type': 'string', 'description': 'Date of registration'}
                }
            }
        },
        404: {'description': 'User not found'}
    }
})
def get_user(user_id):
    user = UserTable.get_or_none((UserTable.id == user_id) & (UserTable.is_deleted == False))
    if user:
        user_serializer = UserSerializer(user)
        return jsonify(user_serializer.serialize())
    else:
        return jsonify({"error": "Пользователь не найден"}), 404


@users_bp.route('/<int:user_id>', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'id': 'users',
                'required': ['name', 'username', 'age', 'level'],
                'properties': {
                    'name': {'type': 'string', 'description': 'User name', 'example': 'Test Name'},
                    'username': {'type': 'string', 'description': 'User username', 'example': 'Test Username'},
                    'age': {'type': 'string', 'description': 'User age group', 'example': 'old'},
                    'profession': {'type': 'string', 'description': 'User profession', 'example': 'streamer'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'User updated'},
        404: {'description': 'User not found'}
    }
})
def put_user(user_id):
    data = request.get_json()
    user = UserTable.get_or_none((UserTable.id == user_id) & (UserTable.is_deleted == False))
    if user:
        user.user_table_name = data.get("name", user.user_table_name)
        user.user_table_name = data.get("username", user.user_table_username)
        user.user_table_profession = data.get("profession", user.user_table_profession)
        age = data.get("age")
        if age is not None:
            age = age.lower()
            try:
                age_group = UserAge[age.upper()]
            except KeyError:
                age_group = UserAge.WTF
            user.user_table_age = age_group.value
        user.save()
        return jsonify({"message": "Пользователь обновлен"}), 200
    else:
        return jsonify({"error": "Пользователь не найден"}), 404


@users_bp.route('/<int:user_id>', methods=['DELETE'])
@swag_from({
    'responses': {
        204: {'description': 'User deleted'},
        404: {'description': 'User not found'}
    }
})
def delete_user(user_id):
    user = UserTable.get_or_none(UserTable.id == user_id)
    if user:
        user.is_deleted = True
        user.save()
        return jsonify({"message": "Пользователь удален"}), 200
    else:
        return jsonify({"error": "Пользователь не найден"}), 404
