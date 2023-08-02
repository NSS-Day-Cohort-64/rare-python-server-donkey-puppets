import sqlite3
import json
from models import Tag


def get_all_tags():
    """function to get all tags"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM tags t
        """)

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database

        tags = [Tag(row['id'], row['label']) for row in dataset]

        tags.sort(key=lambda x: x.label)

        # Add the dictionary representation of the animal to the list
    return [tag.__dict__ for tag in tags]


def get_single_tag(id):
    """function to get single tag"""
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM tags t
        WHERE t.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()
        if data is None:
            return {
                "error": "Tag not found",
                "status": 404
            }
        else:

            # Create an animal instance from the current row
            tag = Tag(data['id'], data['label'])

            return tag.__dict__


def create_tag(new_tag):
    """ Creates new tag """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tags
            ( label )
        VALUES
            ( ? );
        """, (new_tag['label'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the tag dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_tag['id'] = id

    return new_tag
