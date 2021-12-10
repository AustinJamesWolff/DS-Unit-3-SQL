import pandas as pd
import psycopg2
from sqlalchemy import create_engine
data_url = 'https://raw.githubusercontent.com/bloominstituteoftechnology/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv'
df = pd.read_csv(data_url)
df['Name'] = df['Name'].str.replace('"',"'", regex=False)
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ","_")
print(df.columns)
# print(df['Name'])
# print(df.head())
# print(df.columns)
# print(df.info())
# print(df[1:5])
characters = list(df.itertuples(index=False, name=None))
dbname = "jchcvcdb"
user = "jchcvcdb"
password = "p9mdXzV1180WVEG50QrBO3EypSRSOARB"
host = "kashin.db.elephantsql.com"

engine = create_engine("postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}".format(
            dbuser=user,
            dbpass=password,
            dbhost=host,
            dbname=dbname
    )
)

conn = psycopg2.connect(dbname=dbname, user=user, 
                        password=password, host=host)
curs = conn.cursor()
def execute_query(curs, conn, query):
    results = curs.execute(query)
    conn.commit()
    return results
create_titanic_table = """
    CREATE TABLE IF NOT EXISTS titanic (
        passenger_id SERIAL PRIMARY KEY,
        survived FLOAT NOT NULL,
        pclass INT NOT NULL,
        name TEXT NOT NULL,
        sex TEXT NOT NULL,
        age FLOAT NOT NULL,
        siblings_spouses_aboard INT NOT NULL,
        parents_children_aboard INT NOT NULL,
        fare FLOAT NOT NULL
    );
"""

if __name__ == "__main__":
    # execute_query(curs, conn, create_titanic_table)
    # # print(df['Pclass'])
    # for row in characters:
    #     insert_titanic_data = """
    #         INSERT INTO titanic (survived, pclass, name, sex, age, 
    #         siblings_spouses_aboard, parents_children_aboard, fare)
    #         VALUES {};
    #     """.format(row)
    #     execute_query(curs, conn, insert_titanic_data)
    df.to_sql("titanic", engine, if_exists="append")


    print(df[1:5])
  