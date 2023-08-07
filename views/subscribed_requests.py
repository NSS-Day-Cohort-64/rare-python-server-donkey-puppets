import sqlite3
from models import Post, Subscription
def get_subscribed_posts(follower_id):
     with sqlite3.connect('db.sqlite3') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            s.id,
            s.follower_id,
            s.author_id,
            s.created_on,
            p.id as post_id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved
        FROM Subscriptions s
        JOIN Posts p
            ON p.user_id = s.author_id
        WHERE s.follower_id = ?
    """, (follower_id,))
        dataset = db_cursor.fetchall()
        subscriptions = []
        for row in dataset:
            subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_on'])

            post = Post(row['post_id'], row['user_id'], row['category_id'], row['title'],
                row['publication_date'], row['image_url'], row['content'],
                row['approved'])
            subscription.post = post.__dict__

            subscriptions.append(subscription.__dict__)
        return subscriptions
        