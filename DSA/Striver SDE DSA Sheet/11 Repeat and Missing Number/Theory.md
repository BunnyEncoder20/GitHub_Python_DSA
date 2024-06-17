# Repeated and Missing Number

- Given a array of n integers which will have a repeating number and a missing number 
- We have to return the missing number and the repeated number

---

## Brute Force Approach 

- **Time Complexity : O(n<sup>2</sup>)** 
- **Space Complexity : O(1)** 

### Algorithm

- Iterate through the array and count the number of occurrences of each number.
- The missing number will have a frequency of 0
- The repeated number will have a frequency of more than 1

### Code 

```python 
def repeatedNumber(A):
        n = len(A)
        
        for i in range(1,n+1):
            count = 0
            
            for j in range(n):
                if A[j] == i:
                    count += 1
            
            if count == 2: repeating = i
            if count == 0: missing = i
        
        return [repeating, missing]
```

---

## Better Approach 

- Whenever there is optimization of counting elements in an array, we can use **Hashing**.
- **Time Complexity: O(2n)**
- **Space Complexity: O(n)**

### Algorithm

1. Declare a HashArray of **size n+1** (because the number go from 1 to n) and initialize it to 0
2. Start iterating and update the frequencies of the numbers in the HashArray
3. Iterate over the HashArray and find the indexes will frequency = 0 and frequency > 1
4. Return the missing number and repeating number.

### Code 

```python 
 def repeatedNumber(A):
        n = len(A)
        hashArray = [0]*(n+1)
        
        for num in A:
            hashArray[num] += 1
        
        for i in range(1,len(hashArray)) : 
            if hashArray[i] == 2 : repeated = i
            if hashArray[i] == 0 : missing = i
            
        return [repeated,missing]
```

---

## Optimized Approach

- **Time Complexity: O(n)**
- **Space Complexity: O(1)**
- There are 2 optimal solutions:
  1. using Maths  (basic maths used only) 
  2. using XOR    (difficult, avoid in an interview)

### Algorithm

1. Take 2 variables : 
    - x = repeating number 
    - y = missing number
2. S =  summation of all the elements of the array.
3. Sn =  summation of all the n natural numbers `(n*(n+1)/2)`.
4. Now we know that: 
> x - y = S - Sn --- (eq 1)

5. To solve this equation, we need another equation of x and y.
6. This time we will sum up the square of the elements : 
7. S2 = summation of all square of all elements 
8. Sn2 = summation of all square of n natural numbers `(n*(n+1)*(2n+1) / 6 )`
9. Now we know that:
> x<sup>2</sup> - y<sup>2</sup> = S2 - Sn2 
> (x-y)(x+y) = S2 - Sn2 --- (eq 2)
> x + y = S2 - Sn2 / (x - y)
> x + y = S2 - Sn2 / S - Sn --- from eq 1
10. Now we have 2 equations for x and y : 
> x + y = (S2 - Sn2) / (S - Sn)
> x - y = (S - Sn)
11. Solving the equations, we can find our x and y.

### Code

```python
def repeatedNumber(A):
        n = len(A)
        
        S = 0
        Sn = (n*(n+1))//2
        S2 = 0
        Sn2 = (n * (n+1) * (2*n+1)) // 6
        
        for i in range(n):
            S += A[i]           
            S2 += A[i]*A[i]
        
        # Assuming x is repeating number 
        # Assuming y is missing number 
        val1 = S-Sn             # x-y
        val2 = (S2-Sn2)//2      # x+y = (S2-Sn2)/(x-y)
        
        
        
        x = (val1+val2)//2
        y = val2-x
        
        return [x,y]
```

---

