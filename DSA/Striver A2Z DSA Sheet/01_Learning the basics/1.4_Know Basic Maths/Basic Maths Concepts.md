# Basic Maths Concepts 

---

## 1. Digit Concept (Very Important)

- Take the number = 7789
- We can extract the digits from the number (starting from right to left):
  - `number % 10` = 9 (because nearest 10 divisble number would be 7780, hence the last digit we will get as remainder)
  - `number /10` = 778 (because 7789/10 = int(778.9) = 778)
- Similarly we can extract all the digits from the number by repeating the above 2 steps till we get number/10 == 0

<br>

- Another way of finding the number of digits is finding how many times that number can be divided by 10.
- We can find this by using **Log<sub>10</sub>(number)**
- **Eg:**
```python
from math import log10
def getDigits(n: int) -> None:
    print(f"Number of digits in 7789 = {int(log10(n)+1)}")
```

## 2. Making a number from digits 

- if we given digits like 1,2,3 and told to make a single number out of them (i.e: 123)
- We can do that by multiplying and adding the digits to make the single number 
- **Eg: Reversing a Number**
```
number = 7789
revNum = revNum*10 + lastDigit(number)
```
---

## Questions 

### 1. Count Digits 

- **Problem Statement:**You are given a number ’n’. Find the number of digits of ‘n’ that evenly divide ‘n’.
- Example:
```
Input: ‘n’ = 336

Output: 3

Explanation:
336 is divisible by both ‘3’ and ‘6’. Since ‘3’ occurs twice it is counted two times.
```
- **Code:**
1. Simple approach 
```python 
def countDigits(n: int) -> int:
    num = n 
    count = 0
    while (n>0):
        # print(n)
        i = n%10
        if not i==0 :
            if num%i == 0: 
                count+=1
        n=int(n/10)
        
    return count 
```
2. Log10 approach : 
```python 
from math import log10

def getDigits(n: int) -> None:
    print(f"Number of digits in 7789 = {int(log10(n)+1)}")
```
- `Time Complexity`: **O(log<sub>10</sub>(n))**

> **NOTE:** 
>- if in the question we are dividing by 10 , then Time Complexity will be O(log<sub>10</sub>(n)).
>- If we were dividing by 2 within the loop when the Time complexity would have been O(log<sub>2</sub>(n))
>- Hence **remember** that when ever there is division been done in iterations, the **Time complexity** will have a **logarithmic complexity**

