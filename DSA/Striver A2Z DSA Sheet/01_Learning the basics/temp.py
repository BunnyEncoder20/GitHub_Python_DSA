from typing import List
from collections import defaultdict

def getFrequencies(v: List[int]) -> List[int]: 
    hashmap = defaultdict(int)
    maxmin = [0,0]
    maxi,mini = 0,1000 
    
    for num in v:
        hashmap[num]+=1
    
    for key,value in hashmap.items():
        if value>maxi:
            maxi=value
            maxmin[0]=key
        elif value==maxi:
            if key<maxmin[0]: maxmin[0]=key 
        
        if value == mini:
            if key<maxmin[1]: maxmin[1]=key
        elif value<mini:
            mini=value
            maxmin[1]=key
    return maxmin

if __name__ == '__main__':
    print(getFrequencies([1, 2, 3, 1, 1, 4]))
    print(getFrequencies([10, 10,10, 3, 3, 3]))