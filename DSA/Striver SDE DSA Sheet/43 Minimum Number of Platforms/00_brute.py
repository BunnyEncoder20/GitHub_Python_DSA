from typing import List
def countPlatforms(n:int,arr:List[int],dep:List[int]) -> int:
    # Initialize with minimum number of stations required
    maxStations = 1
    for i in range(n):
        # Cause the current train itself will require a station
        count_stations = 1
        for j in range(i+1,n):
            # Two trains overlap if one's arrival time is between the arrival and departure time of the other.
            # (arr of i train in between arr and dep of j train) or (arr of j train in between arr and dep of i train)
            if (arr[j]<arr[i] and arr[i]<dep[j]) or (arr[i]<arr[j] and arr[j]<dep[i]):
                count_stations+=1
        maxStations = max(count_stations,maxStations)
    return maxStations

if __name__ == "__main__":
    arr = [900, 945, 955, 1100, 1500, 1800]
    dep = [920, 1200, 1130, 1150, 1900, 2000]
    n = len(dep)
    print("Minimum number of Platforms required", countPlatforms(n, arr, dep))