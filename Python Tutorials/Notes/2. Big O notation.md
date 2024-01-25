# Big O notation in DSA
---

## Time Complexity
`Big O notation` is used to measure how **running time** or **space requirements** for your program _grow_ as _input size grows_

A Linear Time Complexity fucniton will have a linear line graph which will follow the math formula : **m*x + c** or **a*n+b** 
Where 
- a is a constant
- b is a constant  
- n is a variable

Rules for getting the time complexity : 
1. Only focus on the fastests growing term 
2. Remove any constants 
So, we get : ***`O(n)` time complexity***
![Image](./Notes%20Assets/O(n).png)

Let's see an example of a program which uses `O(n)` time complexity : 
```
def get_squared_numbers(numbers) :
    squared_numbers=[]
    for n in numbers:
        square_numbers.append(n*n)
    return squared_numbers

numbers = [2,5,8,9]
get _ square _ numbers (numbers)
# returns [4,25,64,81]
```
---

Sometimes the time of execution of the program will not change much with the increase in input size. The execution time would seem to be constant (also seen from it's graph).
***This is a `O(1)` time complexity*** 
![Image](./Notes%20Assets/O(1).png)
Program which has a `O(n)` time complexity : 
```
def sum2nums(num1, num2) : 
    result = num1+num2
    return result
```
Notice how the input size doesn't affect the function's execution time _(because there is no looping or searching happening)_

---

Similarly when there are 2 loops (with one inside the first one) the time complexity increases exponentially given by O(n<sup>2</sup>): 
![Image](./Notes%20Assets/O(n2).png)
An Example of such a program, which finds a duplicate of the number in the list : 
```
numbers = [3,6,2,4,3,6,8,9]

for i range(len(numbers)) : 
    for j in range(i+1, len(numbers)):
        if numbers[i]==numbers[j] :
            print(numbers[i]+" is a duplicate")
            break
```
---
Even when there are more than 1 function, we still apply the basic rules discussed at the beginning : 
1. Only focus on the fastest growing term 
2. Remove any constants 
Eg : 
```
numbers = [3,6,2,4,3,6,8,9]
duplicate = None

for i in range(len(numbers)):
    for j in range(i+l, len(numbers)):      # n^2 iterations
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break   

for i in range(len(numbers)):               # n iterations
    if numbers[i] == duplicate: 
        print (i)

```
The above codes time complexity will be seen as **O(n<sup>2</sup>)** only

BigO refers to very large value of n. Hence only the Largest power will contribute maximum to the term value, hence cause BigO is simple a estimate, we only keep the biggest terms

---

## Space Complexity 
Similar to time complexity when we look at the expansion of space relative to input size we are talking about space complexity 
Let's see the example below of a Binary Search and how it reduces the searching iterations (Hence has a lesser time and space complexity)
![Image](./Notes%20Assets/binarysearchexample.png)
If we use the regular brute force approach we'll get a time complexity of `O(n)` : 
```
for i in range(len(numbers)):
    if numbers [i]==68:
        print (i)
```
Hence if the input elements were a billion numbers, the code will iterate over a billion times , checking each element. This is not efficient for both time and space
Binary Search algo reduces the time and space complexity as shown below : 
![Image](./Notes%20Assets/bsexplaination.png)
Now, converting this into BigO notation : 
![Image](./Notes%20Assets/\../Notes%20Assets/bsBigOnotation.png)


