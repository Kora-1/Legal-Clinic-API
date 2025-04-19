# from pymongo import MongoClient
#
# MONGO_URI = "mongodb+srv://accforapplinmongodb:tvX6lHov82OI0NTG@cluster0.mongodb.net/?retryWrites=true&w=majority"
#
# client = MongoClient(MONGO_URI)
# db = client.simple_auth_db
# users_collection = db.users


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://accforapplinmongodb:tvX6lHov82OI0NTG@datainfo.nqxv2sl.mongodb.net/?retryWrites=true&w=majority&appName=DataInfo"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.auth_db
users_collection = db.users
history_collection= db.history