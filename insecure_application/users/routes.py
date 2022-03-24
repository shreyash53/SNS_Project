
from flask import render_template, request, session, Blueprint
from utilities.constants import *
from .controller import authenticate, add_user

blueprint = Blueprint("User", __name__, url_prefix="/user")


@blueprint.route('/signup', methods = POST)
def signup():
    form = request.form
    
    return add_user(form)
    
    
@blueprint.route('/login', methods = POST)
def login():
    form = request.form
    return authenticate(form)
    