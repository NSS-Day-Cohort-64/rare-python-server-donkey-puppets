import sqlite3
from models import Post, User
def get_all_posts():
    with sqlite3.connect('db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
           p.id,
           p.user_id,
           p.category_id,
           p.title,
           p.publication_date,
           p.image_url,
           p.content,
           p.approved,
           u.first_name,
           u.last_name
        FROM Posts p
        JOIN User u
            ON p.user_id = u.id
        
        """)
        all_posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            single_post = Post(
                row['id'], row['user_id'], row['category_id'], row['title'],
                row['publication_date'], row['image_url'], row['content'],
                row['approved'])
            all_posts.append(single_post.__dict__)
    return all_posts