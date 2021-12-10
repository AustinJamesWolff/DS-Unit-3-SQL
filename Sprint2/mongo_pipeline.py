import sqlite3
import pymongo

test_characters = [
    (1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1), 
    (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1)
]

# Open a connection to Mongo
def create_mdb_conn(collection_name):
    client = pymongo.MongoClient("mongodb+srv://austinwolff:Austinwolff0808@cluster0.htev8.mongodb.net/test2?retryWrites=true&w=majority")

    db = client.test2
    collection = db.collection_name
    return db

# Create document to insert into Mongo
def char_doc_creation(mongo_db, character_list):
    for char in character_list:
        character_doc = {
            'name': char[1],
            'level': char[2],
            'exp': char[3],
            'hp': char[4],
            'strength': char[5],
            'intelligence': char[6],
            'dexterity': char[7],
            'wisdom': char[8]
        }
        mongo_db.characters.insert_one(character_doc)

# Connect to SQLite
def create_sl_conn(source_db='rpg_db.sqlite3'):
    sl_conn = sqlite3.connect(source_db)
    return sl_conn

# Execute a SQLite Query
def execute_query(curs, query):
    return curs.execute(query).fetchall()

get_characters = """
    SELECT *
    FROM charactercreator_character;
"""

if __name__ == "__main__":
    # Mongo connection
    db = create_mdb_conn('characters')
    # print(db)

    # SQLite connection
    sl_conn = create_sl_conn()
    sl_curs = sl_conn.cursor()

    # Get characters from SQLite
    characters = execute_query(sl_curs, get_characters)

    # Create documents in Mongo
    char_doc_creation(db, characters)