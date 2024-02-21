import requests 

def fetch_random_user_freeApi():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"

    response = requests.get(url)    # the response is in string format
    object = response.json()          # converting the response into json object
    #print(type(object))               # dict now

    if object['success'] and "data" in object:
        print(object['message'])
        userData = object['data']['data']
        
        for user in userData:
            print(f"Email \t:\t {user['email']}")
            print(f"Name \t:\t {user['name']['title']} {user['name']['first']} {user['name']['last']}")
            print(f"Gender \t:\t {user['gender']}")
            print(f"Country :\t {user['location']['country']}")
            print("\n"+"*"*70)
    
    else : 
        raise Exception("Failed to fetch user data")
        
    
if __name__ == '__main__':
    
    try : 
        fetch_random_user_freeApi()
    except Exception as e :
        print(str(e))
        
    