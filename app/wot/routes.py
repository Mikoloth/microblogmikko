from flask import render_template, redirect, url_for, flash, request
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user, login_required
from flask_babel import _
from app import db
from app.wot import bp
from app.models import User
from urllib.request import urlopen
import os
import json

@bp.route('/wot')
@bp.route('/wot/<username>')
@login_required
def wot(username):
    if username:
        user = User.query.filter_by(username=username).first_or_404()
    else:
        user = current_user

    #https://api.worldoftanks.eu/wot/account/info/?application_id=932b8056c47d21338cb76aa065a05514&account_id=507769638
    json_url = urlopen("https://api.worldoftanks.eu/wot/account/info/?application_id="+os.environ['WOT_API_KEY']+"&account_id="+user.wotid)
    data = json.loads(json_url.read())

    nickdata = data["data"][user.wotid]["nickname"]
    trees = str(data["data"][user.wotid]["statistics"]["trees_cut"])

    #next_url = url_for('main.user', username=user.username,
    #                   page=posts.next_num) if posts.has_next else None
    #prev_url = url_for('main.user', username=user.username,
    #                   page=posts.prev_num) if posts.has_prev else None
    return render_template('wot/wot.html', user=user, nickdata=nickdata, trees=trees)