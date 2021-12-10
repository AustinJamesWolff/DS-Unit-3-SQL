import psycopg2

conn = psycopg2.connect(dbname='omptepfv',
                        user='omptepfv',
                        password='rTaXKB1JSlwLwcaGnF5MQi3xmS6pe_JT',
                        host='kashin.db.elephantsql.com'
)

cur = conn.cursor()

cur.execute(
    """
    """
)

print(cur.fetchone())