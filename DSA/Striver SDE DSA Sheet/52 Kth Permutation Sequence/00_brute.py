class Solution:
    def getPermutation(self,n:int,k:int)->int:
        numbers = [i for i in range(1,n+1)]
        answer = []

        # Recursive function to find all permutations (swapping approach)
        def fetchPermutations(index,numbers):
            if index == len(numbers):
                answer.append(numbers[:])
                return
            for i in range(index,len(numbers)):
                numbers[i],numbers[index] = numbers[index],numbers[i]
                fetchPermutations(index+1,numbers)
                numbers[i],numbers[index] = numbers[index],numbers[i]
        
        fetchPermutations(0,numbers)
        print(answer)
        return answer[k-1]


if __name__ == "__main__":
    n = 3
    k = 3
    ans = Solution().getPermutation(n, k)
    print("The Kth permutation sequence is", ans)