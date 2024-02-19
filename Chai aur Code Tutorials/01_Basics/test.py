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

