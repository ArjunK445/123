 # create a list of usernames, input a username from the user and check if the username is present in the list or not.
# '''create a dictionary of usernames and paswords, extract all the usernames from the usernames from the dictionary and input 
# usernamesfrom the user and check if the username is present in the extractedlist of usernames'''
# create a dictionary of usernames and password.Input username and password from user also check if ussername and password are correct or not.
 
print("1st question")
list_of_usernames = ["Ryan","Roshan","Ganesh","Arjun","Doom","14","python","9"]
print(list_of_usernames)
print("list of usernames using for loop")
for i in list_of_usernames:
    print(i)
x = input("Enter a username:")
print("Is username present:",x in list_of_usernames)
print()
print()
print("2nd question")
print()

dictionary= {
    "Arjun":"123456",
    "Ryan":"456",
    "Bikki":"arr4"}                                    
print("The usernames are:",dictionary.keys())
print("The passwords are:",dictionary.values())
A = input("Enter username:")
print("Is username present:",A in dictionary.keys() )
print()
print("updated using function")
def user():
    print("The usernames :",dictionary.keys())
def psw():
    print("The passwords:",dictionary.values())
dictionary= {
    "Arjun":"123456",
    "Ryan":"456",
    "Bikki":"arr4"}                                    
user()
psw()
A = input("Enter username:")
print("Is username present:",A in dictionary.keys() )
print()
print("3rd question")
print()
dict = {
    "Janvi": "p125q",
    "Gita":"G112",
    "AA": "1231",
    "Kl_rahul":"55fs"
}
print(dict)
User = input("Enter a username:")
password = input("Enter a password:")
if User in dict and dict[User] == password:
    print("Username and password are correct")
else:
    print("Username and password are incorrect")

