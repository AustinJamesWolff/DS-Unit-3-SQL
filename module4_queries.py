import pandas as pd
import psycopg2

dbname = "jchcvcdb"
user = "jchcvcdb"
password = "p9mdXzV1180WVEG50QrBO3EypSRSOARB"
host = "kashin.db.elephantsql.com"

conn = psycopg2.connect(dbname=dbname, user=user, 
                        password=password, host=host)
curs = conn.cursor()

def execute_query(query, conn=conn, curs=curs):
    curs.execute(query)
    conn.commit()
    return curs.fetchall()

num_survived_query = """
    SELECT COUNT(survived) AS num_survived, 
        COUNT(index) - COUNT(survived) AS num_died
    FROM titanic;
"""
print('Num survived:') 
execute_query(num_survived_query)

# table_info = """
#     SELECT *
#     FROM information_schema.columns;
# """

# print("Table info:", execute_query(table_info))