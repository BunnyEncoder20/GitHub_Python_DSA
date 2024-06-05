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
    