# Finding the N<sup>th</sup> Root of M

- Given two numbers `N` and `M`, find the N<sup>th</sup> root of `M`. 
- The nth root of a number `M` is defined as a number `X` when raised to the power `N` equals `M`. 
- If the 'nth root is not an integer, return -1.

Example 1:
```
Input Format:
 N = 3, M = 27
Result:
 3
Explanation:
 The cube root of 27 is equal to 3.
```
Example 2:
```
Input Format:
 N = 4, M = 69
Result:
 -1
Explanation:
 The 4th root of 69 does not exist. So, the answer is -1.
```

<br>

## Brute Force Approach 

### Algorithm 

- [Watch it here](https://youtu.be/rjEJeYCasHs?si=zl2RpzmoYhycRmXd&t=74)
- We babsically are given a number `M` of which we need to find the `N`<sup>th</sup> root 
- By using Linear search, we can easily do that
- Run a loop from 1 to M
- If i<sup>N</sup> == M , return i
- If i<sup>N</sup> > M , return -1

### Code 

```python
# Brute way of finding power(base,expo) TC = O(n)
def NthRoot1(n,m):
    for i in range(m):
        if i**n == m :
            return i
        if i**n > m:
            return -1

# Better way of finding power(base,expo) ( less TC = O(log(n)) )
def pow(base,expo):
    ans = 1
    while expo>0:
        if expo%2==0:
            base = base**2
            expo//=2
        else:
            ans*=base
            expo-=1
    return ans

def NthRoot2(n,m):
    for i in range(m):
        if pow(i,n)==m : return i
        if pow(i,n)>m  : return -1
    

if __name__ == "__main__":
    listn = [3,4]
    listm = [27,69]
    n,m=0,0
    while n<len(listn) and m<len(listm):
        # print(f"n:m::{listn[n]}:{listm[m]}")
        print("The answer is:",NthRoot2(listn[n], listm[m]))
        n+=1
        m+=1
```
- **Time complexity : O(M x log<sub>2</sub>N)**
  - Worst case it might keep going till m (eg: n=1,m=69)
- Space complexity : O(1)

<br>

## Optimal Approach (Binary Search)

### Algorithm

- [Watch it here](https://youtu.be/rjEJeYCasHs?si=RKwWf4xAmHVGG6TO&t=276)
- Use BS to cut down the search space of (1,M)
- We use the optimized pow(base,expo) function to calculate the mid<sup>N</sup>

### Code

```python
def NthRoot(n,m)->int:
    low,high = 1,m
    # Binary Search 
    while low<=high:
        mid = (low+high)//2
        if pow(mid,n)==m: return mid
        elif pow(mid,n)<m : low=mid+1
        else: high=mid-1
    return -1

def pow(base,expo):
    ans = 1
    while expo>0:
        if expo%2==0:
            base*=base
            expo//=2
        else:
            ans*=base
            expo-=1
    return ans

if __name__ == "__main__":
    listn = [3,4]
    listm = [27,69]
    n,m=0,0
    while n<len(listn) and m<len(listm):
        # print(f"n:m::{listn[n]}:{listm[m]}")
        print("The answer is:",NthRoot(listn[n], listm[m]))
        n+=1
        m+=1
```
- **Time complexity : O(log<sub>2</sub>(M) x log<sub>2</sub>(N))**
  - This TC is much better than the previous one
- **Space complexity : O(1)**

> **Edge Case** : This code will fail when we take a very large `N`. Hence we need to make the pow() function such that it doesn't compute the asnwer if it is going beyond `M`

```python
def NthRoot(n,m)->int:
    low,high = 1,m
    # Binary Search 
    while low<=high:
        mid = (low+high)//2
        if pow(mid,n,m)==0: return mid
        elif pow(mid,n,m)==1 : low=mid+1
        else: high=mid-1
    return -1

def pow(base,n,m):
    '''
    returns  1 : ans<m
    returns  0 : ans==m
    returns -1 : ans>m
    '''
    ans = 1
    while n>0:
        if n%2==0:
            base*=base
            n//=2
        else:
            ans*=base
            if ans>m : return -1
            n-=1
    if ans == m : return 0
    else : return 1

# Simplier implementation of pow function
# def pow(base,expo,m):
#     '''
#     returns  1 : ans<m
#     returns  0 : ans==m
#     returns -1 : ans>m
#     '''
#     ans = 1
#     for _ in range(expo):
#         ans*=base
#         if ans>m : return -1
#     if ans==m : return 0
#     else : return 1

if __name__ == "__main__":
    listn = [3,4]
    listm = [27,69]
    n,m=0,0
    while n<len(listn) and m<len(listm):
        # print(f"n:m::{listn[n]}:{listm[m]}")
        print("The answer is:",NthRoot(listn[n], listm[m]))
        n+=1
        m+=1
```
