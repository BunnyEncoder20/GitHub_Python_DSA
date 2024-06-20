# Minimum Number of Platforms required for a Railway

- We are given two arrays that represent the `arrival` and `departure` times of trains that stop at the platform. We need to find the minimum number of platforms needed at the railway station so that no train has to wait.

<br>

## Brute Force Approach 

- We figure out the number of max intersections in the arrays

### Algorithm

- [Watch it here](https://youtu.be/AsGzwR_FWok?si=7XpeAggl0GQTQMiO&t=216)
-  Iterate over the arrays and find the max number of intersections occuring.
-  That will be the number of stations required
-  There are 4 cases of intersections

<br>

### Code 

```python
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
```
- **Time complexity : O(n<sup>2</sup>)**
- **Space complexity : O(1)**

<br>

## Optimal Approach 

### ALgorithm 

- [Watch it here](https://youtu.be/AsGzwR_FWok?si=Rkl7Y9HuGslr00mJ&t=659)
- Sort the arr and dep arrays according to time
- Put 2 pointers at the start of each array.
- when an arrival happens, increase the count 
- when a departure happens, decrease the count 
- update the max count

### Code 

```python 
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
```
- **Time complexity : O(2n)**
- **Space complexity : O(1)**