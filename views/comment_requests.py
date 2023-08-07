import sqlite3
from models import Comment, User, Post
def get_comments_by_post_id(id):
    with sqlite3.connect('db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            u.id as user_pk,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.created_on,
            u.active,
            p.id as post_pk,
            p.user_id as post_user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content as post_content,
            p.approved
        FROM Comments c
        JOIN Users u
            ON c.author_id = user_pk
        JOIN Posts p
            ON c.post_id = post_pk
        WHERE c.post_id = ?
        """, (id,))
        data = db_cursor.fetchall()
        comments = []
        for row in data:
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])
            comments.append(comment.__dict__)
            user = User(
                row['user_pk'], row['first_name'], row['last_name'], row['email'], row['bio'], row['username'],
                row['password'], row['created_on'], row['active'],
            )
            post = Post(
                row['post_pk'], row['post_user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'],
                row['post_content'], row['approved'],
            )
            comment.user = user.__dict__
            comment.post = post.__dict__
        return comments
def create_comment(post_body):
    with sqlite3.connect('./db.sqlite3') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            (post_id, author_id, content)
        VALUES(?, ?, ?);
        """, (post_body['post_id'], post_body['author_id'], post_body['content']))

        id = db_cursor.lastrowid

        post_body['id'] = id
    return post_body

def delete_comment(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))