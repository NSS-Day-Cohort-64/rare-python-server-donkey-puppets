import sqlite3
from models import Post, Subscription, Category
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
            p.approved,
            c.id as category_id,
            c.label
        FROM Subscriptions s
        JOIN Posts p
            ON p.user_id = s.author_id
        JOIN Categories c
            ON c.id = p.category_id
        WHERE s.follower_id = ?
    """, (follower_id,))
        dataset = db_cursor.fetchall()
        subscriptions = []
        for row in dataset:
            subscription = Subscription(row['id'], row['follower_id'], row['author_id'], row['created_on'])

            post = Post(row['post_id'], row['user_id'], row['category_id'], row['title'],
                row['publication_date'], row['image_url'], row['content'],
                row['approved'])
            
            category = Category(row['category_id'], row['label'])
            subscription.post = post.__dict__
            subscription.category = category.__dict__

            subscriptions.append(subscription.__dict__)
        return subscriptions
        
def create_subscription(new_subscription):
    """ Creates a new subscription """
    with sqlite3.connect("./db.sqlite3") as conn:
        
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO "Subscriptions"
            ( follower_id, author_id, created_on )
        VALUES
            ( ?, ?, ? );
        """, (new_subscription['follower_id'], new_subscription['author_id'], new_subscription['created_on'], ))

        id = db_cursor.lastrowid

        new_subscription['id'] = id

    return new_subscription
