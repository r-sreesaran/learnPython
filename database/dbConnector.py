import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

cur.execute(''' DROP TABLE IF EXISTS Ages ''')
cur.execute(''' CREATE TABLE Ages (name TEXT,age INTEGER) ''')
#cur.execute(''' DELETE * FROM Ages ''')
cur.execute(''' INSERT INTO Ages (name, age) VALUES(?,?) ''',('Tadhg', 15))

cur.execute(''' INSERT INTO Ages (name, age) VALUES(?,?) ''',('Emi', 18))
cur.execute(''' INSERT INTO Ages (name, age) VALUES(?,?) ''',('Rafferty', 24))
cur.execute(''' INSERT INTO Ages (name, age) VALUES(?,?) ''',('Xue', 19))
cur.execute(''' INSERT INTO Ages (name, age) VALUES(?,?) ''',('Nerea', 40))
cur.execute(''' INSERT INTO Ages (name, age) VALUES(?,?) ''',('Sukhvir', 35))

sqlstr = 'SELECT * FROM Ages '


for row in cur.execute(sqlstr):
    print(row[0],row[1])

sqlstr1 ='SELECT hex(name || age) AS X FROM Ages ORDER BY X'
for row in cur.execute(sqlstr1):
    print(row[0])