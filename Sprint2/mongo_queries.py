import pymongo
import mongo_pipeline as mp

client = pymongo.MongoClient("mongodb+srv://austinwolff:Austinwolff0808@cluster0.htev8.mongodb.net/test2?retryWrites=true&w=majority")
db = client.test2

# print(db.characters.find_one())

print("Total characters:", db.characters.count_documents({}))

get_items = """
    SELECT *
    FROM armory_item;
"""

# print(mp.execute_query(mp.create_sl_conn().cursor(), get_items))

def item_doc_creation(mongo_db, item_list):
    for char in item_list:
        item_doc = {
            'name': char[1],
            'value': char[2],
            'weight': char[3],
        }
        mongo_db.items.insert_one(item_doc)

item_doc_creation(db, mp.execute_query(mp.create_sl_conn().cursor(), get_items))

print(db.items.find_one({}))

# print("Total items:", db.characters

# )
