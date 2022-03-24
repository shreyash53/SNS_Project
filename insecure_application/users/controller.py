
import sqlite3
from flask import session

def get_connection():
    conn = sqlite3.connect('database.db')
    return conn

def signup():
    conn = get_connection()
    
    conn.execute('')
    print("Table created successfully")
    conn.close()
    
    
def authenticate(user, pword):
    conn = get_connection()
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users where user=? and pword=?",(user, pword))

        rows = cur.fetchone()

        if rows :
            session['name'] = user
            user_type = rows[3]
            print('user_type:',user_type)
            return user_type
        return 0
    
    except Exception as e:
        print("in authenticate...\n", e)
        return 0
        
    finally:
        conn.close()