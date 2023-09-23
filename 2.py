import sqlite3
conn = sqlite3.connect("quan_ly_sinh_vien.db")
c=conn.cursor()
c.execute("""
    create table sinh_vien(
            ma_sv int,
            ten varchar,
            nam_sinh varchar,
            dia_chi varchar,
            lop_hoc varchar,
            diem_toan varchar,
            primary key(ma_sv)
    )          
""")