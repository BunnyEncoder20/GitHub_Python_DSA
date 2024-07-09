def aggressiveCows(stalls, k):
    n = len(stalls)
    limit = max(stalls)-min(stalls)
    stalls.sort()
    print(stalls)
    for i in range(min(stalls),max(stalls)+1):
        if not can_we_place(stalls,i,k):
            return i-1
    
    return limit

def can_we_place(arr,distance,no_of_cows):
    count_cows = 1
    last_cow_position = arr[0]

    for i in range(len(arr)):
        if arr[i]-last_cow_position >= distance:
            last_cow_position = arr[i]
            count_cows += 1
            if count_cows >= no_of_cows : 
                return True
        else:
            continue
    return False

if __name__ == "__main__":
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4
    ans = aggressiveCows(stalls, k)
    print("The maximum possible minimum distance between cows is:", ans)