from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user, login_required
from flask_babel import _
from app import db
from app.wot import bp
from app.models import User

@bp.route('/wot')
@bp.route('/wot/<username>')
@login_required
def user(username):
    if username:
        user = User.query.filter_by(username=username).first_or_404()
    else:
        user = current_user

    nickdata = "nick dataa"

    #next_url = url_for('main.user', username=user.username,
    #                   page=posts.next_num) if posts.has_next else None
    #prev_url = url_for('main.user', username=user.username,
    #                   page=posts.prev_num) if posts.has_prev else None
    return render_template('wot/wot.html', user=user, nickdata=nickdata)