def lengthOfLongestSubstring(str):
    n = len(str)
    maxLength = float('-inf')
    hashset = set()
    left = 0

    for right in range(n):
        if str[right] in hashset:
            while left<right and str[right] in hashset :
                hashset.remove(str[left])
                left+=1
        hashset.add(str[right])
        maxLength = max(maxLength, right-left+1)
    return maxLength

if __name__ == "__main__":
    strList = ["abcabcbb","bbbbb","pwwkew"]
    for str in strList:
        print(lengthOfLongestSubstring(str))