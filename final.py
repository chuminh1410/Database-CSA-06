import sqlite3
from datetime import datetime

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE Books (
        book_id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        publication_year INTEGER,
        publisher TEXT,
        genre TEXT,
        description TEXT
    )
''')


cursor.execute('''
    CREATE TABLE Members (
        member_id INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        phone_number TEXT,
        emergency_contact TEXT
    )
''')




