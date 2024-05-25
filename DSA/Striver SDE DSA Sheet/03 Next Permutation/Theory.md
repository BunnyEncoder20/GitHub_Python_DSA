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
## Printing all Permutations Recursively

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