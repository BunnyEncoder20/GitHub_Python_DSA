def lengthOfLongestSubstring(str):
    n = len(str)
    maxLength = -1

    for i in range(n):
        hashset = {}
        for j in range(i,n):
            if str[j] in hashset:
                length = j-i 
                maxLength = max(length,maxLength)
                break 
            hashset[str[j]] = True
    return maxLength


if __name__ == "__main__":
    strList = ["abcabcbb","bbbbb","pwwkew"]
    for str in strList:
        print(lengthOfLongestSubstring(str))