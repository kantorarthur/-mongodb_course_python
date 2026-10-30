import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


class Database:

    def __init__(self, db_name: str) -> None: 
        uri = os.environ["MONGODB_URI"]
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        print("Succesfully connected to {} database".format(db_name))

    def get_collection(self, name: str) -> str:
        return self.db[name]

    def list_collection_names(self) -> list[str]:
        return self.db.list_collection_names()


    def close(self) -> None:
        self.client.close()

