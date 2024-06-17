# nested loop - the 'inner loop' will finish all of it's iterations before finishing one iteration of the 'outer loop'

rows = int(input("number of rows : "))
cols = int(input("number of cols : "))
symbol = input("Enter the Symbol to use : ")

print("Here is a rectangle of ", symbol)
for i in range(rows):
    for j in range(cols):
        # note the ', end="")' prevents the cursor from going to the next line after printing a character
        print(symbol, end="")
    print()
    # this print is for adding a newline for the next row
