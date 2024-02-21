import os 
from dotenv import load_dotenv, dotenv_values
from pymongo import MongoClient

# loading the env file 
load_dotenv()

# Connecting to the mongoDB client 
client = MongoClient(os.getenv("MONGODB_URL"))
print(client)

# IN production usually the database name will be given like this
db = client["youtube_manager_db"]

# making a new collection in the database
video_collection = db["videos_list"]
print(video_collection)
