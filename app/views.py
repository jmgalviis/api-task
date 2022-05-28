import datetime

import jwt
from flask import Blueprint, request
from werkzeug.security import generate_password_hash, check_password_hash

from config import DevelopmentConfig
from .models.user import User
from .respsonses import response, not_found
from .respsonses import bad_request
from .models.task import Task
from .user_schemas import user_schema
from .utils.set_task import set_task
from .utils.token_required import token_required
from .schemas import task_schema
from .schemas import tasks_schema
from .schemas import params_task_schema

api_v1 = Blueprint('api', __name__, url_prefix='/api/v1')


@api_v1.route('/tasks', methods=['GET'])
@token_required
def get_tasks():
    tasks = Task.query.all()

    return response(tasks_schema.dump(tasks))


@api_v1.route('/tasks/<id>', methods=['GET'])
@set_task
def get_task(task):
    return response(task_schema.dump(task))


@api_v1.route('/tasks', methods=['POST'])
def create_task():
    json = request.get_json(force=True)

    error = params_task_schema.validate(json)
    if error:
        print(error)
        return bad_request()

    task = Task.new(json['title'], json['description'], json['deadline'])
    if task.save():
        return response(task_schema.dump(task))

    return bad_request()


@api_v1.route('/tasks/<id>', methods=['PUT'])
@set_task
def update_task(task):
    json = request.get_json(force=True)

    task.title = json.get('title', task.title)
    task.description = json.get('title', task.description)
    task.deadline = json.get('title', task.deadline)

    if task.save():
        return response(task_schema.dump(task))

    return bad_request()


@api_v1.route('/tasks/<id>', methods=['DELETE'])
@set_task
def delete_task(task):
    if task.delete():
        return response(task_schema.dump(task))

    return bad_request()


@api_v1.route('/register', methods=['POST'])
def signup_user():
    json = request.get_json(force=True)
    hashed_password = generate_password_hash(json['password'], method='sha256')
    user = User.new(json['username'], json['name'], hashed_password)
    if user.save():
        return response(user_schema.dump(user))

    return bad_request()


@api_v1.route('/login', methods=['GET', 'POST'])
def login_user():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return bad_request()

    user = User.query.filter_by(username=auth.username).first()

    if user is None:
        return not_found()

    if check_password_hash(user.password, auth.password):
        token = jwt.encode({
            'uuid': user.uuid,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, DevelopmentConfig.SECRET_KEY)
        print(type(token))
        return response(token.decode('UTF-8'))

    return bad_request()
