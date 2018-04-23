import sqlite3

conn = sqlite3.connect('emaildb.sqllite')
cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS Counts
''')

cur.execute(''' 
CREATE TABLE Counts (email TEXT, count INTEGER)
''')

#fname = input('Enter file name:')
#if(len(fname)< 1 ): 
fname = 'mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From '): continue
    pieces = line.split()
    email = pieces[1]
    row = cur.fetchone()

    if row is None:
        cur.execute('''INSERT INTO Counts(email, count) VALUES (?,1)''',(email,))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1  WHERE email = ?  ''',(email,))

    conn.commit()

sqlstr = 'SELECT * FROM Counts '

#print(cur.execute(sqlstr))
for row in cur.execute(sqlstr):
   print(row[0],row[1])

cur.close
