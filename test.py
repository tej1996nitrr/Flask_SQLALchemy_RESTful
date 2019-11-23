import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "create table users(id int,username text,password text)"
cursor.execute(create_table)
insert_query = "insert into users values(?,?,?)"
users = [
(1,'fox','asdf'),
(2,'monkey','qwer'),
(3,'bear','zxcv')
]
cursor.executemany(insert_query,users)
connection.commit()

