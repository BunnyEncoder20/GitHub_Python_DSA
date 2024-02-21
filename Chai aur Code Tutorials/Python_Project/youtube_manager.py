import json
filename = 'youtube_manager_db.txt'

def load_data():
    try: 
        with open(filename, 'r') as file:
            return json.load(file)  # fetches the file if there and converts the data within it to json
    except FileNotFoundError:
        return []
    
def save_data(videos):
    with open(filename, 'w') as file:
        json.dump(videos, file)     # json function to write with params for what to write and where to write
        

def list_all_videos(videos):
    print()
    print('*'*100)
    for index,video in enumerate(videos, start=1) : 
        print(f"{index}. Title: {video['name']}\t Time: {video['time']}")
    print()
    print('*'*100)

def add_video(videos):
    name = input("Enter the Video title: ")
    time = input("Enter the Video time: ")
    videos.append({'name':name, 'time':time})
    save_data(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

def main():
    videos = load_data()
    while True:
        print("\n ✨ YouTube Manager ✨")
        print("1. List all Youtube videos 📰")
        print("2. Add a Youtube video 📼")
        print("3. Update a Youtube video details 📝")
        print("4. Delete a Youtube video ❌")
        print("5. Exit the app 👋")
        
        
        choice = input("Enter your choice : ")
        
        match choice : 
            case '1' : list_all_videos(videos)
            case '2' : add_video(videos)
            case '3' : update_video(videos)
            case '4' : delete_video(videos)
            case '5' : break    # to come out of the while True loop
            case _ : print("invalid choice, try again")
            
if __name__ == "__main__":
    main()