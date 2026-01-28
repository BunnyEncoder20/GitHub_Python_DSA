class Solution:
    def anagramStrings(self, s, t):
        if len(s) != len(t):
            return False

        fpp = {}
        for ch in s:
            fpp[ch] = fpp.get(ch, 0) + 1

        for ch in t:
            fpp[ch] = fpp.get(ch, 0) - 1

        for val in fpp.values():
            if val != 0:
                return False

        return True


if __name__ == "__main__":
    print(Solution().anagramStrings(s="anagram", t="nagaram"))
    print(Solution().anagramStrings(s="dog", t="cat"))
