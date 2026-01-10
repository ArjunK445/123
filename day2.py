# create a simple calculator app where you assign two values and perform arithmetic operations with the values.
# input two numbers from user and perform all the arithmetic operations on them

#for 1st question

A = 25   #assigning the value  
B = 12
print("A:", A)
print("B:", B)
print("The addition of A and B is:", A+B)
print("The subtraction of A and B is:", A-B)
print("The multiplication of A and B is:", A*B)
print("The division of A and B is:", A/B)
print("The modulus(reminder) of A and B is:", A%B)
print("A power B is:", A**B)
print("The floor value of A and B is:", A//B)
print()

#for 2nd
print("for second question")
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
print()
print("performing the arithmetic operations for given input")
while True: # while loop used (updated)
    print("The addition of given number is:",num1+num2)
    print("The subtraction of given number is:",num1-num2) 
    print("The multiplication of given number is:",num1*num2) 
    print("The division of given number is:",num1/num2) 
    print("The modulus of num1 and num2 is:",num1%num2)
    print("The floor value of num1:num2 is:",num1//num2)
    print("The power of num1:num2 is:",num1**num2)
    break