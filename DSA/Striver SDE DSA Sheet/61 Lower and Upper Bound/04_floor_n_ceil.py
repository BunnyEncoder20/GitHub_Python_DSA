if __name__ == "__main__":
    arr = [10,20,30,40,50]
    xs = [25]
    for x in xs:
        floor,ceil = calc_floor_and_ceil(arr,len(arr),x)
        print("Floor value is : ",floor)
        print("Ceil value is : ",ceil)