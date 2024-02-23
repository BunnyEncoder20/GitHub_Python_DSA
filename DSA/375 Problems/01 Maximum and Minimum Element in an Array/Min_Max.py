def minmax(list):
    
    if len(list)%2 == 0 : 
        if list[0] < list[1] :
            mini = list[0]
            maxi = list[1]
        else :
            mini = list[1]
            maxi = list[0]
        i = 2
    else : 
        mini = maxi = list[0]
        i = 2 
    
    while i < len(list)-1 :
        if list[i] < list[i+1] :
            mini = min(mini,list[i])
            maxi = max(maxi,list[i+1])
        else : 
            mini = min(mini, list[i+1])
            maxi = max(maxi, list[i])
        i+=2
    
    return mini,maxi

if __name__ == '__main__':
    arr = [1000, 11, 445, 1, 330, 3000]
    mini,maxi = minmax(arr)
    print(f"Minimum element is {mini}\n Maximum element is {maxi}")