import sqlite3
import json
from models import Category

CATEGORY = [
    {
        "id": 1,
        "label": "News"
    }
]

def get_all_categories():
    """function to get all categories"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM Categories c
        """)

        dataset = db_cursor.fetchall()

        # Fetch the categories and store them in a list of Category objects
        categories = [Category(row['id'], row['label']) for row in dataset]

        # Sort the categories alphabetically based on the 'label' property
        categories.sort(key=lambda x: x.label)

    return [category.__dict__ for category in categories]

def get_single_category(id):
    """function to get single location"""
    with sqlite3.connect("./data.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            c.id,
            c.label
        FROM categories c
        WHERE c.id = ?
        """, (id,))

        data = db_cursor.fetchone()

        if data is None:
            # The species with the given ID was not found, return a 404 error response
            return {
                "error": "Category not found",
                "status": 404
            }
        else:
            # Create a species instance from the current row
            category = Category(data['id'], data['label'])
            return category.__dict__

def create_category(new_category):
    """function to create new owner"""
    with sqlite3.connect("./data.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            ( label )
        VALUES
            ( ? );
        """, (new_category['label'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_category['id'] = id


    return new_category

def delete_category(id):
    """function to delete snake"""
    with sqlite3.connect("./data.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM categories
        WHERE id = ?
        """, (id, ))

def update_category(id, new_category):
    """function to update animal"""
    with sqlite3.connect("./data.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Species
            SET
                label = ?
        WHERE id = ?
        """, (new_category['label'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True