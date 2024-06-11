def lengthOfLongestSubstring(str):
    last_occurance = {}

    left,right = 0,0
    n = len(str)
    maxlength = 0

    while right<n:
        if str[right] in last_occurance:
            # Move the left pointer to the right of the last occurrence of the current character
            left = max(last_occurance[str[right]]+1, left)
        
        # Update the last occurance of the current character
        last_occurance[str[right]] = right

        # Update the max length 
        maxlength = max(maxlength,right-left+1)

        # move the right pointer 
        right += 1

    return maxlength 


if __name__ == "__main__":
    strList = ["abcabcbb","bbbbb","pwwkew"]
    for str in strList:
        print(lengthOfLongestSubstring(str))