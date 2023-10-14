import sqlite3
conn = sqlite3.connect("donhang.db")
c=conn.cursor()
c.execute("""
    create table san_pham(
            maSP int,
            ten varchar,
            nam int,
            dia_chi varchar,
            gia_thanh int,
            so_luong int,
            primary key(maSP)
    )          
""")