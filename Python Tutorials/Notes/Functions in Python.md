# Writing Reusable Code using Functions in Python

![](https://i.imgur.com/TvNf5Jp.png)

This tutorial covers the following topics:

- Creating and using functions in Python
- Local variables, return values, and optional arguments
- Reusing functions and using Python library functions
- Exception handling using `try`-`except` blocks
- Documenting functions using docstrings

## Creating and using functions

A function is a reusable set of instructions that takes one or more inputs, performs some operations, and often returns an output. Python contains many in-built functions like `print`, `len`, etc., and provides the ability to define new ones.

You can define a new function using the `def` keyword.
```
def say_hello():
    print('Hello there!')
    print('How are you?')
```
Note the round brackets or parentheses `()` and colon `:` after the function's name. Both are essential parts of the syntax. The function's *body* contains an indented block of statements. The statements inside a function's body are not executed when the function is defined. To execute the statements, we need to `call` or `invoke` the function.
```
say_hello()     
#Hello there! 
#How are you?
```

### Function arguments

Functions can accept zero or more values as *inputs* (also knows as *arguments* or *parameters*). Arguments help us write flexible functions that can perform the same operations on different values. Further, functions can return a result that can be stored in a variable or used in other expressions.

Here's a function that filters out the even numbers from a list and returns a new list using the `return` keyword.
```
def filter_even(number_list):
    result_list = []
    for number in number_list:
        if number % 2 == 0:
            result_list.append(number)
    return result_list

even_list = filter_even([1, 2, 3, 4, 5, 6, 7])
print(even_list)            # [2, 4, 6]
```

## Writing great functions in Python

As a programmer, you will spend most of your time writing and using functions. Python offers many features to make your functions powerful and flexible. Let's explore some of these by solving a problem:

> Radha is planning to buy a house that costs `$1,260,000`. She considering two options to finance her purchase:
>
> * Option 1: Make an immediate down payment of `$300,000`, and take loan 8-year loan with an interest rate of 10% (compounded monthly) for the remaining amount.
> * Option 2: Take a 10-year loan with an interest rate of 8% (compounded monthly) for the entire amount.
>
> Both these loans have to be paid back in equal monthly installments (EMIs). Which loan has a lower EMI among the two?


Since we need to compare the EMIs for two loan options, defining a function to calculate the EMI for a loan would be a great idea.  The inputs to the function would be cost of the house, the down payment, duration of the loan, rate of interest etc. We'll build this function step by step.

First, let's write a simple function that calculates the EMI on the entire cost of the house, assuming that the loan must be paid back in one year, and there is no interest or down payment.
```
def loan_emi(amount):
    emi = amount / 12
    print('The EMI is ${}'.format(emi))

loan_emi(1260000)   # The EMI is $105000.0
```
### Local variables and scope

Let's add a second argument to account for the duration of the loan in months.
```
def loan_emi(amount, duration):
    emi = amount / duration
    print('The EMI is ${}'.format(emi))
```
Note that the variable `emi` defined inside the function is not accessible outside. The same is true for the parameters `amount` and `duration`. These are all *local variables* that lie within the *scope* of the function.

> **Scope**: Scope refers to the region within the code where a particular variable is visible. Every function (or class definition) defines a scope within Python. Variables defined in this scope are called *local variables*. Variables that are available everywhere are called *global variables*. Scope rules allow you to use the same variable names in different functions without sharing values from one to the other. 

We can now compare a 8-year loan vs. a 10-year loan (assuming no down payment or interest).

```
loan_emi(1260000, 8*12)     # The EMI is $13125.0
loan_emi(1260000, 10*12)    # The EMI is $10500.0
```
### Return values

As you might expect, the EMI for the 6-year loan is higher compared to the 10-year loan. Right now, we're printing out the result. It would be better to return it and store the results in variables for easier comparison. We can do this using the `return` statement
```
def loan_emi(amount, duration):
    emi = amount / duration
    return emi

emi1 = loan_emi(1260000, 8*12)
emi2 = loan_emi(1260000, 10*12)
```
### Optional arguments

Next, let's add another argument to account for the immediate down payment. We'll make this an *optional argument* with a default value of 0.
```
def loan_emi(amount, duration, down_payment=0):
    loan_amount = amount - down_payment
    emi = loan_amount / duration
    return emi

emi1 = loan_emi(1260000, 8*12, 3e5)
print(emi1)         # 10000.0
emi2 = loan_emi(1260000, 10*12)
print(emi2)         # 10500.0
```
Next, let's add the interest calculation into the function. Here's the formula used to calculate the EMI for a loan:

<img src="https://i.imgur.com/iKujHGK.png" style="width:240px">

where:

* `P` is the loan amount (principal)
* `n` is the no. of months
* `r` is the rate of interest per month

```
def loan_emi(amount, duration, rate, down_payment=0):
    loan_amount = amount - down_payment
    emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    return emi
```
Note that while defining the function, required arguments like `cost`, `duration` and `rate` must appear before optional arguments like `down_payment`.

Let's calculate the EMI for Option 1
```
loan_emi(1260000, 10*12, 0.08/12)   # 15287.276888775077
```


### Named arguments

Invoking a function with many arguments can often get confusing and is prone to human errors. Python provides the option of invoking functions with *named* arguments for better clarity. You can also split function invocation into multiple lines.
```
emi1 = loan_emi(
    amount=1260000, 
    duration=8*12, 
    rate=0.1/12, 
    down_payment=3e5
)
print(emi1)        # 14567.19753389219

emi2 = loan_emi(amount=1260000, duration=10*12, rate=0.08/12)
print(emi2)        # 15287.276888775077
```

### Modules and library functions

We can already see that the EMI for Option 1 is lower than the EMI for Option 2. However, it would be nice to round up the amount to full dollars, rather than showing digits after the decimal. To achieve this, we might want to write a function that can take a number and round it up to the next integer (e.g., 1.2 is rounded up to 2). That would be a great exercise to try out!

However, since rounding numbers is a fairly common operation, Python provides a function for it (along with thousands of other functions) as part of the [Python Standard Library](https://docs.python.org/3/library/). Functions are organized into `modules` that need to be imported to use the functions they contain. 

> **Modules**: Modules are files containing Python code (variables, functions, classes, etc.). They provide a way of organizing the code for large Python projects into files and folders. The key benefit of using modules is _namespaces_: you must import the module to use its functions within a Python script or notebook. Namespaces provide encapsulation and avoid naming conflicts between your code and a module or across modules.

We can use the `ceil` function (short for *ceiling*) from the `math` module to round up numbers. Let's import the module and use it to round up the number `1.2`. 
```
import math
help(math.ceil)     # for seeing what the module is about
math.ceil(1.2)      # gives 2
```

Let's now use the `math.ceil` function within the `home_loan_emi` function to round up the EMI amount. 

> Using functions to build other functions is a great way to reuse code and implement complex business logic while still keeping the code small, understandable, and manageable. Ideally, a function should do one thing and one thing only. If you find yourself writing a function that does too many things, consider splitting it into multiple smaller, independent functions. As a rule of thumb, try to limit your functions to 10 lines of code or less. Good programmers always write short, simple, and readable functions.
```
import math

def loan_emi(amount, duration, rate, down_payment=0):
    loan_amount = amount - down_payment
    emi = loan_amount * rate * ((1+rate)**duration) / (((1+rate)**duration)-1)
    emi = math.ceil(emi)        
    return emi

emi1 = loan_emi(
    amount=1260000, 
    duration=8*12, 
    rate=0.1/12, 
    down_payment=3e5
)

emi2 = loan_emi(amount=1260000, duration=10*12, rate=0.08/12)      

if emi1 < emi2:
    print("Option 1 has the lower EMI: ${}".format(emi1))
else:
    print("Option 2 has the lower EMI: ${}".format(emi2))

# Option 1 has the lower EMI: $14568
```
### Reusing and improving functions 

Now we know for sure that "Option 1" has the lower EMI among the two options. But what's even better is that we now have a handy function `loan_emi` that we can use to solve many other similar problems with just a few lines of code. Let's try it with a couple more questions.

> **Q:** Shaun is currently paying back a home loan for a house he bought a few years ago. The cost of the house was `$800,000`. Shaun made a down payment of `25%` of the price. He financed the remaining amount using a 6-year loan with an interest rate of `7%` per annum (compounded monthly). Shaun is now buying a car worth `$60,000`, which he is planning to finance using a 1-year loan with an interest rate of `12%` per annum. Both loans are paid back in EMIs. What is the total monthly payment Shaun makes towards loan repayment?

This question is now straightforward to solve, using the `loan_emi` function we've already defined.
```
import math

def calc_EMI(amt, rate, time, downpayment=0) : 
    amt2pay = amt - downpayment
    emi = (amt2pay * rate * ((1+rate)**time)) / (((1+rate)**time)-1)
    return math.ceil(emi)

house_emi = calc_EMI(800000,.07/12,6*12,800000*.25)
car_emi = calc_EMI(60000,.12/12,1*12)

print("Total Monthly EMI payments = ",(house_emi+car_emi))          # 15561
```

### Exceptions and `try`-`except`

> Q: If you borrow `$100,000` using a 10-year loan with an interest rate of 9% per annum, what is the total amount you end up paying as interest?

One way to solve this problem is to compare the EMIs for two loans: one with the given rate of interest and another with a 0% rate of interest. The total interest paid is then simply the sum of monthly differences over the duration of the loan.