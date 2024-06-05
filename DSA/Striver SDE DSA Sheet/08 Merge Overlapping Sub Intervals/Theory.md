# Merge Overlapping Sub Intervals

- Problem states that given a arr of sub intervals, we have to merge all overlapping intervals and give a array which covers all the intervals without overlapping.

```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6]
```
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

---

## Brute Force Solution

- **Time Complexity : O(nlogn) + O(2n)** [sorting + for loops]
- **Space Complexity :  O(n)**

### Algorithm 

1. Sort the sub intervals (so that close intervals are grouped together)
2. Iterate over the sub arrays, **if the first element of a sub Interval is less or equal to the last element of the previous sub interval, then they are overlapping**.
3. In order to accumilate the overlap, we remove the current and previous sub interval and **replace it with a sub interval which contains the first element of the previous sub interval and the lsat element of the current sub interval**.
4. If the last element of the next sub interval is **not overlapping** (It is greater than the last element of the previous sub interval) then we have gotten our corrected sub interval.

<br>

### Code 

```python
# Brute Solution for Sub interval Overlapping 
# Time Complexity : O(nlogn) + O(2n) [sorting + for loops]
# Space Complexity :  O(n)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = []

        for i in range(n):
            start_interval = intervals[i][0]
            end_interval = intervals[i][1]

            # Check if answer has some interval, if yes then we need to check if the next intervals are within it or not (because they are already processed)
            if ans and end_interval<=ans[-1][1]:
                continue

            # Check the next sub intervals, if overlapping, update the end_interval
            for j in range(i+1,n):
                if intervals[j][0] <= end_interval:
                    end_interval = max(end_interval,intervals[j][1])    # Note that sometimes the next intervals can be within the interval, hence we need to check which last element  is greater 
                else:
                    break
            
            ans.append([start_interval,end_interval])

        return ans

if __name__ == '__main__':
    ins = Solution()
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]        
    intervals2 = [[1,4],[4,5]]
    print(ins.merge(intervals1))
    print(ins.merge(intervals2))
```

---

## Optimal Solution 

- In the previous approach, one of our pointers (i) was standing will j checked the next intervals. We need to avoid this in order to reduce the Time complexity.
- **Time Complexity : O(nlogn) + O(n)** [sorting + for loops]
- **Space Complexity :  O(n)**


### Algorithm

1. Iterate over the sub intervals 
2. If the first element more than the last element of the ans, it is a new interval.
3. If the first element more than the last element of the ans, it is a part of the previous subinterval, and we need to update the last element of the previous ans interval.

### Code

```python 
# Optimal Solution for Sub interval Overlapping 
# Time Complexity : O(nlogn) + O(n) [sorting + for loops]
# Space Complexity :  O(n)

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = []

        for i in range(n):

            # Check if we need to make a new ans interval
            if not ans or ans[-1][1]<intervals[i][0]:
                ans.append(intervals[i])

            # Check if the interval is overlapping with previous ans interval
            else:
                ans[-1][1] = max(ans[-1][1],intervals[i][1])

        return ans


if __name__ == '__main__':
    ins = Solution()
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]        
    intervals2 = [[1,4],[4,5]]
    print(ins.merge(intervals1))
    print(ins.merge(intervals2))
```