class Solution:
    def longestCommonPrefix(self, st):
        # Using the dictionary concept
        st.sort()

        length = min(len(st[0]), len(st[-1]))
        prefix = ""
        for i in range(length):
            if st[0][i] != st[-1][i]:
                return prefix
            prefix += st[0][i]
        return prefix


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["flowers", "flow", "flight", "fly"]))
