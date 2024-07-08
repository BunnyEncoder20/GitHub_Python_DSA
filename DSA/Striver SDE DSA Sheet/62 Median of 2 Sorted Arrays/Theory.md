# Median of 2 Sorted Arrays of Different Sizes

- Given two sorted arrays `arr1` and `arr2` of size `m` and `n` respectively, return the median of the two sorted arrays. 
- The median is defined as the middle value of a sorted list of numbers. 
- **In case the length of the list is even, the median is the average of the two middle elements.**

## Brute Force Approach

### Algorithm 

- [Watch it here](https://youtu.be/C2rRzz-JDk8?si=rYasm22ym8a3roCH&t=174)
1. Using Merge sort technique to merge 2 sorted arrays and combine the 2 arrays into a single array
2. Then find the median of that array

### Code 

```python
def median(arr1, arr2):
    left = 0
    right = 0
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = []
    
    # Merging the 2 arrays
    while left<n1 and right<n2 :
        if arr1[left]<=arr2[right]:
            arr3.append(arr1[left])
            left+=1
        else:
            arr3.append(arr2[right])
            right+=1

    if left<=n1:
        arr3.extend(arr1[left:])
    if right<=n2:
        arr3.extend(arr2[right:])
    
    # Finding the median in the arr3
    n = n1+n2
    if n%2==1:
        return arr3[n//2]
    else:
        return (arr3[n/2] + arr3[(n/2)-1])//2
        
if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))
```
- Time complexity : O(n1+n2) 
- Space complexity : O(n1+n2)

<br>

## Better Approach 

- We will try to optimize the space complexity here

### Algorithm 

- [Watch it here](https://youtu.be/C2rRzz-JDk8?si=kLDZasKipowwGUtv&t=523_)
1. We do not need all the elements of the thirss array. 
2. We just need the one or two elements in the middle 
3. This time we just use pointers to find the elements at idx1 (n/2 - 1) and idx2 (n/2)
4. if n (n1+n2) is odd, we return idx2 else we return (idx2+idx1)/2
   
### Code 

```python
def median(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    n = n1+n2
    idx1,idx2 = (n//2)-1, n//2
    count = 0
    ele1 = None
    ele2 = None
    
    # Applly the merge step
    left,right=0,0
    while left<n1 and right<n2 :
        if arr1[left]<=arr2[right]:
            if count==idx1 : 
                ele1 = arr1[left]
            if count==idx2 : 
                ele2 = arr1[left]
                break
            count+=1
            left+=1
        else:
            if count==idx1 : 
                ele1 = arr2[right]
            if count==idx2 : 
                ele2 = arr2[right]
                break
            count+=1
            right+=1

    if not ele1 and not ele2:
        # Do we really need these ? Yes we do. Think about arrays of very unequal sizes
        while left<=n1:
            if count==idx1 : 
                ele1 = arr1[left]
            if count==idx2 : 
                ele2 = arr1[left]
                break    
            left+=1
            count+=1
        while right<=n2:
            if count==idx1 : 
                ele1 = arr2[right]
            if count==idx2 : 
                ele2 = arr2[right]
                break
            right+=1
            count+=1
        
    # Finding the median in the arr3
    if n%2==1:
        return float(ele2)
    else:
        return float(ele1+ele2)/2.0
        
if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))
```
- Time complesxity : O(n+m)
- Space complexity : O(1)

<br>

## Optimal Approach 

- When we get a sorted array, we can always think of a **Binary search** solution 

### Alogrithm 

- [Watch it here](https://youtu.be/F9c7LpRZWVQ?si=LS48EqLYiglo1Hvq&t=221)
1. Just watch the vid, it's too complex to write here

### Code 

```python 
def median(arr1,arr2):
    n1 = len(arr1)
    n2 = len(arr2)

    # To ensure that the smallest array is arr1
    if n1>n2 : return median(arr2, arr1)

    low = 0
    high = n1 
    req_on_left = (n1+n2+1)//2
    n = n1+n2    
    # Binary serach the number of elements we need to take on the left
    while low<=high:
        mid1 = (low+high)//2
        mid2 = req_on_left - mid1

        # elements near the symmtric line default values
        l1,l2 = float('-inf'),float('-inf')
        r1,r2 = float('inf'),float('inf')

        # Check that the index exist before assigning the values to the edge elements 
        if mid1 < n1 : r1 = arr1[mid1]
        if mid2 < n2 : r2 = arr2[mid2]
        if mid1-1 >= 0 : l1 = arr1[mid1-1]
        if mid2-1 >= 0 : l2 = arr2[mid2-1]

        # Checking if this is the symmertric we have been looking for 
        if l1<=r2 and l2<=r1 : 
            if n%2==1 : 
                # assuming there are more elements on the left side
                return float(max(l1,l2))
            else:
                return float(max(l1,l2)+min(r1,r2))/2.0

        # move to the left 
        elif l1 > r2 : high = mid1-1
        else : low = mid1+1 

    return 0 

if __name__ == "__main__":
    a = [1, 4, 7, 10, 12]
    b = [2, 3, 6, 15]
    print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))
```
- **Time complexity : O( log<sub>2</sub>(min(n1,n2)) )**
- **Space complexity : O(1)**