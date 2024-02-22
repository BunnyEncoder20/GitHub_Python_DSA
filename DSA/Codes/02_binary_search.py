def binary_search(list, target):
    first = 0
    last = len(list) - 1
    
    while first<=last :                 # remember that at the end of the search , we will have first = last 
        midpoint = (first+last)//2      # floor division 
        if list[midpoint] == target :
            return midpoint
        elif list[midpoint]<target : 
            first = midpoint + 1
        elif list[midpoint]>target :
            last = midpoint - 1
    return False

if __name__ == '__main__' : 
    list = [x+1 for x in range(21)]
    target = 5
    res = binary_search(list , target)
    if res : 
        print(f"{target} was found at index:{res}")
    else : 
        print('The element was not found in the list')