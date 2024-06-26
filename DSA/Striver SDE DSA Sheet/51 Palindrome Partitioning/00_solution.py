class Solution:

    def partition(self,string):
        ans = []
        path = []

        def partitionHelper(index):
            if index == len(string):
                ans.append(path[:])
                return 
            for i in range(index,len(string)):
                if isPalindrome(index,i,string):
                    path.append(string[index:i+1])
                    partitionHelper(i+1)
                    path.pop()
        
        def isPalindrome(start,end,string):
            while start<=end:
                if string[start]!=string[end]: 
                    return False
                start+=1
                end-=1
            return True

        partitionHelper(0)
        return ans

if __name__ == "__main__":
    s = "aabb"
    obj = Solution()
    ans = obj.partition(s)  
    print("The Palindromic partitions are :-")
    # [['a', 'a', 'b', 'b'], ['a', 'a', 'bb'], ['aa', 'b', 'b'], ['aa', 'bb']]
    print(ans)