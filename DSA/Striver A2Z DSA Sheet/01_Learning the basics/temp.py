def symmetry(n: int):
    
    for i in range(n*2-1):
        for j in range(n*2-1):
            top_distance = i
            bottom_distance = (n*2-2)-i
            left_distance = j
            right_distance = (n*2-2)-j
            print(n - min(top_distance, bottom_distance, left_distance, right_distance), end=" ")
        print()
if __name__ == '__main__':
    symmetry(4)