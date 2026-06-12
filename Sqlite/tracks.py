import sqlite3
import csv

# 1. Setup Database
conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

# Make fresh tables
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

# 2. Read and Process CSV
# Ensure tracks.csv is in the same folder as this script
handle = open('tracks.csv', encoding='utf-8')
reader = csv.reader(handle)
next(reader) # Skip the header row

for row in reader:
    # Assuming standard CSV structure: 
    # [Track, Artist, Album, Count, Rating, Len, Genre]
    # Adjust these indices if your CSV is structured differently!
    name = row[0]
    artist = row[1]
    album = row[2]
    count = row[3]
    rating = row[4]
    length = row[5]
    genre = row[6]

    # Normalization: Insert Artist
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES (?)''', (artist,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist,))
    artist_id = cur.fetchone()[0]

    # Normalization: Insert Genre
    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES (?)''', (genre,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre,))
    genre_id = cur.fetchone()[0]

    # Normalization: Insert Album
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?, ?)''', (album, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album,))
    album_id = cur.fetchone()[0]

    # Insert Track
    cur.execute('''INSERT OR REPLACE INTO Track 
        (title, album_id, genre_id, len, rating, count) 
        VALUES (?, ?, ?, ?, ?, ?)''', 
        (name, album_id, genre_id, length, rating, count))

conn.commit()
print("Database created successfully! You can now upload 'tracks.sqlite'.")
