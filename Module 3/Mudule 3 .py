
#Write a Python function to get the largest number, smallest num and sum of all from a list.

def operationNum(l):
    sum = 0
    for i in l:
        sum +=i
    largest = max(l)
    smallest = min(l)
    print(f"""
    Largest number is {largest}
    Smallest number is {smallest}
    Sum of list is {sum}
    """)

numList = [12,21,98,34,54,23,87,99,23]
operationNum(numList)


#How will you compare two lists?
#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

stringList = ["Ahuja", "Ishani", "Jeevan","I","Kombucha","Trumpet","Gondola"]
count = 0
for i in stringList:
    if len(i)>1 and i[0].capitalize() == i[-1].capitalize():
        count = count + 1
print("Total String count with length greater than 1 and first and last index same is ", count)


#Write a Python program to remove duplicates from a list.

stringList = ["Ahuja", "Ishani", "Ahuja","I","Kombucha","Trumpet","Gondola", "Kombucha"]

mySet = set(stringList)
stringList = list(mySet)

print(stringList)


#Write a Python program to check a list is empty or not.

stringList = ["Ahuja", "Ishani", "Ahuja","I","Kombucha","Trumpet","Gondola", "Kombucha"]

if len(stringList) > 0:
    print("The list is not empty")
else:
    print("The list is empty")


#Write a Python function that takes two lists and returns true if they have at least one common member.

def checkList(x,y):
    for i in x:
        for j in y:
            if i == j:
                print("True")
                return True
    print("False")
    return False      

list1 = [1,3,5,7,9,15,17]
list2 = [2,4,6,8,10,11,12,14]

checkList(list1,list2)
    

#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
list1 = []
list2 = []

for i in range(1,31):
    list1.append(i*i)
for j in range(0,5):
    list2.append(list1[j])
for k in range(25,30):
    list2.append(list1[k])

print(list1)
print(list2)

#Write a Python function that takes a list and returns a new list with unique elements of the first list.

stringList = ["Ahuja", "Ishani", "Ahuja","I","Kombucha","Trumpet","Gondola", "Kombucha"]
def uniqueList(l):
    mySet = set(l)
    l = list(mySet)

    print(l)
uniqueList(stringList)

#Write a Python program to create a tuple with different data types.

myTuple = (1, 'Ahmedabad', 9.5, True, False, 99, 'Baroda')

for i in myTuple:
    print(i)

#Write a Python program to create a tuple with numbers.

myTuple = (1,2,9,89,21,99,76)
print(myTuple)

#Write a Python program to convert a list of characters into a string. 

mylist = ['a','n','u','j','l','i','k','e','s','p','y','t','h','o','n']
myStr = ""

for i in mylist:
    myStr += i

print(myStr.capitalize())

#Write a python program to select an item randomly from a list.



#Write a Python program to find the second smallest number in a list. 

mylist = [2,4,6,8,10,11,12,14]

smallest = min(mylist)
mylist.remove(smallest)

secondSmallest = min(mylist)
print(secondSmallest)

#Write a Python program to get unique values from a list

mylist = [2,4,6,8,10,11,12,14,14,12,6]

for i in mylist:
    for j in mylist:
        if i == j:
            mylist.remove(j)
print(mylist)

#Write a Python program to check whether a list contains a sub list 

mylist = [2,[4,6,8],[10,12,14],16,18,20,[22,24,26],28,30]

for i in mylist:
    if type(i) == list:
        print(f"This is a sublist {i}")
    else:
        print(i)

#Write a Python program to split a list into different variables

mylist = [2,[4,6,8],[10,12,14],16,18,20,[22,24,26],28,30]
var1, var2, var3, var4, var5, var6, var7, var8, var9 = mylist

print(f"""      {var1}
      {var2}
      {var3}
      {var4} 
      {var5} 
      {var6} 
      {var7} 
      {var8} 
      {var9}""")

#Write a Python program to convert a tuple to a string.
myTuple = ("Hello","My","Name","Is","Anuj","And","I","Am","Enrolled","In","Python","Course")
myString = ''

for i in myTuple:
    myString = myString + " " + i
print(myString)
#Write a Python program to check whether an element exists within a tuple

myTuple = (1,2,9,89,21,99,76)
myelement = 10
check = False

for i in myTuple:
    if i == myelement:
        check = True


if check == True:
    print("Your element exists in tuple")
else:
    print("Your element does not exist in tuple")

#Write a Python program to find the length of a tuple.

myTuple = (1,2,9,89,21,99,76)
print(len(myTuple))

#Write a Python program to convert a list to a tuple.

mylist = [2,[4,6,8],[10,12,14],16,18,20,[22,24,26],28,30]
myTuple = tuple(mylist)

print(myTuple)

#Write a Python program to reverse a tuple.

myTuple = (1,2,9,89,21,99,76)
newTuple = myTuple[::-1]

print(newTuple)

#Write a Python program to replace last value of tuples in a list.
mylist = [1,2,3,4,5,6,7,(8,9,0)]
for i in mylist:
    if type(i) == tuple:
            mylist.pop()
            mylist.append(8)
            mylist.append(9)
            mylist.append(10)

print(mylist)

            
#Write a Python program to find the repeated items of a tuple.

myTuple = (1,2,76,9,15,78,89,15,78,21,99,21,76)

count = myTuple.count(15)
print("Number 15 appears in the tuple ",count," times")

#Write a Python program to remove an empty tuple(s) from a list of tuples. 

mylist = [1,2,(),3,4,5,6,7,(8,9,0)]
print(mylist)
for i in mylist:
    if type(i) == tuple:
        if i == ():
            mylist.remove(i)
print(mylist)

#Write a Python program to unzip a list of tuples into individual lists.
mylist = [(1,2),(3,4,5),(6,7,8,9),(10,11,12,13,14),(15,16,17,18,19,20)]
#Write a Python program to convert a list of tuples into a dictionary.

#Write a Python script to sort (ascending and descending) a dictionary by value.
#Write a Python script to concatenate following dictionaries to create a new one.
#Write a Python script to check if a given key already exists in a dictionary.

#Write a Python script to print a dictionary where the keys are numbers between 1 and 15.
#Write a Python program to check multiple keys exists in a dictionary
#Write a Python script to merge two Python dictionaries
#Write a Python program to map two lists into a dictionary
#Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b': 200,’d’:400} Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

#Write a Python program to print all unique values in a dictionary.


#Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd

#Write a Python program to find the highest 3 values in a dictionary

#Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, o {'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})

#Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


#Write a Python program to read a random line from a file.
#Write a Python program to convert degree to radian
#Write a Python program to calculate the area of a trapezoid
#Write a Python program to calculate the area of a parallelogram
#Write a Python program to calculate surface volume and area of a cylinder
#Write a Python program to returns sum of all divisors of a number Write a Python program to find the maximum and minimum numbers from the specified decimal numbers.