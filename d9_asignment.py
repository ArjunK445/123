
# Check if a given number is palindrome or not
# Make a login system using registration using function
# Print all the even numbers in a list of numbers. 

num = int(input("Enter a number:"))
y = str(num)
x = int(y[-1::-1])# slicing
print("after reversing:",x)
if num==(x):
    print("It is palindrome number")
else:
    print("Not palindrome")
print()
# A = input("Enter a string:")
# if A == A[-1::-1]:
#     print("given string is palindrome")
# else:
#     print("Given string is not palindrome")


# print("Register and Login")
# users = {}
# def reg():
#     while True:
#         username = input("Enter username:")
#         psw = input("Enter a password:")
#         if username in users:
#             print(" username already exits. Try  new one")
#         else:
#             users[username]= psw
#             print("registered successfully")
#             break
# def login():
#     username = input("Enter your username:")
#     psw = input("Enter password:")
#     if username in users and users[username]== psw:
#         print("Login successfull")
#     else: 
#         print("Try again")
# while True:
#     choice = int(input("1 for register, 2 for login:"))  
#     if choice==1:
#         reg()
#     elif choice == 2:
#         login()
#     else:
#         print("exit")
#         break


number =[1,2,5,8,12,76,79,92]
even_number =filter(lambda x: x%2==0,number)
print("Even numbers are:",list(even_number))