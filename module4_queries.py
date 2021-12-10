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
avg_age_by_surv = """
    SELECT survived, AVG(age) AS avg_age
    FROM titanic
    GROUP BY survived;
"""
avg_age_by_pclass = """
    SELECT pclass, AVG(age) AS avg_age
    FROM titanic
    GROUP BY pclass
    ORDER BY pclass ASC;
"""
avg_fare_by_pclass_surv = """
    SELECT survived, pclass, AVG(fare) AS avg_fare
    FROM titanic
    GROUP BY survived, pclass;
"""
avg_siblings_spouses = """
    SELECT survived, pclass, AVG("siblings/spouses_aboard") AS avg_sib_spouse
    FROM titanic
    GROUP BY survived, pclass;
"""
avg_parents_children = """
    SELECT survived, pclass, AVG("parents/children_aboard") AS avg_par_chi
    FROM titanic
    GROUP BY survived, pclass;
"""
same_name = """
    SELECT COUNT(DISTINCT name)
    FROM titanic;
"""

print('Num survived and died:')
print(pd.DataFrame(execute_query(num_survived_query), columns=[cur[0] for cur in curs.description]), '\n')

print('Passengers in each class:') 
print(pd.DataFrame(execute_query(num_in_class), columns =[cur[0] for cur in curs.description]), '\n')

print('Survived and died per class:')
print(pd.DataFrame(execute_query(surv_died_per_class), columns = [cur[0] for cur in curs.description]), '\n')

print('Average age per survived or not:')
print(pd.DataFrame(execute_query(avg_age_by_surv), columns = [cur[0] for cur in curs.description]), '\n')

print('Average age per passenger class:')
print(pd.DataFrame(execute_query(avg_age_by_pclass), columns = [cur[0] for cur in curs.description]), '\n')

print('Average fare by survival and pclass:')
print(pd.DataFrame(execute_query(avg_fare_by_pclass_surv), columns = [cur[0] for cur in curs.description]), '\n')

print('Average siblings/spouses:')
print(pd.DataFrame(execute_query(avg_siblings_spouses), columns = [cur[0] for cur in curs.description]), '\n')

print('Average parents/children:')
print(pd.DataFrame(execute_query(avg_parents_children), columns = [cur[0] for cur in curs.description]), '\n')

print('Number of same name:')
print(pd.DataFrame(execute_query(same_name), columns = [cur[0] for cur in curs.description]), '\n')


