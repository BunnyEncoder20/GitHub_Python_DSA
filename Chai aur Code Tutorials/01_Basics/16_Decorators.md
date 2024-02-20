# Decorators in Python 

---

- Decorators are like a pipe through which function has to pass. 
- If there is extra work to be done on the function, when we can , otherwise let it pass as it is
- A basic decorator function will look something like this (this one doesn't do anything fancy, just takes in the function and executes it and sends the results back)
```python 
def debug(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)    
    return wrapper
```

<br>

- learn all about decorators from the below problems and solutions 

---

## Questions to Understand Decorators

### Q1. Timing Function Execution

- write a decorator which measures the time takes by a function to execute 
- **Solution**
```python
import time 

def timer(func):    
    def wrapper (*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        
        print(f"{func.__name__} ran in {round(end-start, 2)} secs")
        return result
    return wrapper

@timer
def exampleFunc(n):
    time.sleep(n)
    
exampleFunc(2)
```
> **NOTE:**
>- when the exampleFunc is called, it doesn't go to the exampleFunc definition but it instead goes to the timer decorator 
>- Which has a wrapper function which executes the exampleFunc() and returns it's results
>- It also calculates the time it'd take to execute the exampleFunc()

---

### Q2. Debugging Function calls 

- Create a decorator to print the function name and the values of it's arguments every time the function is called 
- **Solution**
```python
def debug(func):
    def wrapper(*args, **kwargs):
        args_values = ", ".join(str(arg) for arg in args)
        kwargs_values = ", ".join(f"{key}:{value}" for key,value in kwargs.items())
        print(f"Called {func.__name__} with args: {args_values} and kwargs: {kwargs_values}")
        
        return func(*args, **kwargs)    
    return wrapper

@debug
def hello():
    print("Greeting users")

@debug
def greeting(name, greeting="Hello"):
    print((f"{greeting}, {name}"))
    
hello()
greeting("Varun", "Ola")
```

---

### Q3. Cache return values 

- Decorates can also be used to hold the returned values of the function.
- This is useful when we are making some functions which are querying the DB.
- The function can cache the previous returned values and return them immediately from memory instead of queuing the DB again

<br>

- Implement a decorator which caches the return values of the function, so that when it is called with the same arguments, it returns the cached result instead of re-executing the function again.
- **Solution**
```python
import time 

def cache(func):
    cached_values = {}
    print("Cached: ",cached_values)

    def wrapper(*args,**kwargs):
        if args in cached_values:
            return cached_values[args]
        result = func(*args,**kwargs)
        cached_values[args] = result
        return result
    return wrapper

@cache
def long_running_function(a,b):
    time.sleep(4)   # simulating DB call
    return a+b

print(long_running_function(1,2))
print(long_running_function(1,2))
print(long_running_function(22,33))
```
- Notice the blazing 🔥 fast speed of return of the second function call. 
- Cause we had already sent the same arguments previously, our decorator was able to identify that it was a duplicate call and returned the cached value
- instead of re-executing the function.