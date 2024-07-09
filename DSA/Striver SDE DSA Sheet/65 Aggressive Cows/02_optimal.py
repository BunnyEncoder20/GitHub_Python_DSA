def aggressiveCows(stalls, no_of_cows):
    stalls.sort()
    n = len(stalls)
    low = 0
    high = stalls[n-1]-stalls[0]
    
    while low<=high:
        mid = (low+high)//2
        if can_we_place(stalls,mid,no_of_cows):
            # possible answer
            low = mid+1
        else:
            # not possible
            high = mid-1
    
    return high

def can_we_place(stalls,distance,no_of_cows):
    count=1
    last_cow_position = stalls[0]
    
    for i in range(len(stalls)):
        if stalls[i]-last_cow_position>=distance:
            last_cow_position = stalls[i]
            count+=1
            if count >= no_of_cows:
                return True
        else:
            continue
    return False

if __name__ == "__main__":
    stalls = [0, 3, 4, 7, 10, 9]
    k = 4
    ans = aggressiveCows(stalls, k)
    print("The maximum possible minimum distance between cows is:", ans)