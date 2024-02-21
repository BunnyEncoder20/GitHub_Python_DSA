import os 
from dotenv import load_dotenv, dotenv_values
from pymongo import MongoClient
from bson import ObjectId   # for converting the id displayed into a bson ObjectId for matching purpose

# loading the env file 
load_dotenv()

# Connecting to the mongoDB client 
client = MongoClient(os.getenv("MONGODB_URL"), tlsAllowInvalidCertificates=True)
# tlsAllowInvalidCertificates=True is not a good practice, we had to use it because we can not using any standard python framework for development. When building in those frameworks, we don't need to worry about this
# print(client)

# IN production usually the database name will be given like this
db = client["youtube_manager_db"]

# making a new collection in the database
video_collection = db["videos_list"]
# print(video_collection)



def list_all_videos() : 
    if 0 < video_collection.count_documents({}) :
        print(); print('*'*70)
        for video in video_collection.find():
            print(f"ID:{video['_id']} \t| Title: {video['name']} \t| Time: {video['time']}")
        print('*'*70)
    else :
        print(); print('*'*70)
        print("❕ No videos records found. Please add some videos first")
        print('*'*70)
        
    

def add_video():
    name = input("Enter the Video title: ")
    time = input("Enter the Video duration: ")
    video_collection.insert_one({
        "name":name,
        "time":time 
    })
    print(f"✅ {name} video added to list successfully")

def update_video():
    list_all_videos()
    while True : 
        try:
            video_id = ObjectId(input("Enter the ID of the video you want to update: "))
            break
        except Exception :
            print("❗ Please Enter a valid index\n")
    new_name = input("Enter the new Title : ")
    new_time = input("Enter the new time : ")
    
    video_collection.update_one(
        {
            '_id':video_id
        },
        {
            "$set":{"name":new_name, "time":new_time}
        }
    )
    
    print(f"✅ ID{video_id} video details updated successfully")

def delete_video():
    list_all_videos()
    while True : 
        try:
            video_id = ObjectId(input("Enter the ID of the video you want to delete: "))
            break
        except Exception :
            print("❗ Please Enter a valid index\n")
    
    video_collection.delete_one({
        '_id':video_id
    })
    print(f"✅ ID{video_id} video deleted successfully")

if __name__ == "__main__":
    while True: 
        print("\n ✨ YouTube Manager with DB ✨")
        print("1. List all Youtube videos 📃")
        print("2. Add a Youtube video 🖼️")
        print("3. Update a Youtube video details 📝")
        print("4. Delete a Youtube video ❌")
        print("5. Exit the app 👋")
        
        
        choice = input("Enter your choice : ")
        
        match choice :
            case '1' : 
                list_all_videos()
            case '2' : 
                add_video()
            case '3' :
                update_video()
            case '4' :
                delete_video()
            case '5' : 
                break    # to come out of the while True loop
            case _ : print("❕ Invalid choice, enter a Number between 1-5")
