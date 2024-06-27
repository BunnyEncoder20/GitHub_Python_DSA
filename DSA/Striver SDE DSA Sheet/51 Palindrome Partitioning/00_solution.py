class Solution:

    def palindrome_partitions(self,string):
        ans = []
        part = []

        def dfs(i):
            if i==len(string):
                ans.append(part[:])
                return
            for j in range(i,len(string)):
                if isPalindrome(i,j,string):
                    part.append(string[i:j+1])
                    dfs(j+1)
                    part.pop()
        
        def isPalindrome(start,end,string):
            while start<=end:
                if string[start] != string[end]:
                    return False
                start+=1
                end-=1
            return True

        dfs(0)
        return ans

if __name__ == "__main__":
    s = "aabb"
    obj = Solution()
    ans = obj.palindrome_partitions(s)  
    print("The Palindromic partitions are :-")
    # [['a', 'a', 'b', 'b'], ['a', 'a', 'bb'], ['aa', 'b', 'b'], ['aa', 'bb']]
    print(ans)