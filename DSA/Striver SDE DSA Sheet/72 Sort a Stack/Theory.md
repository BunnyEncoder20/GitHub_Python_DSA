# Sort a Stack (Recursively)

- You’re given a stack consisting of 'N' integers. Your task is to sort this stack in descending order using recursion.
- We can only use the following functions on this stack S.
    - is_empty(S) : Tests whether stack is empty or not.
    - push(S) : Adds a new element to the stack.
    - pop(S) : Removes top element from the stack.
    - top(S) : Returns value of the top element. Note that this function does not remove elements from the stack.
- Note :
    1) Use of any loop constructs like while, for..etc is not allowed. 
    2) The stack may contain duplicate integers.
    3) The stack may contain any integer i.e it may either be negative, positive or zero.


- Exmaples 
```
Sample Input 1:
1
5
5 -2 9 -7 3
Sample Output 1:
9 5 3 -2 -7

Explanation of Sample Input 1:
9 Is the largest element, hence it’s present at the top. Similarly 5>3, 3 > -2 and -7 being the smallest element is present at the last. 
```
```
Sample Input 2:
1
5
-3 14 18 -5 30
Sample Output 2:
30 18 14 -3 -5

Explanation of Sample Input 2:
30 is the largest element, hence it’s present at the top. Similarly, 18>14, 14 > -3 and -5 being the smallest element is present at the last. 
```

<br>

## Recursive Approach 

- We use recursion instead of all the loops

### Algorithm 
1. Recursively empty the stack and keep the popped element stored in a variable. 
2. When the stack is empty, we return 
3. For each stored element, we call the `place()` function which itself is a recursive function
4. `place()` will push an element into the stack when the top is < then the current element or when the stack is empty 
5. Else, it will recursively call itself, popping the top most element and storing it in another variable. 
6. Once the current element is places in the correct place, we can push the stored element back into the stack

### Code 

```python
def sortStack(stack):
    empty_stack(stack)

def empty_stack(stack):
    if len(stack)==0 : return
    else:
        current_element = stack.pop()
        empty_stack(stack)
        place(stack,current_element)
        
def place(stack,curr):
    if len(stack)==0 or stack[-1]<curr:
        stack.append(curr)
    else:
        top = stack.pop()
        place(stack,curr)
        stack.append(top)

if __name__ == "__main__":
    stack = [5 ,-2,9 ,-7 ,3]
    sortStack(stack)
    print(*stack)
```
- **Time complexity : O(n) x O(n) = O(n<sup>2</sup>)**
  - O(n) for the empty_stack()
  - That might have to call place for all elements in the stack, hence another O(n)
- **Space complexity : O(n) + O(n) = O(n)**
  - for recursive depth O(n)
  - holding the stack elements O(n)