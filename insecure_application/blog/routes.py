
from flask import Blueprint, request
from utilities.constants import *
from .controller import add_blog, delete_all_blogs

blueprint = Blueprint("blog", __name__, url_prefix="/blog")

@blueprint.route('/add', methods=POST)
def add():
    form = request.form
    return add_blog(form)

@blueprint.route('delete', methods=GET)
def delete():
    delete_all_blogs()
    return "deleted"