import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    #Creating table as per requirement
    sql ='''CREATE TABLE IF NOT EXISTS Users(
        column_1 INTEGER NOT NULL PRIMARY KEY,
        user CHAR(20) NOT NULL,
        pword CHAR(20),
        user_type INTEGER DEFAULT 2
    );'''
    cursor.execute(sql)
    conn.close()