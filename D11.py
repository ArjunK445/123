print("Updated calculator with try and except")

try:
    num1 = int(input("enter first number:"))
except ValueError as e:
    print(e)
    
try:
    num2 = int(input("enter second number:"))
except ValueError as e:
    print(e)

print()
print("performing the arithmetic operations for given input")
while True: 
    try:
        print("The addition of given number is:",num1+num2)
        
        print("The subtraction of given number is:",num1-num2) 
        print("The multiplication of given number is:",num1*num2) 
        print("The division of given number is:",num1/num2) 
        print("The modulus of num1 and num2 is:",num1%num2)
        print("The floor value of num1:num2 is:",num1//num2)
        print("The power of num1:num2 is:",num1**num2)
    except NameError as e:
        print("check error:",e)
    except ZeroDivisionError as e:
        print("check error:",e)
    break




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
#     try:
#         choice = int(input("1 for register, 2 for login:")) 
        
#         if choice==1:
#             reg()
#         elif choice == 2:
#             login()
#         else:
#             print("exit")
#             break
#     except ValueError as e:
#         print("check error:",e)



# print("Updated simple Accounting System using function, try and except")
# dict = {
#     "Arjun":{"password":"1254","balance":7000},
#     "Ram":{"password":"123","balance":4000},
#     "Hello":{"password":"A5A2","balance":11000},
#     "shristi":{"password":"gg74","balance":10000}
#     }
# def register():
#     while True:
#         Username = input("Enter your username:")
#         psw = input("Enter your password:")
#         if Username in dict:
#             print(f" Given Username ({Username}) already exists!!. Try new one ")
#         else:
#             dict[Username] = {"password":psw,"balance":0}
#             print("Registerd successfully")
#             break
# def add(amount):
#     if amount >=1500:
#         dict[User]["balance"]+= amount

# def withdraw(amt):
#     if amt <= dict[User]["balance"]:
#         dict[User]["balance"] -= amt

# def new_amount():
#     print("your new balance:",dict[User]["balance"])

# while True:
#     try:
#         choice = int(input("1 for register,2 for login, 3 for exit:"))
#         # match choice:
#         if choice== 1:
#             print("\nRegister account in system")
#             register()
#         elif choice==2:
#             print("\n For login into your account")
#             User = input("Enter username:")
#             Password = input("Enter your password:")

#             if User in dict and dict[User]["password"]== Password:
#                 print("Login Successful")
#                 while True:
#                     try:
#                         choice = int(input("Press 1 for check balance, 2 for add balance, 3 for withdraw balance,4 for exit:\n"))
#                         match choice:
#                             case 1:
#                                 print("The total balance :",dict[User]["balance"])
#                             case 2:
#                                 try:
#                                     add_amount= int(input("Enter amount to add in balance:"))              
#                                     if add_amount >=1500:
#                                         print("Amount added successfully")
                                                    
#                                     else:
#                                         print("Add amount greater than 1500")
                                
#                                     add(add_amount)
#                                     new_amount()
#                                 except ValueError as e:
#                                     print("check error:",e)
#                             case 3:
#                                 try:
#                                     X = int(input("Enter amount to withdraw:"))           
#                                     if X <= dict[User]["balance"]:
#                                         print("Amount withdraw successfully")
#                                     else:
#                                         print("balance not available")

#                                     withdraw(X)
#                                     new_amount()
#                                 except ValueError as e:
#                                     print("Error check:",e)
#                             case 4:
#                                 print("Logging out from your account")
#                                 break
#                             case _:
#                                 print("Invalid choice: Enter a valid choice ")
#                     except ValueError as e:
#                         print("check error:",e)        
#             else:
#                 print("Login denied: Invalid username and password")
#         elif choice==3:
#             print("Exiting from system")
#             break  
#         else:
#             print("Enter valid choice")
#     except ValueError as e:
#         print("check error:",e)    