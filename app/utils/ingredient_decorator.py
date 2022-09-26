
import functools
from flask import jsonify


def entities_wrapper(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        entity, error = func(*args, **kwargs)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    return wrapper
