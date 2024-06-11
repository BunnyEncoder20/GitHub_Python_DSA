# Longest Sub String without Repeating Characters 

- Given a string s, find the length of the longest substring without repeating characters.
- Examples : 

**Example 1:**
> Input: s = "abcabcbb"
> Output: 3
> Explanation: The answer is "abc", with the length of 3.

**Example 2:**
> Input: s = "bbbbb"
> Output: 1
> Explanation: The answer is "b", with the length of 1.

**Example 3:**
> Input: s = "pwwkew"
> Output: 3
> Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

<br>

## Brute Force Approach 

- Generate all the sub strings
- check if all the characters are unique
- if unique, update the longest length

### Generating all the substrings of a string 

```python 
def printSubStrings(str):
    n = len(str)

    # first loop for selecting starting point
    for i in range(n):
        subString = ""

        # second loop for genreating that starting point's sub strings
        for j in range(i,n):
            subString += str[j] 
            print(subString)

if __name__ == "__main__":
    str = "abcd"
    printSubStrings(str)
```
- **Time Complexity : O(n<sup>2</sup>)**
- **Space Complexity : O(1)**

### Code 

```python 
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
```

<br>

## Better Approach

- [Watch it here](https://youtu.be/qtVh-XEpsJo?si=VqLuu5n0J96jqZoG&t=122)
- 2 pointer 

### Code

```python 
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
```
- **Time Complexity : O(2n)**
- **Space Complexity : O(n)**

<br>

## Optimal Approach 

- Complexity gets better by reducing the travel time of the left pointer 

### Code 

```python 
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
```
- **Time complexity : O(n)**
- **Space complexity : O(n)**