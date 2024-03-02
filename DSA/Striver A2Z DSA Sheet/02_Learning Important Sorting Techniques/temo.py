from typing import List

def merge(arr, start, mid, end):
    left = start
    right = mid+1
    temp = []
    
    while left<=mid and right<=end:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else :
            temp.append(arr[right])
            right+=1
    
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right <= end:
        temp.append(arr[right])
        right+=1

    # if not left == mid:
    #     temp = temp + arr[left:mid+1]
    # if not right == end:
    #     temp = temp + arr[right:end+1]

    # Altering the original arr 
    for i in range(start, end+1):
        arr[i] = temp[i-start]
        

def mergeSort(arr, start, end):
    
    # base case : 
    if start == end: return 
    
    
    # Dividing 
    mid = (start + end) // 2
    mergeSort(arr, start, mid)
    mergeSort(arr, mid+1, end)
    
    # Merging
    merge(arr, start, mid, end)

if __name__ == '__main__':
    # str = "68 151 175 398 382 369 609 940 982 47 522 497 784 126 659 124 931 272 473 794 411 379 717 502 812 548 50 450 358 136 454 980 916 683 637 317 345 676 899 574 69 201 353 604 588 375 810 119 808 589 53 565 888 929 997 540 649 267 504 727 228 529 53 760 984 114 738 471 290 655 165 234 242 239 721 614 775 138 339 972 509 856 901 320 46 539 266 502 888 18"
    str = "45 216 198 795 484 650 590 431 705 316 557 189 652 606 153 829 813 367 658 961"
    arr = str.split(" ")
    arr = [int(x) for x in arr]
    
    mergeSort(arr, 0, len(arr)-1)
    print(arr)