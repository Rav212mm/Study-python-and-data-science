import sqlite3

class Database:

    def __init__(self, db):
        conn = sqlite3.connect(db)
        self.cur = conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        conn.commit()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",
                    (title, author, year, isbn))
        conn.commit()
        conn.close()

    def view(self):
        self.cur.execute('SELECT * FROM book')
        rows = cur.fetchall()
        conn.close()
        return rows

    def search(self, title='', author='', year='', isbn=''):
        self.cur.execute("SELECT * from book WHERE title=? OR author=? OR year=? OR isbn=?",
                    (title, author, year, isbn))
        rows = cur.fetchall()
        conn.close()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        conn.commit()
        conn.close()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                    (title, author, year, isbn, id))
        conn.commit()
        conn.close()

#connect()
#insert('The Sun', 'John', 1350, 10)
#delete(3)
#update(4, "The moon", "John Smooth", 12, 442)
#print(view())
#print(search(author='John Smooth'))