import sqlite3
conn = sqlite3.connect("BangDiemSV.db")
c=conn.cursor()
c.execute("""
    create table sinh_vien(
            ID int,
            ten varchar,
            dia_chi varchar,
            nam_sinh varchar,
            toan int,
            ly int,
            hoa int,
            primary key(ID)
    )          
""")