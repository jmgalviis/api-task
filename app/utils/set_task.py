from app.models.task import Task
from app.respsonses import not_found


def set_task(function):
    def wrap(*args, **kwargs):
        id = kwargs.get('id', 0)
        task = Task.query.filter_by(id=id).first()
        if task is None:
            return not_found()

        return function(task)
    wrap.__name__ = function.__name__
    return wrap
