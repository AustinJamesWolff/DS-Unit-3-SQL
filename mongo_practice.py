
import pymongo
client = pymongo.MongoClient("mongodb+srv://austinwolff:Austinwolff0808@cluster0.htev8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test

result = db.test.insert_one({'stringy key': [2, 'thing', 3]})
print(result.inserted_id)
print(db.test.find_one({'stringy key' : [2, 'thing', 3]}))
