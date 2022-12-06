from sqlite3 import Error
import sqlite3
from time import ctime


def post_sql_query(sql_query):
    with sqlite3.connect('./my.db') as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(sql_query)
        except Error:
            pass
        result = cursor.fetchall()
        return result


def create_tables():
    users_query = '''CREATE TABLE IF NOT EXISTS USERS
                        (user_id INTEGER PRIMARY KEY NOT NULL,
                        username TEXT,
                        first_name TEXT,
                        last_name TEXT,
                        lang TEXT,
                        reg_date TEXT);'''

    post_sql_query(users_query)

def create_menu_table():
    query = '''CREATE TABLE "menu" (
	"id"	INTEGER,
	"name"	TEXT,
	"lang"	TEXT,
	"answer"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);'''
    post_sql_query(query)
create_menu_table()

def register_user(user, username, first_name, last_name):
    user_check_query = f'SELECT * FROM USERS WHERE user_id = {user};'
    user_check_data = post_sql_query(user_check_query)
    if not user_check_data:
        insert_to_db_query = f'INSERT INTO USERS (user_id, username, first_name,  last_name, reg_date) VALUES ' \
                             f'({user}, "{username}", "{first_name}", "{last_name}", "{ctime()}");'
        post_sql_query(insert_to_db_query)

create_tables()

def update_lang(user_id, lang):
    sql_query = f"UPDATE USERS set lang='{lang}' where user_id={user_id}"
    post_sql_query(sql_query)


def key_lang_list(user_id):
    sql_query = f"SELECT * FROM menu WHERE lang='kkkl'"
    return post_sql_query(sql_query)

def key_answer_update(answer, cid, lang):
    sql_query = f"UPDATE menu set answer='{answer}' where type={cid} and lang='{lang}'"
    post_sql_query(sql_query)

def get_answer(text, lang):
    sql = f"select answer from menu where name='{text}' and lang='{lang}'"
    result = post_sql_query(sql)
    return result[0][0]

def user_lang(user_id):
    sql_query = f"SELECT lang FROM USERS WHERE user_id='{user_id}'"
    return post_sql_query(sql_query)[0][0]