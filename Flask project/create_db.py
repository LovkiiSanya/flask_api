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
    user_table_profession = TextField(column_name="profession")
    user_table_date = DateTimeField(column_name="registration_date")
    is_deleted = BooleanField(default=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.user_table_name,
            "username": self.user_table_username,
            "age": self.user_table_age,
            "profession": self.user_table_profession,
            "date": self.user_table_date
        }


class CoursesTable(BaseModel):
    courses_table_price = IntegerField(column_name="price USD")
    courses_table_direction = TextField(column_name="direction")
    courses_table_level = TextField(column_name="courses level")
    courses_table_duration = TextField(column_name="duration")
    courses_table_language = TextField(column_name="language")
    courses_table_date = DateTimeField(column_name="start courses")
    is_deleted = BooleanField(default=False)

    def serialize(self):
        return {"id": self.id,
                "price USD": self.courses_table_price,
                "direction": self.courses_table_direction,
                "level": self.courses_table_level,
                "duration": self.courses_table_duration,
                "language": self.courses_table_language,
                "date": self.courses_table_date}


class UserCourse(BaseModel):
    user = ForeignKeyField(UserTable, backref='courses', on_delete='CASCADE')
    course = ForeignKeyField(CoursesTable, backref='users', on_delete='CASCADE')
    is_deleted = BooleanField(default=False)

    class Meta:
        database = connection
        primary_key = CompositeKey('user', 'course')


connection.connect()
connection.create_tables([UserTable, CoursesTable, UserCourse])
