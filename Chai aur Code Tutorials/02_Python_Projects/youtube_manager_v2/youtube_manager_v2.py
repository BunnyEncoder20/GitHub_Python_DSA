import sqlite3

def list_all_videos(cursor):
    records = cursor.execute('SELECT * FROM videos').fetchall() # storing the results of .fetchall() is better as it can be used only once after executing the query

    if (0<len(records)):
        print(); print('*'*70)
        for row in records:
            print(f"ID:{row[0]} |\t Title: {row[1]}\t Time: {row[2]}")
        print('*'*70)
    else : 
        print(); print('*'*70)
        print("❕ No videos records found. Please add some videos first")
        print('*'*70)

def add_video(cursor, conn):
    name = input("Enter the Video title: ")
    time = input("Enter the Video time: ")
            
    cursor.execute("INSERT INTO videos (name, time) VALUES (? , ?)",(name, time))
    conn.commit()     # in SQLite we use the commit() method to save our changes to the db
    print(f"✅ {name} video added to list successfully")

def update_video(cursor, conn):
    list_all_videos(cursor)
    while True : 
        try:
            index = int(input("Enter the ID of the video you want to update: "))
            break
        except :
            print("❗ Please Enter a valid index\n")
    new_name = input("Enter the new Title : ")
    new_time = input("Enter new time : ")
    
    # Notice that we do not do index-1 here cause the indexing of the DB rows starts from 1
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name, new_time, index))
    conn.commit()     # remember that commit is a function of the connection object and not the cursor object
    print(f"✅ ID{index} video details updated successfully")

def delete_video(cursor, conn):
    list_all_videos(cursor)    
    while True : 
        try:
            index = int(input("Enter the ID of the video you want to delete: "))
            break
        except :
            print("❗ Please Enter a valid index\n")
    
    cursor.execute("DELETE FROM videos WHERE id = ?",(index,))
    # NOTE : we have to put the trailing ',' otherwise only 1 (variable) in the () will not be treated like a tuple & will cause errors 
    
    conn.commit()
    print(f"✅ ID{index} video deleted successfully")




def main():
    conn = sqlite3.connect('youtube_manager.db')
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')
    # Remember that ''' ''' is used when we want to send the string with the exact format (spaces and tabs) in which it is given (import for SQL queries)
    
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
                list_all_videos(cursor)
            case '2' : 
                add_video(cursor, conn)
            case '3' :
                update_video(cursor, conn)
            case '4' :
                delete_video(cursor, conn)
            case '5' : 
                break    # to come out of the while True loop
            case _ : print("❕ Invalid choice, enter a Number between 1-5")

    conn.close()        # closing the connection to the database
    
    
if __name__ == '__main__':
    main()