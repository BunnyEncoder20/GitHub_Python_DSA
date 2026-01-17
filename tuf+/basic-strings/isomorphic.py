class Solution:
    def isomorphic(self, s, t):
        # Trivial case
        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for i in range(len(s)):
            sLetter = s[i]
            tLetter = t[i]

            if sLetter in sMap and sMap[sLetter] != tLetter:
                return False
            if tLetter in tMap and tMap[tLetter] != sLetter:
                return False

            # assign the letters to each other
            sMap[sLetter] = tLetter
            tMap[tLetter] = sLetter

        return True


if __name__ == "__main__":
    print(Solution().isomorphic("egg", "add"))
    print(Solution().isomorphic("foo", "bar"))
    print(Solution().isomorphic("apple", "bbnbm"))
