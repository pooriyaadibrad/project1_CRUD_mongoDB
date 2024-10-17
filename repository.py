from  pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client['CRUD']
persons = db['persons']


def init():
    pass


def register(person):
    persons.insert_one(person)