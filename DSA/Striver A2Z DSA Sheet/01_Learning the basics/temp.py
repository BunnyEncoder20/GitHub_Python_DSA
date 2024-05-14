def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print(f"{i+1}",end=" ")
        print()

pattern(5)