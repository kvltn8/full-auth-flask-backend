from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_restful import Api

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "super-secret-key"

    db.init_app(app)
    bcrypt.init_app(app)
    Migrate(app, db)

    api = Api(app)

    from resources.auth import Register, Login, Logout, CheckSession
    from resources.tasks import TaskList, TaskDetail

    api.add_resource(Register, "/register")
    api.add_resource(Login, "/login")
    api.add_resource(Logout, "/logout")
    api.add_resource(CheckSession, "/check_session")
    api.add_resource(TaskList, "/tasks")
    api.add_resource(TaskDetail, "/tasks/<int:id>")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)