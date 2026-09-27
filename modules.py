import math
num = int(input("enter a number: "))

result = math.sqrt(num)      #module.function_name 
print(f"the square root of {num} is {result}")

# calculate the arra of circle 

radius = int(input("enter the radius of circle:"))
area_of_circle = math.pi * radius ** 2

print(f"the area of circle with radius {radius} is {area_of_circle}")


# randit

from random import randint

value = randint(1 , 100)
print(value)


import datetime as dt
t = dt.time(8 , 20 , 30)

print(t)
