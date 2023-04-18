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
Series_num = int(input("Enter the quantity of numbers you want in the fibonacci series :- "))
fibonacci = []
start_num = 1

for Series_num in range(0,Series_num-1,1):
    if fibonacci == []:
        fibonacci.append(1)
        fibonacci.append(1)
    last_two_sum = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(last_two_sum)

print(fibonacci)




#How memory is managed in Python?

#What is the purpose continue statement in python?

#Write python program that swap two number with temp variable and without temp variable.
a = int(input("Enter a number A : "))
b = int(input("Enter a number B : "))

tempNum = a
a = b
b = tempNum

print("Number A is ", a)
print("Number B is ", b)



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

#Write a Python program to calculate the length of a string.
str_1 = input("Enter a string : ")

print("The length of the entered string is ", len(str_1))

#Write a Python program to count the number of characters (character frequency) in a string
mystr=input("Enter a string :- ")

mystr.count('p')
print("P:-" , mystr.count('P'))


#What are negative indexes and why are they used?
#Negative indexes are for getting the value starting from the back of the string. 
# eg. if "Anuj" is a string, the -1 index would give the value 'j'

#Write a Python program to count occurrences of a substring in a string. 
myStr = 'This is a great horse. It is black in color. It is 4 years Old'
print(myStr.count('is'))

#Write a Python program to count the occurrences of each word in a given sentence
myStr = input("Enter a string :- ")
list = []
list=myStr.split()

for p in list:
    frequency = [list.count(p)]

print(dict(zip(list, frequency)))


print(f"The largest word is {largestWord} and the length is {length}")
    
#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
str1 = input("Enter a string 1 : ")
str2 = input("Enter a string 2 : ")

x = str1[0:2]

str1 = str1.replace(str1[0:2], str2[0:2])
str2 = str2.replace(str2[0:2], x)

print(str1,str2)

#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
enterString = input("Enter a string : ")

if len(enterString) >= 3:
    if enterString.endswith("ing"):
        enterString = enterString.replace('ing', 'ly')
    else:
        enterString = enterString + "ing"
else:
    enterString = enterString

print(enterString)


#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
enterString = input("Enter a string : ")
stringList = enterString.split()

if stringList.index('not') > stringList.index('poor'):
    enterString = enterString.replace('not','good')
    enterString = enterString.replace('poor','good')
else:
    enterString = enterString

print(enterString)

#Write a Python function that takes a list of words and returns the length of the longest one.
myList = []
length = 0
largestWord = ''
num = int(input('How many words do you want to add in the list? : '))

for items in range(num):
    element = input(f'Enter List element {items+1}: ')
    myList.append(element)

for word in myList:
    if len(word) > length:
        length = len(word)
        largestWord = word
    else:
        length = length

print(f"The largest word is {largestWord} and the length is {length}")
    
#Write a Python function to reverses a string if its length is a multiple of 4.
enterString = input("Enter a string : ")
if len(enterString)%4 == 0:
    enterString = enterString[::-1]
else:
    enterString = enterString

print(enterString)

#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
enterString = input("Enter a string : ")
firstTwo = enterString[0:2]
lastTwo = enterString[-2:]

if len(enterString) < 2:
    print(enterString)
else:
    enterString = firstTwo + lastTwo
    print(enterString)

#Write a Python function to insert a string in the middle of a string.
str = "My is Anuj"
word = "Name"

str = str[:3] + word + str[2:]

print(str)