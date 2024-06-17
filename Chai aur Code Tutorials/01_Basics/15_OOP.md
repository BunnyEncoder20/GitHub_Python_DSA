# Object Oriented Programming in Python

- made more difficult than it needs to be 
- Basically a coding philosophy of using classes and objects

<br>

 Learn all about OOP by solving the following questions

 ---
 ---

 ## Questions Section

---

### Q1. Basic Class and object

- create a car `class` with `attributes` like brand and model. Then create a instance of this class.
- `class` keyword is used for defining a class in python 
- `self` keyword is used to access the attributes and methods of the class instance.
- `self` is like the `this` keyword in **JS**.

- **Solution**
```python 
class Car : 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    brand = None
    model = None
    
    
if __name__ == "__main__":
    Car_instance1 = Car('Lamborgini','Huracan')
    Car_instance2 = Car('Pagani','Roadster BC')

    print(Car_instance1.brand)  # Lamborgini
    print(Car_instance1.model)  # Huracan

    print(Car_instance2.brand)  # Pagani
    print(Car_instance2.model)  # Roadster BC
```
- we access the properties (like attributes / functions) of a class using the `.` operator.
- **`__init__`** function name is used to _def_ the **constructor** of the class in python.
- we usually define the class in another file and import it when the class is required 

---

### Q2. Class methods and self 

- Add a method to the car class which displays it's full name (brand and model)
- **Solution**
```python 
class Car : 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    brand = None
    model = None
    
    def get_fullname(self):
        return f"{self.brand} {self.model}"
    
    
if __name__ == "__main__":
    Car_instance1 = Car('Lamborgini','Huracan')
    Car_instance2 = Car('Pagani','Roadster BC')

    print(Car_instance1.get_fullname())  # Lamborgini Huracan
    print(Car_instance2.get_fullname())  # Pagani Roadster BC
```

---

### Q3. Class Inheritance

- Create a electric car class that inherits from car class and has a additional attribute battery_size
- **Solution**
```python 
class Car : 
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    brand = None
    model = None
    
    def get_fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    battery_size = None

myCar1 = Car('Lamborgini','Huracan')
myCar2 = ElectricCar("Tesla","Model S","85kWh")

print(myCar2.get_fullname())
print(myCar2.battery_size)
```
- `super()` keyword is used to access the attributes and functions of the parent class.
- In the constructor of the ElectricCar class, we access the **`__init__()`** of the Car (parent) class and send it the attributes it needs to assign.

---

### Q4. Encapsulation 

- Modify the car class to encapsulate the brand attribute, making it private and provide a getter method for it.
- **Solution**
```python 
class Car : 
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    __brand = None
    model = None
    
    def get_brand(self):
        return self.__brand
    
    def get_fullname(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    battery_size = None

myCar1 = Car('Lamborgini','Huracan')
myCar2 = ElectricCar("Tesla","Model S","85kWh")

print(myCar2.get_fullname())    # Tesla Model S
print(myCar2.model)             # Model S
print(myCar2.__brand)           # Will cause an error
```
- `__` before a attribute name (eg: __brand) is used to make the attribute private in python
- if we try to access the private attribute even using the exact same name (__attribute) we will get the following error : 
```
Traceback (most recent call last):
  File "C:\Users\gener\Coding\GitHub Python DSA\Chai aur Code Tutorials\01_Basics\test.py", line 25, in <module>
    print(myCar2.__brand)
          ^^^^^^^^^^^^^^
AttributeError: 'ElectricCar' object has no attribute '__brand'. 
```
- making a attribute **private** makes it inaccessible from outside the class. Only the methods/members of the class can access that variable now. 

---

### Q5. Polymorphism 

- **polymorphism** basically is function overloading but between same name methods in different classes. 
- polymorphism = same name methods but different behaviors/functionality

<br>

- Demonstrate polymorphism by defining a method fuel type in both Car and ElectricCar classes, but with different behaviors 
- **Solution**
```python
class Car : 
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
    __brand = None
    model = None
    
    def get_brand(self):
        return self.__brand
    
    def get_fullname(self):
        return f"{self.__brand} {self.model}"

    def fueltype(self):
        return "Petrol & Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    battery_size = None
    
    def fueltype(self):
        return "electric charging"

myCar1 = Car('Lamborgini','Huracan')
myCar2 = ElectricCar("Tesla","Model S","85kWh")

print(myCar1.fueltype())
print(myCar2.fueltype())
```


