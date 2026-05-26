import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "quotes.db")

def get_all_quotes():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM quotes")

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]

def create_quote(text, author):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO quotes (text, author) VALUES (?, ?)",
        (text, author)
    )

    conn.commit()
    conn.close()

def update_quote_db(quote_id, text, author):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "UPDATE quotes SET text=?, author=? WHERE id=?",
        (text, author, quote_id)
    )

    conn.commit()
    conn.close()

def delete_quote_db(quote_id):
    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM quotes WHERE id=?",
        (quote_id,)
    )

    conn.commit()
    conn.close()