##############################################]
#authors : d.aboud / p.alexandre / q.gourier  |
#project : PMI                                |
#date    : 22-jan-23                          |
##############################################]

import sqlite3, datetime

def create_db():
    # Create the table
    c.execute('''CREATE TABLE parking_lots
                (lot_id INTEGER, status INTEGER, last_modified TIMESTAMP)''')
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def update_status(status_list):
    now = datetime.datetime.now()
    for i, status in enumerate(status_list):
        id = i+1
        c.execute("UPDATE parking_lots SET status = ?, last_modified = ? WHERE lot_id = ?", (status, now, id))
    conn.commit()

def insert(status_list):
    # Insert initial status in the database
    for i, status in enumerate(status_list):
        id = i+1
        c.execute("INSERT INTO parking_lots (lot_id, status, last_modified) VALUES (?,?,?)", (id, status, datetime.datetime.now()))
    conn.commit()

def read():
    # Read data from the table
    c.execute("SELECT * FROM parking_lots")
    print(c.fetchall())
    conn.commit()
    conn.close()

def delete():
    # Delete data from the table
    c.execute("DELETE FROM parking_lots WHERE lot_id = 2")
    conn.commit()
    conn.close()


# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('parking_lots.db')
# Create a cursor object
c = conn.cursor()

# create_db() #enable for db creation

    

