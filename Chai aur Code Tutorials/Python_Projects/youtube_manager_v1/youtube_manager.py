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
    print('*'*70)
    for index,video in enumerate(videos, start=1) : 
        print(f"ID: {index} | Title: {video['name']}\t Time: {video['time']}")
    print('*'*70)

def add_video(videos):
    name = input("Enter the Video title: ")
    time = input("Enter the Video time: ")
    videos.append({'name':name, 'time':time})
    save_data(videos)
    print(f"✅ {name} video added to list successfully")

def update_video(videos):
    list_all_videos(videos)
    while True : 
        try:
            index = int(input("Enter the ID of the video you want to update: "))
            if(1 <= index <= len(videos)):
                break
            else:
                raise ValueError
        except ValueError:
            print("❗ Please Enter a valid index\n")
    
    new_name = input("Enter the new name: ")
    new_time = input("Enter new time: ")
    videos[index-1] = {'name':new_name, 'time':new_time} #[index-1] cause enumerate displays the indexes starting from 1 but we know that indexing in python starts from 0
    save_data(videos)
    print(f"✅ ID{index} video details updated successfully")
    
        

def delete_video(videos):
    list_all_videos(videos)
    while True : 
        try:
            index = int(input("Enter the ID of the video you want to Delete: "))
            if(1 <= index <= len(videos)):
                break
            else:
                raise ValueError
        except ValueError:
            print("❗ Please Enter a valid index\n")
    
    del videos[index-1]
    save_data(videos)
    print(f"✅ ID{index} video deleted successfully")
    

def main():
    videos = load_data()
    while True:
        print("\n ✨ YouTube Manager ✨")
        print("1. List all Youtube videos 📃")
        print("2. Add a Youtube video 🖼️")
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