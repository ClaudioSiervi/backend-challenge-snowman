import sqlite3

connetion = sqlite3.connect('data.db')

cursor = connetion.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# insert a user into database
user = (1, 'claudio', 'qwer')

insert_query = "INSERT INTO users VALUES (?, ?, ?)"
cursor.execute(insert_query, user) # replace each values in the tuple for the question marks

users = [
    (2, 'luciana', 'asdf'),
    (3, 'lucas', 'zxcv')
]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

connetion.commit() # saving the changes into data.db

connetion.close()