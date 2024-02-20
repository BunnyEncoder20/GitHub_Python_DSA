# Basic Concepts for Project

### `enumerate()` Function
- `.enumerate()` is used to let back index and value of a iterable (kidna like the key,value of a dictionary)
>- The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
- Eg:
```python 
>>> x = ('batman','madara','sukuna')
>>> y = enumerate(x)
>>> y
<enumerate object at 0x000001CA7F9256C0>
>>> list(y)         
[(0, 'batman'), (1, 'madara'), (2, 'sukuna')]
```

---

### Opening file in different modes

- we can open files in python different modes by specifying the mode in the `.open()` function 
- By default it opens in 'r' which is the `read` mode
- **Eg:**
```python
file_ref = open('test.py' , 'w')
```
- in the exmaple, we are opening the file in `w` which is the `write` mode. 
- **NOTE:** 'w' creates the file if the file is note present in directory 
- The various modes include:
    - `r` : Open a file in reading mode (default)
    - `w` : Open a file in writing mode
    - `x` : Open a file for exclusive creation 
    - `a` : Open a file in appending mode (adds content at the end of the file)
    - `t` : Open a file in text mode (default)
    - `b` : Open a file in binary mode
    - `+` : Open a file in both read and write mode

--- 

### Proper file handling in Python

- `try`, `except` and `finally` is used for error handling in python.
- Remember that finally will run regardless of errors or not 
- Below is the proper way of handling files in python (method 1) 
```python
file = open('filename.txt`,'w')

try:
    file.write('Hello soma')
except ValueError:
    print("There was a error")
finally :
    file.close()
```
- Below is another way of proper handling of files in python using the `with` keyword
```python
with open('filename.txt','w') as file :
    file.write("Hello Senpai")
```
- **Note** the indentation which comes with this keyword. 
- `with` keyword takes care of closing the file for us, so we don't need to do it ourselves 
- So it just a simpler and better way of handling files 