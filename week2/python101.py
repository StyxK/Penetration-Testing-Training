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

#Boolean expression (True or False) Must Be Capitalize!
print("Boolean Expression : ")
bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9
bool5 = "True"
print(bool1,bool2,bool3,bool4)
print(type(bool1))
print(type(bool5))

#Relational and Boolean Operations
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal = 7 >= 7
less_than_equal = 7<= 7
print(greater_than,less_than,greater_than_equal,less_than_equal)

test_and = (7>5) and (5<7)
test_or = (7>5) or (5<7)
test_not = not True
print(test_and,test_or,test_not)

#Condition statement
print("Condotion Statement")
def soda(money):
	if money >= 2:
		return "You've got yourself a soda!"
	else:
		return "No soda for you!"
print(soda(3))
print(soda(1))
def alcohol(age,money):
	if (age >= 20) and (money >= 5):
		return "You've got tripsy"
	elif (age < 20) and (money >= 5):
		return "Nice try kid"
	elif (age >= 20) and (money < 5):
		return "Come back with money"
	else:
		return "You too poor and too young"
print(alcohol(20,5))
print(alcohol(19,5))
print(alcohol(20,4))
print(alcohol(19,4))

#Lists
print("Lists have brackets : ")
movies = ["Harry Potter","Hang Over","The Purge"]
print(movies[2])
print(movies[0:3])
print(movies[0:])
print(movies[:1])
print(movies[-1])
print(len(movies))

movies.append("Jaws")
print(movies[0:])
movies.pop()
print(movies[0:])
movies.pop(1)
print(movies)