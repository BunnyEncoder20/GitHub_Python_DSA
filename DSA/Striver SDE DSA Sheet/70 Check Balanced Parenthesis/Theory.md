# Check for Balanced Parenthesis

- Check Balanced Parentheses. Given string str containing just the characters `'(', ')', '{', '}', '[' and ']'`, check if the input string is valid and return true if the string is balanced otherwise return false.
- Examples 
```
Exmaple 1

Input: str = “( )[ { } ( ) ]”
Output: True

Explanation: As every open bracket has its corresponding 
close bracket. Match parentheses are in correct order 
hence they are balanced.
```
```
Exmaple 2

Input: str = “[ ( )”
Output: False

Explanation: As ‘[‘ does not have ‘]’ hence it is 
not valid and will return false.
```
<br>

## The Only Approach 

- Can solve this using a stack DS

### Algorithm 

- [Watch it here](https://youtu.be/wkDfsKijrZ8?si=nBeVbvkdnJwTAzSh&t=166)
1. When we encounter a opening bracket, we push it into the stack
2. when we encounter a closing bracket, check if the stack is non empty and pop out the top bracket.
3. Compare if the 2 are matching pairs. 
4. If the stack doesn't have any brackets, or if the brackets do not match we return or string ended and the stack is not empty False.
5. if all the brackets match with the opening brackets in the stack, return True

### Code 

```python 
# LifoQueue is a stack in python
from queue import LifoQueue

def isValid(s):
    stack = LifoQueue()

    for bracket in s:
        if bracket in "([{":
            stack.put(bracket)
        else:
            if stack.empty(): return False
            else:
                stack_top = stack.get()
                if (bracket==')' and stack_top=='(') or (bracket==']' and stack_top=='[') or (bracket=='}' and stack_top=='{'):
                    continue
                else:
                    return False
    
    return True if stack.empty() else False


if __name__ == '__main__':
    strings = ["()[{}()]","((([]{}{)))"]
    for s in strings:
        if isValid(s):
            print("True")
        else:
            print("False")
```
- **Time complexity : O(n)**
- **Space complexity : O(n)**

<br>

---
---