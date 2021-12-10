import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

try: 
    create_table = """
        CREATE TABLE demo (
            s VARCHAR(30) NOT NULL,
            x INT NOT NULL,
            y INT NOT NULL
        );
    """

    curs.execute(create_table)

    test_data = """
        INSERT INTO demo (s, x, y)
        VALUES ('g', 3, 9),
            ('v', 5, 7),
            ('f', 8, 7);
    """
    curs.execute(test_data)
    conn.commit()
except sqlite3.OperationalError:
    print("We already have the table, see queries below.")

def get_query(query, conn=conn, curs=curs):
    results = curs.execute(query).fetchall()
    conn.commit()
    return results

get_row_count = """
    SELECT COUNT(*) AS num_rows
    FROM demo;
"""

row_count = get_query(get_row_count)[0][0]
print("Row count:", row_count)

least_5 = """
    SELECT COUNT(*) AS num_rows
    FROM demo
    WHERE x >= 5 AND y >= 5;
"""

xy_at_least_5 = get_query(least_5)[0][0]
print("Rows where x and y are at least 5:", xy_at_least_5)

get_unique_y = """
    SELECT COUNT(DISTINCT y)
    FROM demo;
"""

unique_y = get_query(get_unique_y)[0][0]
print('Unique values of y:', unique_y)
