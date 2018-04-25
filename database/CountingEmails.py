import sqlite3
import urllib.request

con = sqlite3.connect('test.sqlite')
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS Org''')
cur.execute(''' CREATE TABLE  Org (person  int, count varchar(255))''')
fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From'): continue
    words = line.split()
    email = words[1].split('@')[1]
    
    if  cur.fetchone is None:
        cur.execute('''INSERT INTO Org(email,count) VALUES(?,1) ''',(email,))
    else:
        cur.execute('''UPDATE Org SET count = count + 1 WHERE email=? ''',(email,))

con.commit()
   
sqlstr = 'SELECT * FROM Org '

for row in con.execute(sqlstr):
    print(row[0],row[1])  

  