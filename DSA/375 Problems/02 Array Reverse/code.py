if __name__ == '__main__':
    arr = [x for x in range(1,11)]
    print("Array :",arr)
    stack = []
    for i in arr:
        stack.append(i)
    
    # NOTE this doesn't assign the element with the new value
    # for element in arr:
    #     element = stack.pop()
    
    # This is the proper way of assign new value in the list : 
    for i in range(0, len(arr)):
        arr[i] = stack.pop()
    
    print("Reserved array: ",arr)
    