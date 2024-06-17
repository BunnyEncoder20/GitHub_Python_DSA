# Scopes and Closures in Python 

- sometimes also called `namespaces` 

<br>

## General overview of scopes

- Most of the times when we are defining variables in python we are directly in the memory.
- In python (unlike many other languages) the block scope is not that restrictive.
- In python we can mostly concerned about `functional` scopes 
- block code like `functions` in python create a block of memory which stores the variables made by the function 
- These `variables` are **not accessible** outside the function (in the `global namespace`)
- **However** the _variables of the parent scope are available inside the function_

```python 
username = 'soma'

def func() : 
    username = 'bunny'
    print(username)

print(username)     # soma
func()              # bunny
```

- If a variable name is not found inside a function **it'll look** for it in it's **parent scope**.
```python 
username = 'soma'

def func() : 
    # username = 'bunny'
    print(username)

print(username)     # soma
func()              # soma
```
<br>

- Generally, we want to **avoid** using global variables in python.
- When we make changes to the functional scoped variables, they have no effect on the global ones : 
```python 
x = 99

def func():
    x = 88

func()
print(x)      # 99
```
- `global` keyword is used to declare that a variable from the global scope is to be used :
```python 
x = 99
def func():
    global x
    x = 88
func()
print(x)      # 88
```
- this will lead to the global variables getting changed directly.
> - **NOTE:** this is **not** a good coding practice cause it compromises the reliability of the program. **Avoid** overwriting global variables.

<br>

## Closures in Python

- Consider the following code : 
```python 
x = 99
def func():
    # x = 88 
    def func2():
        print(x)
    func2()    
func()  
```
- This feature in which the code looks for the variable in the next parent scope is called _climbing_. 

- **NOW** in the same code if we return the entire func2 from func1() ? 
```python 
x = 99
def func1():
    x = 88 
    def func2():
        print(x)
    return func2    # returning the func2 ref from here
ref_func2 = func1() 
ref_func2()         # 88
```
- When we are calling `ref_func2()`, you must ask if only the def of `func2` was passed, how did it know the value of `x` which was defined it's parent scope ?
<br>
- This is called **`Closure`** property in the python (also there in JS but implemented differently)
> - In Python, a **closure** is a _nested function_ that **captures and remembers** the values of variables from the _enclosing (outer) scope_ even after the **outer function** has finished executing. 
> - This allows the **inner function** to access and manipulate **those variables**.

- the `func2` becomes a **CLOSURE** because it is accessing the variable `x` which is there in the scope of the `func1()` function.
- Hence when we are passing the reference of the `func2()` we are not only passing just the definition **but also** all of the variables which are been accessed by it from it's **enclosing scope**
- Not only that but the inner function can also access the params which were passed to the outer function. **Eg:**
```python 
def chaiCoder(num): 
    def actual(x):
        return x**num
    return actual

f = chaiCoder(2)
g = chaiCoder(3)

print(f(3))
print(g(3))
```
