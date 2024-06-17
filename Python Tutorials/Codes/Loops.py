# While Loops : a state / block that will execute it's block of code as long as a condition is true
#               used when we do not know the exact number of times we want to repeat a code, just know a limit

import time     # to get the time of a second
name = ''
while len(name) == 0:
    name = input("Enter your name : ")

print("hello ", name)


# For loops : a state/block of code which will execute it's block of code a limited amt of times
#           used when we know the about of times we want to repeat the block
# Syntax : for idx in range( starting idx, ending idx, step) :    // starting is inclusive and end is exclusive
for i in range(10):
    print(i+1)

for i in range(10, 20+1, 2):
    print(i)

# Advantage of for loops is we can iterate throught anything which is iterable : eg String of character :
for i in name:
    print(i)

for seconds in range(5, 0, -1):       # counts down because of step=(-1)
    print(seconds)
    time.sleep(1)       # sleep for 1 second
print("Happy new year !!!")
