# Code to generate all the sub strings of a given string 
# Time Complexity : O(n^2)
# Space Complexity : O(1)

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
