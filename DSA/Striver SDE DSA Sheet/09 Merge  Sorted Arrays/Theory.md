# Merge two Sorted Arrays in Constant Space 

- Merge 2 Sorted arrays without using any extra space 

## Brute Solution 

- Generally, the question will not mention to solve in constant space. Hence Brute solution involves making an third array.
- **Time Complexity : O(n+m)**
- **Space Complexity: O(n+m)**

### Algorithm 
- Create a third array of size len(arr1)+len(arr2).
- Making 2 pointers starting at start of each of the 2 arrays 
- Iterate over the two arrays, conpare the elements at the pointer and add the smaller element into the answer array. 
- If one of the arr finishes, move all the remaining elements of the other array into the asnwer arr. 

### Code

```python 
# Brute Slution for Merging 2 Sorted arrays 
# Time Complexity : O(n+m)
# Space Complexity: O(n+m)

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ans = []
        index,left,right = 0,0,0

        while left<m and right<n :
            if nums1[left] < nums2[right]:
                ans.append(nums1[left])
                left+=1
            else : 
                ans.append(nums2[right])
                right+=1
        
        ans.extend([nums1[i] for i in range(left,m)])
        ans.extend([nums2[i] for i in range(right,n)])

        return ans
```

---

## Optimal Solution 

### Algorithm 

1. Start with largest element of arr1 (the last element), and the smallest element on arr2 (the first element).
2. Compare them, if they are not in the correct place, swap them. 
3. Move the pointers : lastElement-- and firstElement++
4. Compare again and swap if needed. 
5. Once we get the position where the Elemenets are in there correct position, all the elements after them, do not need swapping (cause they are sorted arrays)
6. Now we sort both of the arrays and that gives us the answer we need. 

### Code 

```python 
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        left,right = n-1,0

        while left>=0 and right<m:
            if(nums1[left]>=nums2[right]):
                nums1[left],nums2[right]=nums2[right],nums1[left]
                left-=1
                right+=1
            else:
                break   # remember why we break here 
        
        nums1.sort()
        nums2.sort()
```

---

## Optimal Solution 2 : Gap method

- This optimal solution uses gap method from the shell sorting method.
- This some how gave better results than the previous optimal method.
- **Time Complexity : O(log<sub>2</sub>(n+m)) + O(n+m)** (because outer loop  keeps diving by 2 and inner loop runs for most cases till n+m)
- **Space Complexity : O(1)** (no extra space used)

### Algorithm 

1. Take the length of the 2 arrays, add them and divide by 2. Take the ceil value of it. This will be the gap
1. Take 2 pointers (on a array with all of the elements of the 2 arrays) with leftIndex+gap number of spaces to rightIndex. 
Eg: if gap = 5 , then left = 0 and right = 5 
1. Loop through the both the arrays and compare the corresponding elements (both pointers move on each loop). 
1. after one of the pointers goes out of index (right pointer will go out of the List), we restart.
1. We again divide the gap by 2 and take it's ceiling value as the new gap.
1. We place the left pointer at 0 and the right pointer after leftIndex+new gap number places 
1. Again compare the elements and swap the elements which are not in the correct place. 
1. We keep doing this until the gap = 1. After which we can end the loop.

### Code 

```python 
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = [nums2[i] for i in range (n)]
        length = m+n
        gap = (length//2)+(length%2)  # eas way of getting the ceil value after divind even or odd number

        while gap>0 : 
            left = 0
            right = left+gap

            while right<length:
                if nums1[left] < nums1[right] :
                    left+=1
                    right+=1
                    continue
                else :
                    nums1[left],nums1[right]=nums1[right],nums1[left]
                    left+=1
                    right+=1
                    
            if gap == 1 : break
            gap = (gap//2)+(gap%2)
```