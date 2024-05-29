
from flask import Flask
from all_user_staff.users import users_bp
from all_courses_staff.courses import courses_bp
from user_course import user_course_bp
from flasgger import Swagger
from all_enams import *

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(courses_bp, url_prefix='/courses')
app.register_blueprint(user_course_bp, url_prefix='/user_course')
app.register_blueprint(enams_bp, url_prefix='/enams')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
