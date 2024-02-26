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

### 1. Count Digits [CodingNinjas](https://www.codingninjas.com/studio/problems/count-digits_8416387)

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

---

### 2. Reversing an Integer - [LeetCode](https://leetcode.com/problems/reverse-integer/description/)

- **Problem Statement:** Given a signed 32-bit integer x, return x with its digits reversed. 
- If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
- **Examples:**
```
Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
```

- **Solution**
```python 
class Solution:
    def reverse(self, x: int) -> int:
        revNum = 0
        isPositive = True if x>0 else False
        x = abs(x)
        originalNum = x
        while x>0 :
            lastDigit = x%10
            if not (x==originalNum and lastDigit==0):
                revNum = revNum*10 + lastDigit
            x = int(x/10)
        if  -2**31<revNum<2**31-1 :
            return revNum if isPositive else -revNum 
        else : 
            return 0
```

---

### 3. Palindrome Numbers - [LeetCode](https://leetcode.com/problems/palindrome-number/)

- **Problem Statement:** Given an integer x, return true if x is a
palindrome, and false otherwise.
```
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
```

- **Solution**
```python 
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x != 0 and (x < 0 or x%10==0) : return False
        originalNum = x
        revNum = 0
        while x>0 : 
            lastDigit = x%10
            revNum = revNum*10 + lastDigit
            x = int(x/10)
        if revNum == originalNum : 
            return True
        else :
            return False
```

---

### 4. Armstrong Numbers 

- **Problem Statement:** 

- **Examples** 
```
Sample Input 1 : 1
Sample Output 1 : true

Sample Input 2 : 103
Sample Output 2 : false
```
- Expected Time Complexity: `O(log(n))`. 

- **Solution**
```python
digits = []
originalNum = int(input())
duplicateNum = originalNum

while duplicateNum>0 : 
    lastDigit = duplicateNum%10
    digits.append(lastDigit)
    duplicateNum = int(duplicateNum/10)

sum = 0
for digit in digits:
    sum += digit**len(digits)

if sum==originalNum:
    print("true")
else:
    print("false")
```