def countPlatforms(n,arr,dep)->int:
    arr.sort()
    dep.sort()
    count = 0
    max_count = 0

    pointer1 = 0
    pointer2 = 0
    while pointer1<n:
        if arr[pointer1] < dep[pointer2] : 
            count+=1
            pointer1+=1
        else:
            count-=1
            pointer2+=1
        max_count = max(count,max_count)
        
    return max_count


if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    n = len(dep)
    print("Minimum number of Platforms required", countPlatforms(n, arr, dep))