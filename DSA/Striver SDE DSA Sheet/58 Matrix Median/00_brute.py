def median(matrix,m,n):
    oneD = []
    for row in range(m):
        for col in range(n):
            oneD.append(matrix[row][col])
    oneD.sort()
    return oneD[(m*n)//2]

if __name__=="__main__":
    matrix = [
        [1, 2, 3, 4, 5],
        [8, 9, 11, 12, 13],
        [21, 23, 25, 27, 29]
    ]
    m = len(matrix)
    n = len(matrix[0])
    ans = median(matrix, m, n)
    print("The median element is:", ans)