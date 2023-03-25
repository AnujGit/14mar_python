#Write a Python program to check if a number is positive, negative or zero.

a = int(input("Enter a number : 0")) 

if a < 0:
    print("The number is negative")
elif a > 0:
    print("The number is positive")
else:
    print("The number is Zero")


#Write a Python program to get the Factorial number of given number.

a = int(input("Enter a number to get its factorial: "))
factorial = 1

for a in range(a,0,-1):
    factorial = factorial * a

print(f"{factorial}")

#Write a Python program to get the Fibonacci series of given range.


#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
num = int(input("Enter value of a :- "))

if num%2 == 0:
    print("A is an even number")
else:
    print("A is an odd number")

#Write a Python program to test whether a passed letter is a vowel or not.
char = int(input("Enter a letter between a - z :- "))

if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
    print("The passed letter is a vowel")
else:
    print("The passed letter is nota vowel")

#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter first number : ")) 
b = int(input("Enter second number : ")) 
c = int(input("Enter third number : ")) 
sum = 0

if a == b or b == c or c == a:
    print("The sum of three numbers is 0")
else:
    sum = a+b+c
    print(f"The sum of three numbers is {sum}")

#Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
a = int(input("Enter first number : ")) 
b = int(input("Enter second number : ")) 

status = True

if a == b or a+b == 5 or a-b == 5 or b-a==5:
    status = True
else:
    status = False

print(status)

#Write a python program to sum of the first n positive integers.

n = int(input("Enter a number : "))
sum = 0

for n in range(0,n+1,1):
    sum = sum + n

print(f"{sum}")