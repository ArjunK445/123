print("Assignment of day 7")
while True:
    choice=int(input("""\nPress 1 for Q.No.1, 2 for Q.No.2, 3 for Q.No.3, 4 for Q.No.4, 5 for Q.No.5, 6 for Q.No.6,
     7 for Q.No.7, 8 for Q.No.8, 9 for Q.No.9, 10 for Q.No.10, 0 for exit: \n Enter number:"""))
    match choice:
        case 1:
            print("1. Write a program to check whether a number is even or odd using if-else.\n")
            A=int(input("Enter a number:"))
            if A%2==0:
                print(f"Given number: {A} is Even number.")
            else:
                print(f"Given number: {A} is odd number.")
        
        case 2:
            print("2. Write a program to check whether a number is positive, negative, or zero.\n")
            Num= int(input("Enter a number:"))
            if Num > 0:
                print(f"{Num} is a positive number")
            elif Num < 0:
                print(f"{Num} is a negative number")
            else :
                print(f"{Num} is zero")
        
        case 3:
            print("3. Write a program to find the largest of two numbers using if-else.\n")
            A = int(input("Enter first number:"))
            B = int(input("Enter second number:"))
            if A > B:
                print(f"{A} is largest number")
            else:
                print(f"{B} is largest number")
        
        case 4:
            print("4.Write a program to print numbers from 1 to 10 using a for loop.\n")
            for i in range(1,11):
                print (i)
        
        case 5:
            print("5. Write a program to calculate the sum of first N natural numbers using a loop.\n")
            N = int(input("Enter number: "))
            for i in range(1,N+1):
                sum = (i*(i+1))/2
            print(f"The sum of first {N} natural number:", sum )
        
        case 6:
            print("6. Write a program to print the multiplication table of a given number.\n")
            N1 = int(input("Enter a number:"))
            def multiply(a):
                multiply = N1*a
                print(f"{N1}*{a}:", multiply)
            print(f"The multiplicaation table of {N1}:")
            for i in range(1,11):
                multiply(i)    
        
        case 7:
            print("7. Write a program to count how many even numbers are between 1 and 50.\n")
            count=0
            for i in range(1,51):
                if i %2 == 0:
                    count= count + 1
            print("The even numbers between 1 and 50 are:",count)
            
        case 8:
            print("""8. Write a program to perform addition, subtraction, multiplication, and division 
            using arithmetic operators.\n""")
            X = int(input("Enter first number:"))
            Y = int(input("Enter second number:"))
            def add():
                sum = X + Y
                print("The sum of numbers is:",sum)
            def subtract():
                sub= X-Y
                print("The subtraction of numbers is:",sub)
            def multiply():
                mult = X*Y
                print("The multiplication of numbers is:",mult)
            def division():
                div= X/Y
                print("The division of numbers is:",div)
            def power():
                power = X**Y
                print(f"The {X} power {Y}  is:",power)
            def modulus():
                mod = X%Y
                print(f"The modulus of numbers {X} and {Y} is:",mod)
            def floor_division():
                floor= X//Y
                print("The floor division between numbers is:",floor)

            add()
            subtract()
            multiply()
            division()
            power()
            modulus()
            floor_division()

        case 9:
            print("9. Write a program to compare two numbers using comparison operators.")
            print(" Comparison operators are: == ,!= , > ,< ,<= , >= ")
            first= int(input("Enter first number:"))
            Second= int(input("Enter second number:"))

            if first==Second:
                print("The numbers are equal")
            elif first>Second:
                print(f"The number {first} is greater than {Second}")
            elif first<Second:
                print(f"The number {Second} is greater than {first} ")
        
        case 10:
            print("""10. Write a program to check whether a number is greater than 10 and 
            less than 50 using logical operators.""")
            first= int(input("Enter first number:"))
            if (first >10) and (first<50):
                print(f"The given number ({first}) satisfy the condition")
            else:
                print(f"The given number ({first}) does not satisfy the condition")
        
        case 0:
            break
        
        case _:
            print("Invalid choice")