#!/bin/python3

#Print String
print("String and things:")
print("Hello, world!")
print("This is"+" a string\n")

#Math
print("Math time:")
print(50 + 50) #add
print(50 - 50) #substract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo
print(50 // 6) #number without leftovers
print("\n")

#Variables & Methods
print("Fun with variables and methods:")
quote = "All is fair in love and war"
print(len(quote)) #length
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #capitalcase
print("\n")

name = "Health"
age = 29 #int int(29)
gpa = 3.7 #float float(3.7)

print(int(age))
print(int(29.9)) #does not round
print("My name is "+name+" and I am "+str(age)+" years old")
age += 1
print(age)

birthday = 1
age += birthday
print(age)

#function
print("Now , some functions: ")
def who_am_i():
	name = "Bank"
	age = 22
	print("My name is "+name+"  and I am "+str(age)+" years old")
who_am_i()

#adding in parameters
def add_one_hundred(num):
	print(num + 100)
add_one_hundred(10000)

#add multiple parameters
def add(x,y):
	print(x+y)
add(7,7)

#Using return
def multiply(x,y):
	return x*y
print(multiply(7,6))

def square_root(x):
	return x ** 0.5
print(square_root(64))