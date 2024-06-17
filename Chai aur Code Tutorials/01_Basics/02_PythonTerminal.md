# Python Terminal 
---

- The python terminal can be accessed by typing `python` in the command line.
- This will enable the python shell.
- This shell is used to quickly check what a line / command of python code does.
- It can be exit by typing `exit() + ⏎` or `ctrl+z` and `⏎`
Common Commands seen : 
```
import os
os.system('cls')
os.getcwd()

for c in "Soma":
...     print(c)
```
```
import sys
sys.platform
```
- Similar to these imports we can also import files from our local dir:
```
import say_hello
say_hello.sayHello("Bunny")
```
- We can access all the functions and attributes of the python script using `filename.function()` or `filename.attribute` syntax.
- if we were to make any new changes to the imported file we will see that those changes are not seen in the terminal. 
```
def sayHello(name):
    print("Hello "+name)

# adding new variables/attributes
friend1 = "Soma"
friend2 = "Hoods"
friend3 = "Bunnu"
```
- We must re import or reload the file again into the shell to get the latest changes.
- This can be done using the reload function from the importlib
```
from importlib import reload
reload(say_hello)
```
- Now the new changes are reflected onto the shell import.