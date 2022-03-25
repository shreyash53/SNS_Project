
from flask import redirect, render_template, session
from .model import Blog
from utilities.database_queries import data_add, data_delete

def get_all_blogs():
    return Blog.query.order_by(Blog.modified_time.desc()).all()

def add_blog(form_data):
    try:
        # print('eheeee',form_data['blog_title'] == '', form_data['blog_content'] == '')
        blog_ = Blog(**form_data, blog_user=session['name'].user_id)
        data_add(blog_)
        return redirect('/login')
    except Exception as e:
        print('error...', e)
        return redirect('/login')
    
def delete_all_blogs():
    data_delete(Blog)