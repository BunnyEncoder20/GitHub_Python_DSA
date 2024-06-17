# # Recursively printing all permutations of a number / string (Approach 2 - Swapping)
# Time complexity : O(n! x n)
# Space Complexity : O(1)
# No extra memory required

def recursivePermutations(index,number,answer):

    # Ending case 
    if (index == len(number)):
        # the combination is completed and will now add to answer
        answer.append(number[:])
        return

    # remaining cases 
    for i in range(index,len(number)):
        swap(i, index, number)                          # function to swap the numbers 
        recursivePermutations(index+1, number, answer)  # calling next permutations
        swap(i, index, number)
        

def swap(i, j, number):
    temp = number[i]
    number[i] = number[j]
    number[j] = temp

if __name__ == '__main__':
    number = [3,1,2]
    answer = []
    index = 0
    number.sort()
    recursivePermutations(index,number,answer)

    print("Answer:\n",answer)