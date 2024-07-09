# Allocating Books or Book Allocation 

- Given an array ‘arr of integer numbers, `ar[i]` represents the number of pages in the `i-th` book. There are a `m` number of students, and the task is to allocate all the books to the students.
- Allocate books in such a way that:
    - Each student gets at least one book.
    - Each book should be allocated to only one student.
    - Book allocation should be in a contiguous manner.
- You have to allocate the book to `m` students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1
- Examples : 
```
Example 1:
Input Format:
 n = 4, m = 2, arr[] = {12, 34, 67, 90}
Result:
 113
Explanation:
 The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.
```
```
Example 2:
Input Format:
 n = 5, m = 4, arr[] = {25, 46, 28, 49, 24}
Result:
 71
Explanation: The allocation of books will be 25, 46 | 28 | 49 | 24.
```

<br>

## Brute Force Approach 

- [Watch it here](https://youtu.be/Z0hwjftStI4?si=qU6tDllAcXhb4Wt2&t=410)
1. We will be using Linear Search to find the maximum number of pages required to assign all the books to the number of students 
2. We Figured out the range for Linear Search will be low=max(pages_arr) and high = sum(pages_arr)
3. This is cause worst case can be only one student and in that case all the books will go to him i.e; all pages will go to one student. 
4. Low is set to max no. pages of any book as that way one student can get any of the books in the pages_arr

### Code 

```python
def findPages(arr, n, m):
    low = max(arr)
    high = sum(arr)
    
    for pages in range(low,high+1):
        count_students = allocate_books(arr,pages)
        if count_students == m:
            return pages

def allocate_books(arr,max_pages):
    students = 1
    pages_with_student = 0
    for i in range(len(arr)):
        if pages_with_student + arr[i] <= max_pages:
            pages_with_student+=arr[i]
        else:
            students+=1
            pages_with_student = arr[i]
    return students


if __name__ =="__main__":
    arr = [25, 46, 28, 49, 24]
    n = 5
    m = 4
    ans = findPages(arr, n, m)
    print("The answer is:", ans)
```
- Time complexity : O(sum-(max+1) x N)
- Space complexity : O(1)

<br>

## Optimal Approach

### Algorithm 

- [Watch it here](https://youtu.be/Z0hwjftStI4?si=7HhxEkzNyAKSvSYO&t=1083)
1. We will use Binary Serach to optimize the Algo.
2. We know that the range was low=max(pages) and high=sum(pages).
3. Low = max(pages) required 5 students
4. High = sum(pages) required 1 student
5. Hence the answer should lie somewhere in between (in our case it was 71 which required 4 students)
6. so pages to the left of the mid would have less limit and hence require more student 
7. and pages towards the right have more limit per student and require less number of students

<br>

### Code 

```python
def findPages(arr, n, m):
    if m>n :    # book allocation impossible 
        return -1
        
    low = max(arr)
    high = sum(arr)
    while low<=high:
        mid = (low+high)//2
        no_students = count_students(arr,mid)
        if no_students>m : 
            low = mid+1
        else: 
            high = mid-1
    return low

def count_students(arr,max_pages):
    count = 1
    pages_with_student = 0
    for i in range(len(arr)):
        if pages_with_student+arr[i] <= max_pages:
            pages_with_student += arr[i]
        else:
            count+=1
            pages_with_student = arr[i]
    return count

if __name__ =="__main__":
    arr = [25, 46, 28, 49, 24]
    n = 5
    m = 4
    ans = findPages(arr, n, m)
    print("The answer is:", ans)
```
- Time complexity : O( log<sub>2</sub>(sum-(max+1)) x N )
- Space complexity : O(1)

<br>

---
---