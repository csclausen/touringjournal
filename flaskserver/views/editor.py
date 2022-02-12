from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for,
)
from werkzeug.security import generate_password_hash
from flaskserver.db import get_db

from flaskserver.views.auth import login_required

bp = Blueprint('editor', __name__, url_prefix='/editor')

# TODO extract this to middleware
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/new', methods=['GET'])
@login_required
def new():
    return 200

