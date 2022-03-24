from flask import session, render_template
from .model import Users
from sqlalchemy.exc import IntegrityError
from utilities.constants import *
from utilities.database_queries import data_add

def add_user(body):
    user = body['user']
    pword = body['pword']
    name = body['name']
    user_obj = Users(
            user=user,
            pword=pword,
            name=name
        )

    try:
        data_add(user_obj)
        return
    except IntegrityError as i:
        print(i)
        return render_template('index.html')
    except Exception as e:
        print("in signup...", e)
        return render_template('error.html')
    
def authenticate(form):
    try:
        user = form['pword']
        pword = form['pword']
        
        user_ = Users.query.filter_by(user=user, pword=pword).first()
        if user_:
            session['name'] = user_
            user_type = user_.user_type
            print('user_type:',user_type)
            if user_type == 1:
                return render_template('admin-dashboard.html')
            elif user_type == 2:
                return render_template('user-dashboard.html')
        return render_template('login.html')
    
    except Exception as e:
        print("in authenticate...\n", e)
        return 0