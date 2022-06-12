from flask import make_response, jsonify
from src import app
from jsonschema import ValidationError


# RESPONSE ON SUCCESSFUL CONTROLLER EXECUTION
def response(success, obj, status_code):
    return make_response(jsonify(success=success, obj=obj), status_code)


# BAD REQUEST EXCEPT
@app.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return make_response(jsonify(success=False, obj={'msg': original_error.message}), 200)
    # handle other "Bad Request"-errors
    return make_response(jsonify(success=False, obj={'msg': error}), 200)
