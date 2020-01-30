from flask import Blueprint

bp = Blueprint('wot', __name__)

from app.wot import routes