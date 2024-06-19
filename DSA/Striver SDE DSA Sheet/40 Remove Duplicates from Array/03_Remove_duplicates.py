# Brute Force approach
def check_duplicates(arr):
    uniques = set()
    for num in arr:
        uniques.add(num)
    return len(uniques)

def optimal_check_duplicates(arr):
    n = len(arr)
    i = 0
    for j in range(1,n):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i+=1
    return i+1

if __name__ == '__main__':
    arr = [1,1,2,2,2,3,3]
    print(check_duplicates(arr))
    print(optimal_check_duplicates(arr))