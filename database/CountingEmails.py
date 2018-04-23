import sqlite3

con = sqlite3.connect('test.sqlite')
cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS Org''')
cur.execute(''' CREATE TABLE  Org (email TEXT, count INTEGER)''')

file = open('mbox.txt')

for line in file:
    if not line.startswith('From'): continue
    words = line.split()
    email = words[1]
    row = cur.fetchone()
    
    