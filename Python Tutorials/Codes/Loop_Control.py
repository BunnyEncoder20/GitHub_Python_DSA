# Loop Control statements :
# 1. break : used to terminate the loop entirely and exit the loop
# 2. continue : skips the current iteration and goes to the next iteration of the loop
# 3. pass : does nothing only acts a placeholder (won't use it much)

while True:
    name = input("Enter your name : ")
    if len(name) != 0:
        break

phone_number = "123-456-789"
# to print this number in the terminal without dashes :
for i in phone_number:
    if i == "-":
        continue
    print(i, end='')

for i in range(11, 21):
    if (i == 13):   # cause we don't want bad luck
        pass
    else:
        print(i)
