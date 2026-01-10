#print("arjun")
#print('mustang')
#print("lokesh and ramesh are good friend")

#d2
#name = 11
#print(type(name))

#a = 9
#b =8
#a +=5
#print(a%b)
#print(a==b)

#llogical operators
# ANd opratoor: both condition true results true
# OR operator: any condition is true results true
# Not Operator: codition and results are opposite

#a = True
#p= False
#print(a or p)
#print(a and p)
#print( not p)

#print("identity operator")
#identity operators : is, isnot
#print(7==7)
#print(9!=4)

#print("membership operator")
#membership operator : in, not in
#bike = "motor"
#print('s' in bike)

#bitwise operator, comparision operator, assignment operator
#for multiline comment/multiline string use:"""

#indexing: accessing only one element in a particular index
#positive indexing: we write positive value
#negative indexing: we write negative value
#print('indexing')
# c="python in mdriser"
# print(c[5])
# print("negative indexing:",c[-5])

#slicing: accessing a group of element in a particular group element. The end value is exclusive(not included)
# print('slicing')
# print(c[5:11])
#print(c[3:8:2]) #steping

#in dictionary, membership operator(in, not in) only checks key values 

#day4 
# conditional statements
# 1. if else statements
#finding the greatest nnumber among three nummbers
# if condition:
#   statement
#Elif ladder
#percentage = float(input("enter percentage:"))
#if percentage >= 90:
 #   print("A+")
#elif percentage >= 80 and percentage <90:
#    print("A")
#elif percentage >= 70 and percentage < 80:
#   print("B+")
#else:
#    print("fail") 

# python match   ( same as sitch case )
#A = int(input("enter first number;"))
#B = int(input("enter second number;"))
#choice = int(input(" Press 1 for sum, 2 for sub, 4 for multiply,9 for division:"))
#match choice:
#(    case 1:
     #   print(A+B)
    #case 2:
     #   print(A-B)
    #case 4:
    #    print(A*B)
    #case 9:
        #print(A/B)
    #case _:
        #print("invalid")

# loops are used when we need to execute the same block of code multiple times repeatedly
# 2 types of loops: 
# for loop : for loop is ussed when we know the start and end condition
# syntax: for iterator  in iterable:
#           statements
# Iterator : it is a variable that stores the element when a loop completes an iteration
#  Iterable : it is simply a group data type
# Iteration : one complete round of a loop
# while loop: it is used when we dont know the starting and stopping condition

# Nested loop: loop inside another loop
#infinite loop: a loop that runs infinitely:> doesnot have stopping conditions
#practice for loop, nested for loop
# range(): it generates data (used in for loop)
#syntax: range(start,end,step)
#for i in range(5,15,3):
 #   print(i)

# list comprehensive
#list = [1,2,3,4,5,6,7,8,9]
#list_comp =[x+2 for x in range(2,80)]
#print(list_comp)
# break and continue also practice
# syntax of while loop
#while condition:
#   statement

#a=5
#while a> 2:
#    print(a)
#    a-=2

# while True:
#     choice  = int(input("press 1 for add, 2 for sub, 3 for skip,4 for exit: "))
#     match choice:
#         case 1:
#             n =int(input("1st number:"))
#             m =int(input("2nd number:"))
#             print(n+m)
        
#         case 2:
#             n =int(input("1st number:"))
#             m =int(input("2nd number:"))
#             print(n-m)

        
#         case 3:
#             print("skip")
#             continue
#         case 4:
#             print("exit")
#             break
#         case 5:
#             pass
#         case _:
#             print("invalid")
            
# for else: If break encounters in for loop, it exits the loop with else part also skipped. IF break doesnot encounters, it completes the loop and execues the else part.

# day 6 
# functions
# functions are used when we need to execute same bl;ock of a code again and again
# It helps us to euse the same block of a code again and again and functions make our code structured
# def keyword is used to define a function
#syntax:  def function_name(parameters):
#           code to be executed
#only by defining a function does not works, we need to call a function
# to call a function, function_name(arguments)
#eg{
# def add():
#     A= int(input("Enter value:"))
#     B = int(input("Enter second value:"))
#     print(A+B)
# add()
# for i in range(15):
#  #  print(i)
# add()
#  }

#Arguments: the values that we send to a function, they are passed while calling a function
# Parameters: The variables that stores the arguments. they are defines while defning a function

# def add(a,b):
#     print(a+b)
# num1 = int(input("enter num1:"))
# num2 = int(input("enter num2:"))
# add(num1,num2)

# day 7
#Local variable: variable ddefined inside a function. it can be accessed only inside the function
#  Global variable: variable defined outsidde the function. It can be accessed anywhere in the function

# Types of functon
# 1. Builtin functons : Functions that are alredy defined inpython. Eg. print(), input(),type()
#2. User defined functions: functions that are defined by the  programmers. Eg. add(),sub()

# Types of fuction based on return type
# function with return type: function that return  value
#function without return type: function that do not return value
# To return a value, we need to use return keyword
# def add(a,b):
    # print(a+b) # non-returnable function
    # return a + b # returnable function
