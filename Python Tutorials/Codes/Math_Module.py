import math 

pi = 3.14 ;

print("round : ",round(pi));       # rounding off a number to nearest integer 

# to round up a number |> math.ceil() (short for ceiling)
print("math.ceil : ",math.ceil(pi));

# to round a number down |> math.floor
print("math.floor : ",math.floor(pi));

# absolute value  |> math.abs() returns the abs difference (converts negative number into positive)
a = 10
b = 20
print("abs : ",abs(a-b))     # should have been -10 but abs makes it +10

# raising a number to a power |> math.pow( base number , raised to number)
print("2^3",math.pow(2, 3))       # 2^3 = 8
print("pi^2",math.pow(pi, 2))

# find the square root of a number |> math.sqrt()
print("square root of pi : ",math.sqrt(pi)) ;

# find the largest of values : max()
x,y,z = 1,3,2 ;
print("max : ",max(x,y,z))

# find the smallest of values : min()
print("min : ",min(x,y,z))
