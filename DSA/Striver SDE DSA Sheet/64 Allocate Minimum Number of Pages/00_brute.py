def findPages(arr, n, m):
    low = max(arr)
    high = sum(arr)
    
    for pages in range(low,high+1):
        count_students = allocate_books(arr,pages)
        if count_students == m:
            return pages

def allocate_books(arr,max_pages):
    students = 1
    pages_with_student = 0
    for i in range(len(arr)):
        if pages_with_student + arr[i] <= max_pages:
            pages_with_student+=arr[i]
        else:
            students+=1
            pages_with_student = arr[i]
    return students


if __name__ =="__main__":
    arr = [25, 46, 28, 49, 24]
    n = 5
    m = 4
    ans = findPages(arr, n, m)
    print("The answer is:", ans)