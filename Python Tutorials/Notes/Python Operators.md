## Performing Arithmetic Operations using Python

Can you guess what the `//`, `%`, and `**` operators are used for?
- `//` Floor Division operator
- `%`  Modulus operator
- `**` Exponential operator 

As you might expect, operators like `/` and `*` take **precedence** over other operators like `+` and `-` as per mathematical conventions. You can use _parentheses_, i.e. `(` and `)`, to specify the order in which operations are performed.
```
((2 + 5) * (17 - 3)) / (4 ** 3)     # 1.53125
```
Python supports the following arithmetic operators:

| Operator   | Purpose           | Example     | Result    |
|------------|-------------------|-------------|-----------|
| `+`        | Addition          | `2 + 3`     | `5`       |
| `-`        | Subtraction       | `3 - 2`     | `1`       |
| `*`        | Multiplication    | `8 * 12`    | `96`      |
| `/`        | Division          | `100 / 7`   | `14.28..` |
| `//`       | Floor Division    | `100 // 7`  | `14`      |    
| `%`        | Modulus/Remainder | `100 % 7`   | `2`       |
| `**`       | Exponent          | `5 ** 3`    | `125`     |

--- 

## Solving multi-step problems using variables

Let's try solving the following word problem using Python: 

> A grocery store sells a bag of ice for $1.25 and makes a 20% profit. If it sells 500 bags of ice, how much total profit does it make?

We can list out the information provided and gradually convert the word problem into a mathematical expression that can be evaluated using Python. 

*Cost of ice bag ($)* = 1.25

*Profit margin* = 20% = .2

*Profit per bag ($)* = profit margin * cost of ice bag = .2 * 1.25

*No. of bags* = 500

*Total profit* = no. of bags * profit per bag = 500 * (.2 * 1.25)

Thus, the grocery store makes a total profit of $125. While this is a reasonable way to solve a problem, it's not entirely clear by looking at the code cell what the numbers represent. We can give names to each of the numbers by creating Python *variables*.

> **Variables**: While working with a programming language such as Python, information is stored in *variables*. You can think of variables as containers for storing data. The data stored within a variable is called its *value*.
```
cost_of_ice_bag = 1.25
profit_margin = .2
number_of_bags = 500
profit_per_bag = cost_of_ice_bag * profit_margin
total_profit = number_of_bags * profit_per_bag
```
Storing and manipulating data using appropriately named variables is a great way to explain what your code does.

Let's display the result of the word problem using a friendly message. We can do this using the `print` *function*.

> **Functions**: A function is a reusable set of instructions. It takes one or more inputs, performs certain operations, and often returns an output. Python provides many in-built functions like `print` and also allows us to define our own functions.
```
print("The grocery store makes a total profit of $", total_profit)
```
`Ternary Operator` – is a shorter way of writing if else conditions (in one line)
**Syntax :**
```
[on_true] if [expression] else [on_false]
```
Eg of ternary operator 
```
from random import random

a,b=random(),random()
res="a" if a>b else "b"
print(res)
```

Practice HW Question : 
> **EXERCISE**: A travel company wants to fly a plane to the Bahamas. Flying the plane costs $5000. So far, 29 people have signed up for the trip. If the company charges 200 dollars per ticket, what is the profit made by the company? Create variables for each numeric quantity and use appropriate arithmetic operations.
```
flying_cost = 5000
no_of_people = 29
ticket_cost_per_people = 200
earnings = 29*200
profit = earnings-flying_cost
print(f"Profit : {profit}")
profit_percentage = (profit/flying_cost)*100
print(f"Profit percentage : {profit_percentage}%")
```