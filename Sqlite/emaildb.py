import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)
''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: '):
        continue

    pieces = line.split()
    email = pieces[1]

    # Extract organization/domain
    org = email.split('@')[1]

    cur.execute(
        'SELECT count FROM Counts WHERE org = ?',
        (org,)
    )

    row = cur.fetchone()

    if row is None:
        cur.execute(
            'INSERT INTO Counts (org, count) VALUES (?, 1)',
            (org,)
        )
    else:
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?',
            (org,)
        )

# Commit once after processing all records
conn.commit()

cur.close()