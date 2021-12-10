import pandas as pd
import numpy as np
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
    SELECT survived, COUNT(*)
    FROM titanic
    GROUP BY survived;
"""
num_in_class = """
    SELECT pclass, COUNT(*)
    FROM titanic
    GROUP BY pclass;
"""
surv_died_per_class = """
    SELECT survived, pclass, COUNT(*)
    FROM titanic
    GROUP BY survived, pclass;
"""

print('Num survived and died:')
print(pd.DataFrame(execute_query(num_survived_query), columns=[cur[0] for cur in curs.description]))
print()

print('Passengers in each class:') 
print(pd.DataFrame(execute_query(num_in_class), columns =[cur[0] for cur in curs.description]))
print()

print('Survived and died per class:')
print(pd.DataFrame(execute_query(surv_died_per_class), columns = [cur[0] for cur in curs.description]))
print()



