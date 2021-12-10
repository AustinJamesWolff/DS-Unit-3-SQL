
import pymongo
client = pymongo.MongoClient("mongodb+srv://austinwolff:Austinwolff0808@cluster0.htev8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

result = db.test.insert_one({'stringy key': [2, 'thing', 3]})
print(result.inserted_id)
# print(db.test.find_one({'stringy key' : [2, 'thing', 3]}))

db.test.insert_one({'x':1})
# print(db.test.find_one({'x':1}))

cursor = db.test.find({'x':1})
# print(list(cursor))

ryan = {
    'name': 'Ryan',
    'fav_food': 'tacos',
    'lucky_num': 6
    }

bob = {
    'name': 'Bob',
    'fav_food': 'Burgers',
    'has_cat': True
    }

doc_list = [ryan, bob]
db.test.insert_many(doc_list)
# print(list(db.test.find()))

print(db.test.find_one({'fav_food':'Burgers'}))
db.test.delete_one({'x':1})
# print(list(db.test.find()))

result = db.test.update_one({'x':1}, {'$inc':{'x':3}})
print(result.matched_count)



