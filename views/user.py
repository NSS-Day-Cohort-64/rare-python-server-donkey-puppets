import sqlite3
import json
from datetime import datetime
from models import User

def get_all_users():
  
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT id, first_name, last_name, email, bio, username, profile_image_url, created_on, active
            FROM Users
            ORDER BY username
        """)

        users_from_db = db_cursor.fetchall()

        # Format the result into a list of dictionaries
        users_list = []
        for user in users_from_db:
            user_dict = {
                'id': user['id'],
                'first_name': user['first_name'],
                'last_name': user['last_name'],
                'email': user['email'],
                'bio': user['bio'],
                'username': user['username'],
                'profile_image_url': user['profile_image_url'],
                'created_on': datetime.strptime(user['created_on'], '%Y-%m-%d').strftime('%B %d, %Y'),
                'active': user['active']
            }
            users_list.append(user_dict)

        return users_list

def get_user_by_id(id):
    with sqlite3.connect('db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT 
           u.id,
           u.first_name,
           u.last_name,
           u.email,
           u.bio,
           u.username,
           u.password,
           u.profile_image_url,
           u.created_on,
           u.active
        FROM Users u
        WHERE id = ? 
        """, (id,))
    data = db_cursor.fetchone()
    user = User(
                data['id'], data['first_name'], data['last_name'], data['email'], data['bio'], data['username'],
                data['password'], data['profile_image_url'], data['created_on'], data['active'],
            )
    return user.__dict__
def login_user(user):

    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            select id, username
            from Users
            where username = ?
            and password = ?
        """, (user['username'], user['password']))

        user_from_db = db_cursor.fetchone()

        if user_from_db is not None:
            response = {
                'valid': True,
                'token': user_from_db['id']
            }
        else:
            response = {
                'valid': False
            }

        return json.dumps(response)


def create_user(user):
    with sqlite3.connect('./db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        Insert into Users (first_name, last_name, username, email, password, bio, created_on, active) values (?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            user['first_name'],
            user['last_name'],
            user['username'],
            user['email'],
            user['password'],
            user['bio'],
            datetime.now()
        ))

        id = db_cursor.lastrowid

        return json.dumps({
            'token': id,
            'valid': True
        })
