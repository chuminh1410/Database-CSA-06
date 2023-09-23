import sqlite3
conn = sqlite3.connect("MyData.db")
c=conn.cursor()
c.execute("""
    create table Nhan_vien(
            ID int,
            ten varchar,
            nam_sinh varchar,
            dia_chi varchar,
            nghe_nghiep varchar,
            primary key(ID)
    )          
""")