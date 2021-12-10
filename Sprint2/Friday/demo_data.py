import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

create_table = """
    CREATE TABLE IF NOT EXISTS demo (
        s VARCHAR(30) NOT NULL,
        x INT NOT NULL,
        y INT NOT NULL
    );
"""

curs.execute(create_table)