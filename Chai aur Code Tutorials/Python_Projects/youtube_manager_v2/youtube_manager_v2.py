import sqlite3


def list_all_videos(cursor):
    cursor.execute('SELECT * FROM videos')

    print('\n'); print('*'*70)
    for row in cursor.fetchall():
        print(f"ID:{row[0]} |\t Title: {row[1]}\t Time: {row[2]}")
    print('\n'); print('*'*70)

def add_video(cursor, conn):
    name = input("Enter the Video title: ")
    time = input("Enter the Video time: ")
            
    cursor.execute("INSERT INTO videos (name, time) VALUES (? , ?)",(name, time))
    conn.commit()     # in SQLite we use the commit() method to save our changes to the db

def update_video():
    pass

def delete_video():
    pass




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