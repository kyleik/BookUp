import sqlite3

def connect():
    conn = sqlite3.connect("bookup.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, isbn integer)")
    conn.commit()
    conn.close()


def insert_book(title, author, isbn):
    conn = sqlite3.connect("bookup.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title, author, isbn))
    conn.commit()
    conn.close()


def view_book():
    conn = sqlite3.connect("bookup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_book(id, title, author, isbn):
    conn = sqlite3.connect("bookup.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, isbn=? WHERE id=?", (title, author, isbn, id))
    conn.commit()
    conn.close()


def search_book(title="",author="",isbn=""):
    conn=sqlite3.connect("bookup.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR isbn=?", (title, author, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_book(id):
    conn = sqlite3.connect("bookup.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id))
    conn.commit()
    conn.close()


connect()
print(view_book())