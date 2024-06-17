# Recursively printing all permutations of a number / string
# Time complexity : O(n! x n)
# Space Complexity : O(n) + O(n)
# Brute , not Optimal cause of extra data structure memory requirements.

def recursivePermutations(number, stack, mapping, answer):

    # Base case (ending case)
    if len(stack)==len(number):
        answer.append(stack[:]) # stack[:] creates a deep copy of the stack, so that it doesn't reference the original stack ds 
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