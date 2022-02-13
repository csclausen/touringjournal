import functools
from flask import (
    Blueprint, request, session, jsonify,
)
from flaskserver.controllers.auth import UserAPI


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('POST',))
def register():
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')

    if any(x is None for x in [username, password, email]):
        return jsonify({'error': 'Missing fields'}), 400

    user = UserAPI().register_user(username, email, password)

    return jsonify(user), 200


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
        session['user_id'] = user['id']

        return jsonify(user), 200

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
