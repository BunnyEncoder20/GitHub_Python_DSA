# Type Casting - ability to convert a data type of a value to another data type

x = 1       # int 
y = 2.0     # float
z = "3"     # string

print(x)
print(y)
print(z*3)

x = int(1)       # type casting to int 
y = int(2.0)     # float ==> int 
z = int("3")     # string ==> int

print(type(z))
print(x)
print(y)
print(z*3)

x = float(1)       # int ==> float
y = float(2.0)     # type casting to float
z = float("3")     # string ==> float

print(type(x))
print(x)
print(y)
print(z*3)

x = str(1)       # int ==> str
y = str(2.0)     # type casting to str
z = str("3")     # string ==> str

print(type(y))
print(x)
print(y)
print(z*3)
