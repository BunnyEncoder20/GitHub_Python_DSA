class Solution:
    def isomorphic(self, s, t):
        sMap = tMap = {chr(i): 0 for i in range(97, 123)}  # a-z


if __name__ == "__main__":
    print(Solution().isomorphic("egg", "add"))
    print(Solution().isomorphic("foo", "bar"))
    print(Solution().isomorphic("apple", "bbnbm"))