# # A function is always returns  value from where that function is being called
# # we should use return keyword at the last of the function
# result =add(5,10)
# print("result")
 
# # Formatted string
# age=50
# print(f"My name is Dipak. i am {age} years old.  ")

# day 8
# Types of functions
# lambda functons
# map functions
# filter functions
# Reduce functions
# Zip functions

# lambda functions: function in one line
# eg: normal function 
        # def (a,b)
        #   print (a+b)
        # add(2,5)
# syntax:
# lambda parameters: statement
#  we need to store a lambda function into a variable
# To call a lambda function, we need to call the variable
# eg: add=lambda a,b: print(a+b)
#  add(5,10) 
# disp = lambda name: name
# result = disp("Arjun")
# print(result)

# map functions
# It applies a function to each element of an iterable (like list).
# eg:
# number =[1,2,5]
# greater=map(lambda x: x>3,number)
# print(list(greater))

# filter functions
# number =[1,2,5]
# greater=filter(lambda x: x>3,number)
# print(list(greater))

# Reduce functions
# Reduce converts a group data type into a single value based on our condition
# from functools import reduce

# list1 = [11,2,3,4,5]
# add =reduce(lambda x,y:x+y,list1)
# print(add)

# Zip functions
#  It combines two or more iterables into a single iterable based on the index positions
# a = [1,2,3,4,5,6]
# b = ['a','b','c','d','e','f']
# c = zip(a,b)
# print(list(c))


# day 9
# Python File Handling
# File: It is a named location on the disk to store related information
# File Handling: It is the process of creating , reading, updateing and deleting file
# File Handling Flow
# 1. Open a File 
# 2. Perform operations 
# 3. Close the file 

# #Open a file 
# open() function is used to open a file
# syntax: open (path,mode)
# mode = 'r' - read mode: used to read content of file. If file not found, it throws an error.
# mode = 'w' - write mode: used to write content to a file. If file not found, it creates a new file.If file is found, it overwrites the content of a file.
# mode = 'a' - append mode: used to add content to a file. If file found, it creates a new file. If file is found, it add content to the end of a file.
# we can write only  string or JSON in a file
# we can get string or json when we read a file

#day 10
# file handling contd....

# day 11
# Exception Handling
# Handling the errors in a graceful manner

# Try and Except
# try :
# try block contains the code which may raise an exception
# except:
#  if error aridse in try bllock, then the except block is executed

# l =[10,20,30,40,50]
# try:
#     print(l[20])
# except:
#     print("An error occured")
# finally:
#     print("This block runs anyway")
# l =[10,20,30,40,50]
# try:
#     print(l[20])
#     print(10/0)
#     file = open("qqq.txt","r")
#     content = file.read()
#     file.close()
# except IndexError:     #for each error,  here for index error 
#     print("An error occured: check your index")
# except ZeroDivisionError as e:
#     print(e)
#     # print("division by zero is not allowed")
# except FileNotFoundError:
#     file =open("qqq.txt","w")
#     file.close()
# except:
#     print("error occur")

# __str__: if any object gets print,__str__ will executed


# day 12
# oop(object oriented programming): It is a new technique in programming language that organizes the code in classes and object.
# class is a blueprint to create an objct. It defines the structure and behaviour of an object. Keyword "class" is used to create a class.
#  Object is simply a variable calling class. Object are the instances of class. Objects are created by calling the class.

# Attributes: The variables defined inside the class. Attributes describes the properties of class.
# Methods: The functions defined inside the class. It describes the behaviour of the class

# class dog:
#     eyes=2
#     legs = 4
#     tail = 1
#     def bark(self):
#         print("dog barked")
#     def eat(self):
#         print("eating food")

# sete = dog()
# kali = dog()

# print("tails of sete:",sete.tail)
# print(kali.bark())
# sete.eat()
# del kali.bark
# kali.bark()

# day 13
# class attributes => The attributes that do not change according  to the object.
# object atributes => The attributes that change according o the object.
# Inheritance
# Encapsulation

# day 14
# Abstraction: Showing what is needed and hiding the implementation details

# Constructors and decorators
# constructor is a special method that executes automatically when an object is created
# There is only one constructor that is __init__()
# It is mainly used to create object attribute
# class student:
#     college="mindriser"
#     def __init__(self,name,age,gender):
#         self.name = name
#         self.age =age
#         self.gender = gender
#     def display(self):
#         print(f"Name:{self.name}")
#         print(f"Age:{self.age}")
#         print(f"gender: {self.gender}")
#         print(f"college: {self.college}")
# ss = student("ram",45,"male")        
# s = student("arjun",22,"male")
# v = student("sita",23,"female")

# ss.display()
# s.display()
# v.display()

# Decorators: the special function that receive a function as an argument and modifies the function withput changing its code.
# Decorators always have a nested function and returns the nested. And the nested function helps to modify the received function.
#  To use decorator, we need to use @ prefix of the decoratorsjust above the function


