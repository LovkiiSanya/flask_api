class UserSerializer:
    def __init__(self, user):
        self.id = user.id
        self.name = user.user_table_name
        self.username = user.user_table_username
        self.age = user.user_table_age
        self.profession = user.user_table_profession
        self.registration_date = user.user_table_date

    def serialize(self):
        return self.__dict__


class CourseSerializer:
    def __init__(self, courses):
        self.id = courses.id
        self.price = courses.courses_table_price
        self.direction = courses.courses_table_direction
        self.level = courses.courses_table_level
        self.duration = courses.courses_table_duration
        self.language = courses.courses_table_language
        self.start_course = courses.courses_table_date

    def serialize(self):
        return self.__dict__


class UserCourseSerializer:
    def __init__(self, user_course):
        self.user_id = user_course.user_id
        self.course_id = user_course.course_id

    def serialize(self):
        return self.__dict__
