import sqlite3
from models import Comment
def get_comments_by_post_id(query):
    with sqlite3.connect('db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content
        FROM Comments c
        WHERE c.post_id = ?
        """, (query,))
        data = db_cursor.fetchall()
        comments = []
        for row in data:
            comment = Comment(row['id'], row['post_id'], row['author_id'], row['content'])
            comments.append(comment.__dict__)
        return comments
