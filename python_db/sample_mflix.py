from connection import Database
from bson import ObjectId

db = Database("sample_mflix")

print(db.list_collection_names())

movies_collection = db.get_collection("movies")

print(movies_collection.find_one())

new_movie = {
    "plot": "Two robbers robbing",
    "genres": "boring",
    "runtime": 11,
    "cast": ["boc", "frei"],
    "poster": "nan",
    "title": "boc and the robbers",
}

result = movies_collection.insert_one(new_movie)

print(result.inserted_id)
print()

document_to_find = {"_id" : ObjectId("6ae48a97e3ffa29a1b227fce")}

result = movies_collection.find_one(document_to_find)

print(result)

document_to_find = {"runtime": {"$gt": 11}}

result = movies_collection.find_one(document_to_find)

print(result)
print()

document_to_update = {"runtime": {"$gt": 9}}
update = {"$inc": {"runtime": 10}}

movies_collection.update_one(document_to_update, update)

db.close()