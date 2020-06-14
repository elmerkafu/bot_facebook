import os
from flask import json, request, jsonify
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def handler_response(app, code_error, output, validate=True, payload=None):
    if payload is None:
        payload = {}

    response_object = {
        'response': {
            'system_message': output,
            'api_response': payload,
            'validate': validate,
            'status_code': code_error
        }
    }

    response = app.response_class(
        response=json.dumps(response_object),
        status=code_error,
        mimetype='application/json'
    )

    return response


