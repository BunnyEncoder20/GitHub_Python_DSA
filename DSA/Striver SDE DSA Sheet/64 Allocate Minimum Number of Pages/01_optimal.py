def findPages(arr, n, m):
    if m>n :    # book allocation impossible 
        return -1
        
    low = max(arr)
    high = sum(arr)
    while low<=high:
        mid = (low+high)//2
        no_students = count_students(arr,mid)
        if no_students>m : 
            low = mid+1
        else: 
            high = mid-1
    return low

def count_students(arr,max_pages):
    count = 1
    pages_with_student = 0
    for i in range(len(arr)):
        if pages_with_student+arr[i] <= max_pages:
            pages_with_student += arr[i]
        else:
            count+=1
            pages_with_student = arr[i]
    return count

if __name__ =="__main__":
    arr = [25, 46, 28, 49, 24]
    n = 5
    m = 4
    ans = findPages(arr, n, m)
    print("The answer is:", ans)