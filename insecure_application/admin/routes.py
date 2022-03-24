
from flask import Blueprint, redirect, render_template, session
from utilities.common_functions import check_session_exists
from utilities.constants import *

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/', methods=GET)
def get_admin_dashboard():
    if check_session_exists():
        return render_template('admin-dashboard.html', user_ = session['name'].get())
    return redirect('login.html')