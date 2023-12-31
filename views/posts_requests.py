import sqlite3
from models import Post, User, Category

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
           u.last_name,
           u.email,
           u.bio,
           u.username,
           u.password,
           u.profile_image_url,
           u.created_on,
           u.active,
           c.label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        """)
        all_posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            single_post = Post(
                row['id'], row['user_id'], row['category_id'], row['title'],
                row['publication_date'], row['image_url'], row['content'],
                row['approved'])
            single_user = User(
                row['id'], row['first_name'], row['last_name'], row['email'], row['bio'], row['username'],
                row['password'], row['created_on'], row['active'],
            )
            single_category = Category(
                row['id'], row['label']
            )
            single_post.user = single_user.__dict__
            single_post.category = single_category.__dict__
            all_posts.append(single_post.__dict__)
            all_posts_sorted = sorted(
                all_posts, key=lambda post: str(post['publication_date']), reverse=True)
    return all_posts_sorted

def get_post_by_id(id):
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
           u.id as user_id,
           u.first_name,
           u.last_name,
           u.email,
           u.bio,
           u.username,
           u.password,
           u.created_on,
           u.active,
           c.id as category_id,       
           c.label
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE p.id = ?
        """, (id,))
    data = db_cursor.fetchone()

    post = Post(
                data['id'], data['user_id'], data['category_id'], data['title'],
                data['publication_date'], data['image_url'], data['content'],
                data['approved'])
    single_user = User(
                data['user_id'], data['first_name'], data['last_name'], data['email'], data['bio'], data['username'],
                data['password'], data['created_on'], data['active'],
            )
    single_category = Category(data['category_id'], data['label'])
    
    post.user = single_user.__dict__
    post.category = single_category.__dict__
    return post.__dict__

def create_post(new_post):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Posts
            ( user_id, category_id, title, publication_date, image_url, content, approved )
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?);
        """, (new_post['user_id'], new_post['category_id'], new_post['title'],
              new_post['publication_date'], new_post['image_url'], new_post['content'], new_post['approved']
              ))

        id = db_cursor.lastrowid

        new_post['id'] = id

    return new_post

def delete_post(id):
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Posts
        WHERE id = ?
        """, (id, ))