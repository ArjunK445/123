print("simple Accounting System")                                                                                       

dict ={"Arjun":"1254",
       "Ram":"123",
       "Hello":"A5A2"}
dict1 ={"Arjun":7000,
        "Ram":4000,
        "Hello":11500
        }
User = input("Enter username:")
Password = input("Enter your password:")
if User in dict and dict[User]== Password:
    print("Login Successful")
    while True:
        choice = int(input("Press 1 for check balance, 2 for add balance, 3 for withdraw balance,4 for exit:\n"))
        match choice:
            case 1:
                print("The total balance :",dict1[User])
            case 2:
                add_amount= int(input("Enter amount to add in balance:"))
                if add_amount >=1500:
                    dict1[User]+= add_amount
                    print("Amount added successfully")
                    print("Available balance :",dict1[User])
                else:
                    print("Add amount greater than 1500")
            case 3:
                withdraw = int(input("Enter amount to withdraw:"))       
                if withdraw <= dict1[User]:
                    dict1[User] -= withdraw
                    print("Amount withdraw successfully")
                    print("Available balance:",dict1[User])
                else:
                    print("balance not available")
            case 4:
                print("Exiting from your system")
                break
            case _:
                print("Invalid choice")
      
else:
   print("Login denied:Invalid username and password")