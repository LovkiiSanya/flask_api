from create_db import *
from user_course import *
from users import *
from courses import *

app = Flask(__name__)
api = Api(app)

# Регистрация Blueprint'ов
app.register_blueprint(courses_bp)
app.register_blueprint(users_bp)
app.register_blueprint(user_course_bp)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
