# Next Permutation

- Given a List of integers, find the next permutation of the List. 
- The numbers can be rearranged to generate various permutations (arrangements) of the numbers.
- Eg:
```
let given arr = [3,1,2]
All possible Permutations include:
[1,2,3], 
[1,3,2], 
[2,1,3], 
[2,3,1], 
[3,1,2], 
[3,2,1]
As given permutation is at index 4, we return the next index permutation i.e. [3,2,1]
```
---
## Printing all Permutations Recursively - Approach 1

- We gonna need a the number in a list, 2 data structures: stack(for keep track of current combination) and dictionary (to see which numbers we have already taken) and another list to store the resultant permutations.
- **Time complexity will be `O(N!xN)`**
- **Space complexity will be `O(N)+O(N)`**
- Below the Brute Force approach for the same: 

```python
def recursivePermutations(number, stack, mapping, answer):

    # Base case (ending case)
    if len(stack)==len(number):
        answer.append(stack[:]) # stack[:] reacts a deep copy of the stack, so that it doesn't reference the original stack ds 
        return
    
    # if the stack is not filled: (remaining cases)
    for i in range(len(number)):
        if not mapping[number[i]] :
            mapping[number[i]] = True
            stack.append(number[i])
            recursivePermutations(number, stack, mapping, answer)
            
            # After we come back from the recursion end, we remove the number from the ds and map
            stack.pop()
            mapping[number[i]] = False

if __name__ == '__main__':
    number = [3,2,1]
    stack = []
    mapping = {num:False for num in number}
    answer = []
    
    # number.sort()     # can do this to sort the permutations
    recursivePermutations(number,stack,mapping,answer)
    answer.sort()       # or can do this to sort the permutations
    print(answer)
```
- The above approach, the time complexity is `O(N!xN)` and the space complexity is `O(N)+O(N)`. The space complexity is not good and the below approach fixes this. 

---

## Printing all Permutations Recursively - Approach 2

- In this approach, instead of using a stack and dictionary which use extra memory, we swap the numbers within the original DS. 
- The numbers to the left of the index, are fixed and the numbers to the right of the index, are to be swapped. Then for the next recursion, the index is moved more towards the right
- This is done recursively until the index == len(number).
- This way, we do not use any extra space, which improves the space complexity to `O(1)`.

```python
def recursivePermutations(index, number, answer):
    
    # Ending case 
    if index == len(number):
        answer.append(number[:])
        return 
    
    # Other cases 
    for i range(index,len(number)):
        swap(index,i,number) # swap for new combination
        recursivePermutations(index+1, number, answer)
        swap(index,i,number) # un swap to get original number back


def swap(i, j, number):
    temp = number[i]
    number[i] = number[j]
    number[j] = temp

if __name__ == '__main__':
    number = [3,2,1]
    number.sort()
    index = 0
    answer = []
    recursivePermutations(index, number, answer)
    print(answer)
```

---
---
## Brute Force 

- Generate all the possible permutations in sorted order (using **recursion**: if the n is number of elements in the list, then the total possible permutations is **n!** )
- Find the position of the given permutation using Linear Search
- Return the next permutation of the List. (return first permutation if the given permutation is the last permutation in the list)
- **Time complexity: O(N!xN)**  (very bad time complexity)


---

## Better 

- A better solution would be use the inbuilt nextPermutation function available in the STL library of C++.

---

## Optimal