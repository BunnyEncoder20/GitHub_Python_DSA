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