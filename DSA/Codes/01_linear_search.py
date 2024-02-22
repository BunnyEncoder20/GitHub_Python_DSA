def linear_search(list , target):
    for index,num in enumerate(list) :
        if num == target :
            return index
    return False

if __name__ == '__main__' : 
    list = [1,4,2,3,5,6,8,7,9.10]
    target = 12
    result = linear_search(list , target)
    if result : 
        print(f"{target} was found at index:{result}")
    else :
        print("The element was not found in the list")