# def decorator(func):
#     def wrapper():
#         for i in range(5):
#             print("Hello programmer")
#         print("........")
#         func()
#         print("........") 
#         print("thank you")
#     return wrapper

# @decorator
# def abc():
#     print("Mindrisers ")
# abc()


# Types of Decorators
#  Static method
# abstract method

# @static method

# class stud:
#     @staticmethod
#     def display():
#         print("display sth")
# s1 = stud()
# s1.display()

# @abstract method
# If the parent class is inherited from ABC(ABC = Abstract Base Class) and has one abstract method
# Every child class that inherits the parent class should have abstractmethod

# from abc import ABC, abstractmethod

# class teacher(ABC):
#     name= "Teacher"

#     @abstractmethod
    
#     def teaches(self):
#         print("I am a teacher")
    
# class Mathteacher(teacher):
#     name = "Ram" 
#     def teaches(self):
#         print("Math teacher")

# m = Mathteacher()
# print(m.name)


# Polymorphism
# The main idea of polymorphism is same method or attribute with different behaviour according to class

# class bird:
#     name = "bird"
#     def sound(self):
#         print("Bird is chirping")

# class dog:
#     name = "dog"
#     def sound(self):
#         print("Bird is barking")
# b = bird()
# d = dog()
# print(b.name)
# print(d.name)
# b.sound()
# d.sound()

#day15

#  Magic Methods
# The special symbol methods in python that runs automatically and also starts and ends with double underscores(__).
#  __init__ : constructor
# __str__ : called automatically when object is printed
# __add__ : called hen + operator is executed
# __subtract__: called hen - operator is executed
# __len__ : returns the length of the data data type when len() is executed

# class abc:
#     name ="kkl"
#     def display(self):
#         print("abc is called")
#     def __str__(self):
#         return "an object is being called"
# a = abc()
# print(a)

# Download git and create account in github.com

# library management system classses: book, library,.
# Add methods to add_book, remove_book, search_boook.
# use inheritance for different book types(eg. Ebook).

# class Book:
#     def __init__(self,name,author,pages):
#         self.name=name
#         self.author=author
#         self.pages=pages
#     def display(self):
#         print(f"Name of Book:{self.name}")
#         print(f"Author name:{self.author}")
#         print(f"Pages of Book:{self.pages}")

# class Ebook(Book):
#     def __init__(self, name, author, pages,size):
#         super().__init__(name, author, pages)
#         self.size = size
#     def display(self):
#         super().display()
#         print(f"File size:{self.size}")

# b = Book("Poor Man","Ram",200)
# b1 = Book("Nepal","Prithivi Narayan shah",680)
# e = Ebook("random auction","Shrivastav",800,"215kb")

# # b.display()
# # b1.display()
# # e.display()


# class LMS:
#     books=[]
#     def add_book(self,book):
#         self.books.append(book)
    
#     def remove_book(self):
#         book_name = input("Enter book name to remove:")
#         for book in self.books:
#             if book_name== book.name:
#                 self.books.remove(book)
#                 print("Removed successfully")
#             else:
#                 print("Book not found")
#                 break

#     def search_book(self):
#         book_name = input("Enter book name to search:")
#         for book in self.books:
#             if book_name== book.name:
#                 self.books.index(book)
#                 print("Removed successfully")
#             else:
#                 print("Book not found")

#     def display_book(self):
#         for book in self.books:
#             print(f"Name = {book.name}")
#             print(f"Author = {book.author}")
#             print(f"Pages = {book.pages}")
#             if"Ebook" in str(book):
#                 print(f"File size = {book.size}") 
#             else:
#                 print("Physical book \n")

# lms1 = LMS()
# lms1.add_book(b)
# lms1.add_book(e)
# lms1.display_book()
# lms1.remove_book()
# lms1.display_book()



# # update the program with file handling , try and except, loop


# day 16
# Git and Github
# Git is a command line interface that keeps track of your code.
# Git is VCS(version control system)
# Git flow
# 1. Initialize git: Git creates a empty folder(only once for a project)
#  command: git init
# U : Untracked
# A : Added
# M : Modified
# 2. connect your project folder with github repository
# command: git remote add origin{ssh-key}(only once for project)
# 3. add files to git: git add{file_name}
# To add all files at once 
#  command: git add . 

# 4. commit the changes 
# command:git commit -m "{message}"
# Push the code to github : git push -u origin {branch_name} : first push
# -u : Upstream (Upstream stores the current pushed branch name)
#  When you keep the upstream, git push pushes to the upstream branch
# git push origin {branch_name}



# day 17
# Numpy
#  It stands for numerical python used for numerical calculations.

# Here range = arange where arange acceptds stepping decimal(2.5)
# np.arange(start,end,step)
# np.linspace(start,end,number)
# 
# To generate random number 
# np.random.rand(number of elements)  #here, rand only acess number from 0 &1
# np.random.randint(number of elements) # randint only access integer number

# In numpy ,we can create an empty array using np.empty()
#  empty gives garbage value, similar(close value) as 0.
