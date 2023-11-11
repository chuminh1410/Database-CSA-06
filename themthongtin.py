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





def add_example_members():
    example_members = [
        ("Nguyễn Văn A", "Hanoi", "555-1234", "555-5678"),
        ("Trần Thị B", "Ho Chi Minh City", "555-9876", "555-4321"),
        ("Lê Văn C", "Da Nang", "555-1111", "555-2222"),
        ("Phạm Thị D", "Hai Phong", "555-3333", "555-4444"),
        ("Hoàng Văn E", "Can Tho", "555-5555", "555-6666"),
        ("Nguyễn Thị F", "Bien Hoa", "555-7777", "555-8888"),
        ("Trần Văn G", "Nha Trang", "555-9999", "555-0000"),
        ("Lê Thị H", "Hue", "555-1212", "555-3434"),
        ("Phạm Văn I", "Vinh", "555-4545", "555-5656"),
        ("Hoàng Thị K", "Buon Ma Thuot", "555-6767", "555-7878"),
    ]

    for member_info in example_members:
        name, city, phone_number, emergency_contact = member_info
        address = city
        add_member(name, address, phone_number, emergency_contact)


add_example_members()




