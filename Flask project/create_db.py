from peewee import *

connection = PostgresqlDatabase("courses_db",
                                host="127.0.0.1", user="admin", password="root"
                                )


class BaseModel(Model):
    class Meta:
        database = connection


class UserTable(BaseModel):
    user_table_name = TextField(column_name="name")
    user_table_username = TextField(column_name="username")
    user_table_age = TextField(column_name="age")
    user_table_level = TextField(column_name="actual level")
    user_table_date = DateTimeField(column_name="registration_date")


class CoursesTable(BaseModel):
    courses_table_price = TextField(column_name="price")
    courses_table_direction = TextField(column_name="direction")
    courses_table_level = TextField(column_name="courses level")
    courses_table_duration = TextField(column_name="duration")
    courses_table_language = TextField(column_name="language")
    courses_table_date = DateTimeField(column_name="start courses")


class UserCourse(BaseModel):
    user = ForeignKeyField(UserTable, backref='courses', on_delete='CASCADE')
    course = ForeignKeyField(CoursesTable, backref='users', on_delete='CASCADE')

    class Meta:
        database = connection
        primary_key = CompositeKey('user', 'course')


connection.connect()
connection.create_tables([UserTable, CoursesTable, UserCourse])
