from flask import session, request
from flask_restful import Resource
from models import Task, db

def current_user_id():
    return session.get("user_id")

class TaskList(Resource):
    def get(self):
        user_id = current_user_id()
        if not user_id:
            return {"error": "Unauthorized"}, 401
        page = request.args.get("page", 1, type=int)
        pagination = Task.query.filter_by(user_id=user_id).paginate(page=page, per_page=5)
        return {
            "tasks": [t.to_dict() for t in pagination.items],
            "total": pagination.total,
            "pages": pagination.pages,
            "page": page
        }, 200

    def post(self):
        user_id = current_user_id()
        if not user_id:
            return {"error": "Unauthorized"}, 401
        data = request.get_json()
        task = Task(title=data["title"], description=data["description"], user_id=user_id)
        db.session.add(task)
        db.session.commit()
        return task.to_dict(), 201


class TaskDetail(Resource):
    def get_task_or_error(self, id):
        user_id = current_user_id()
        if not user_id:
            return None, {"error": "Unauthorized"}, 401
        task = Task.query.get_or_404(id)
        if task.user_id != user_id:
            return None, {"error": "Forbidden"}, 403
        return task, None, None

    def patch(self, id):
        task, err, code = self.get_task_or_error(id)
        if err:
            return err, code
        data = request.get_json()
        if "title" in data:
            task.title = data["title"]
        if "description" in data:
            task.description = data["description"]
        if "completed" in data:
            task.completed = data["completed"]
        db.session.commit()
        return task.to_dict(), 200

    def delete(self, id):
        task, err, code = self.get_task_or_error(id)
        if err:
            return err, code
        db.session.delete(task)
        db.session.commit()
        return {}, 204