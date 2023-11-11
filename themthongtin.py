import datetime
import sqlite3
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

def add_book(title, author, publication_year, publisher, genre, description):
    cursor.execute('''
        INSERT INTO Books (title, author, publication_year, publisher, genre, description)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (title, author, publication_year, publisher, genre, description))
    conn.commit()



def add_member(name, address, phone_number, emergency_contact):
    cursor.execute('''
        INSERT INTO Members (name, address, phone_number, emergency_contact)
        VALUES (?, ?, ?, ?)
    ''', (name, address, phone_number, emergency_contact))
    conn.commit()


def add_member():

    name = input("Enter member's name: ")
    address = input("Enter member's address: ")
    phone_number = input("Enter member's phone number: ")
    emergency_contact = input("Enter member's emergency contact: ")

    cursor.execute("""
        INSERT INTO Members (name, address, phone_number, emergency_contact)
        VALUES (?, ?, ?, ?)
    """, (name, address, phone_number, emergency_contact))

    conn.commit()
    conn.close()

add_member()

