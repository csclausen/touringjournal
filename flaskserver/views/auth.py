import functools
from flask import (
    Blueprint, request, session, jsonify,
)
from flaskserver.controllers.auth import UserAPI
from mongoengine.errors import NotUniqueError


bp = Blueprint('auth', __name__, url_prefix='/auth')


def user_return_value(user_obj):
    return {
        'id': str(user_obj.id),
        'username': user_obj.username,
        'email': user_obj.email
    }

@bp.route('/register', methods=('POST',))
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if any(x is None for x in [username, password, email]):
        return jsonify({'error': 'Missing fields'}), 400

    try:
        user = UserAPI().register_user(username, email, password)
    except NotUniqueError:
        return jsonify({'error': 'Username or Email in use'}), 400
    if user:
        session.clear()
        session['user_id'] = str(user['id'])

        return user_return_value(user), 200

    return jsonify({'error': 'There was a problem registering this user'}), 500


@bp.route('/login', methods=('POST',))
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if any(x is None for x in [username, password]):
        return jsonify({'error': 'Missing fields'}), 400

    user = UserAPI().get_user_by_login(username, password)

    if user:
        session.clear()
        session['user_id'] = str(user['id'])

        return user_return_value(user), 200

    return jsonify({'error': 'Bad username or password'}), 401


@bp.route('/logout')
def logout():
    session.clear()
    return 200


"""
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = UserAPI().get_user(user_id)
"""


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('user_id') is None:
            return jsonify({'error': 'User not logged in'}), 401

        
        return view(**kwargs)
    
    return wrapped_view
