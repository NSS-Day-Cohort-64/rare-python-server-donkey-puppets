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