---

### Q6. Class Variables 

- Class variables that are shared among all instances of a class can be created by using the the **Class name** to access them during creation
- Similarly outside the class either the _Class name or an instance_ of the class cna be used to access that variable
<br>

- add a class variable to class Car which keep track of numbers of cars made.
- **Solution**
```python 
class Car : 
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total += 1
    __brand = None
    model = None
    total = 0
    
    def get_brand(self):
        return self.__brand
    
    def get_fullname(self):
        return f"{self.__brand} {self.model}"

    def fueltype(self):
        return "Petrol & Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    battery_size = None
    
    def fueltype(self):
        return "electric charging"

Car('Lamborgini','Huracan')
ElectricCar("Tesla","Model S","85kWh")

print(Car.total)
```

---

### Q7. Static Methods (decorators)

- **static methods** is a method that belongs to the class and not to an instance of the class. 
- `@staticmethod` keyword is written above a static function to tell the class that it is a static method
- We do not have to pass in the `self` ref here as this function is **not accessible** by any class instance.
- we'll have to access it using the **Class name** itself
- These kinda **`@methods`**  are aka decorators in python. They are used enhance the functionality of the class.

- make a function to return a general description of a car 
- **Solution**
```python 
class Car : 
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total += 1
    __brand = None
    model = None
    total = 0
    
    def get_brand(self):
        return self.__brand
    
    def get_fullname(self):
        return f"{self.__brand} {self.model}"

    def fueltype(self):
        return "Petrol & Diesel"
    
    @staticmethod
    def general_info():
        return "Cars are amazing machine with engine....they are just means of transport "

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    battery_size = None
    
    def fueltype(self):
        return "electric charging"

my_car1 = Car('Lamborgini','Huracan')
my_car2 = ElectricCar("Tesla","Model S","85kWh")

print(Car.general_info())
```

---

### 8. Property Decorators 

- property decorators defined by putting `@property` in front of a function converts it into a non changeable property of the class
- we can pair this up with private variable to close all access to that specific attribute

<br>

- user a property decorator in class Cars and make model attribute read-only
- **Solution**
```python 
class Car : 
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total += 1
    __brand = None
    __model = None
    total = 0
    
    def get_brand(self):
        return self.__brand
    
    def get_fullname(self):
        return f"{self.__brand} {self.__model}"

    @property
    def model(self):
        return self.__model
    

my_car1 = Car('Lamborgini','Huracan')


print(my_car1.model)        # Huracan
print(my_car1.model())      # Error
```
The 2nd print statement will raise the following exception:
```
Traceback (most recent call last):
  File "C:\Users\gener\Coding\GitHub Python DSA\Chai aur Code Tutorials\01_Basics\test.py", line 25, in <module>
    print(my_car1.model())
          ^^^^^^^^^^^^^^^
TypeError: 'str' object is not callable
```
- **NOTE:** that the method name is the same as the private attribute
- Even though model looks like a function, you cannot access it like one as it is has a `@property` decorator.

---

### 9. Class inheritance and isinstance function

- Demonstrate the use of `isintance()` to check if my_tesla is an instance of class Car and ElectricCar.
- **Solution**
```python 
class Car : 
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total += 1
    __brand = None
    __model = None
    total = 0
    
    def get_brand(self):
        return self.__brand
    
    def get_fullname(self):
        return f"{self.__brand} {self.__model}"

    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    battery_size = None

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(isinstance(my_tesla, Car))            # True
print(isinstance(my_tesla, ElectricCar))    # true
```

---

### 10. Multiple inheritance


- Create 2 classes Battery and Engine, and let ElectricCar class inherit from both, demonstrating multiple class inheritance 
- **Solution**
```python 
class Car : 
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    __brand = None
    __model = None
    
    def get_fullname(self):
        return f"{self.__brand} {self.__model}"

class Battery:
    def battery_func(self):
        return "this is from battery class"

class Engine:
    def engine_func(self):
        return "this is from engine class"

class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    battery_size = None

my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
print(my_tesla.battery_func())
print(my_tesla.engine_func())
print(my_tesla.get_fullname())
```