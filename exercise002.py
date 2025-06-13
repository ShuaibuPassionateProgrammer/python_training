# A simple python program that prints the current date, to do that, you are to import the datetime module
from datetime import datetime
import math

print(math.sqrt(4))

print(datetime.now())

def countries(name):
    return "I wish i was born in " + name

print(countries("South Korea"))

def states(name):
    return "I am from " + name

print(states("Soul"))

def numbers(number):
    print(number)


numbers(1)
numbers(2)
numbers(3)

def print_age(age):
    return "I wish i could been a riched person since when i was " + str(age) + " years old"

print(print_age(10))

def celsius_to_fahrenheight(celcius):
    farenheight = (celcius * 9 / 5) + 32
    return farenheight

tempInput = float(input("Enter temperature: "))
output = celsius_to_fahrenheight(tempInput)
print(f"{tempInput} °C is {output} °F" )
