from math import sqrt
import collections
def hash(arr:list)->list:
    hashed = {}
    for char in arr:
        if char in hashed:
            hashed[char]+=1
        else :
            hashed[char] = 1
    return hashed

if __name__ == '__main__':
    hashedArray = hash(['a','g','a','d','r','y'])
    for key in hashedArray:
        print(f"{key} : {hashedArray[key]}")
    