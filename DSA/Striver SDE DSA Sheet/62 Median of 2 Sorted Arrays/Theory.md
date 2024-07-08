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

