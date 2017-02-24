from flask import Blueprint, jsonify, request

routes_blueprint = Blueprint('routes', __name__)


@routes_blueprint.route('/')
def hello_world():
    return 'hello world'
