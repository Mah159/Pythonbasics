# -*- coding: utf-8 -*-
"""MaheenSalman_PythonBasics1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X2cZILkjRn3zsTcd9ZC0O-rv-Ou1Wdj1

Task 1: Variables and Data Types

a) Create three variables: one for storing your age (integer), one for your name (string), and one to
check if you are a student (Boolean). Print the variables.
"""

a = 22 #initializing age
print ("Your age is ", a)
n = "maheen" #initializing name
print ("Your name is ", n)
s = True
ns = False
d = input("Are you a student? (Yes/No) ") #Taking an input from user and storing it in the variable d
if d == "Yes" or "yes": #initializing if to check the input from user, or is used to cater to lowercase or upper case
   print (s)
else:
  print (ns)

"""b) Perform the following operations and print the results:
- Add 25 to your age variable.
- Concatenate your name with the string "Smith"
- Negate the Boolean variable (if True, make it False, and vice versa).
"""

a = 25 #initializing age
a += 25 #adding 25 in age
print (a) #printing age

name = (input("What is your name? ")) #intializing the name as a string to take an input from the user with the help of the input function
surname = "Smith" #initializing surname
fullname = name + " " + surname #adding the surname Smith in the users first name
print ("Your full name is", fullname) #printing fullname
s = True
a = input("Are you a student? (Yes/No) ") #Taking an input from user and storing it in the variable s
if a == "Yes" or "yes": #initializing if to check the input from user, or is used to cater to lowercase or upper case
   print (not s)
else:
  print (s)

"""Task 2: Expressions and Operators
a) A rectangle has a width of 5.5 units and a height of 3.25 units. Store width and height in variables.
Create a new variable called area and write an expression to calculate the area. Print the area in the
output.
"""

width = 5.5 #initializing width of rectangle
height = 3.25 #initializing height of rectangle
area = width*height #calculating area of rectangle by multiplying width and height
print ("Area of rectangle is ", area) #printing area

"""b) Create a temperature variable in Celsius. Convert it to Fahrenheit using the formula: F = (C * 9/5)
+ 32. Store this temperature in a variable called Fahrenheit and print this variable.
"""

#converting Celsius into Fahrenheit
Celsius = float(input("What is your required temperature in Celsius? ")) #converting input value of temperature into an float number, it allows us to take input in float or integer
Fahrenheit = ((Celsius*(9/5)) + 32) #applying formula of Fahrenheit
print ("Your", Celsius, "degree temperature when converted to Fahrenheit is ", Fahrenheit) #printing conversion of celsius to fahrenheit

"""c) Create a variable called radius and give it a value of 5. Calculate the area of a circle with this radius
and store it in a variable called area. Print area at the end of your code. (Use the formula: area = π *
radius^2, where π (pi) is approximately 3.14159).
"""

radius = 5 #initialzing the defined value 5 of radius
area = (3.14159 * (radius**2)) #implementing the formula of area of circle
print ("Area of circle is ", area) #printing the area of a circle

"""Task 3: Introduction to Data Structures

a) Create a list called "fruits" containing the following fruits: "apple" "banana" "orange" "grape" and "kiwi". Print the list.
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"] #initialzing a list of fruits
print(fruits)

"""b) Create a tuple named &quot;months&quot; with the names of the first three months of the year. Print the
tuple.
"""

months = ("January", "February", "March") #initializing the tuple called months to store the first three months. Tuples are immutable
print(months)

"""Task 4: List Manipulation
a) Given the list of numbers below, write a Python program to calculate the sum and average of
these numbers. Print both results.
numbers = [12, 34, 45, 67, 89, 100, 23, 56]
"""

#Calculating the sum of a list of numbers using for and the sum function
numbers = [12, 34, 45, 67, 89, 100, 23, 56] #initialzing a list of numbers
total = 0 #initializing total as zero so that numbers can be stored and added to it
for i in range (0, len(numbers)): #defining the for loop to run till the last index of the list by using the len function, i is the index and range allows us to create a collection
  total = total + numbers[i] #the first time the for loop runs we will get starting with 0 + 12 = 12 then 12 + 34 = 46 and so on
  print (total)
print ("Sum of the numbers given in the list is", total)

total = sum(numbers) #The sum function can also be used to calculate the sum of numbers in the list

print ("Sum of the numbers given in the list is", total)

#Calculating the average
average = total / len(numbers)

print("Average of the numbers given in the list is", average)

"""b) Remove the first and last elements from the &quot;fruits&quot; list created earlier. Print the updated list."""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

#Removing the last element
fruits.pop()

#Removing the first element
fruits.pop(0)

print(fruits) #Output: ['banana', 'orange', 'grape']

"""Task 5: Dictionary Operations
a) Create a dictionary named &quot;capitals&quot; with three key-value pairs: &quot;USA&quot; - &quot;Washington D.C.,&quot;
&quot;France&quot; - &quot;Paris,&quot; and &quot;Japan&quot; - &quot;Tokyo.&quot; Print the dictionary.
"""

capitals = {"USA":" Washington DC", "France":"Paris", "Japan": "Tokyo"}#initializing dictionary for capitals of three countries
print(capitals) #printing the complete dictionary

"""b) Add a new country and its capital to the &quot;capitals&quot; dictionary. The country is &quot;Germany,&quot; and the
capital is &quot;Berlin.&quot; Print the updated dictionary.
"""

capitals = {"USA":" Washington DC", "France":"Paris", "Japan": "Tokyo"} #initializing dictionary for capitals of three countries

capitals["Germany"] ="Berlin" #adding Berlin capital of Germany in the dictionary
print(capitals)

"""c) Check if &quot;France&quot; exists in the &quot;capitals&quot; dictionary. If it does, print &quot;France is in the dictionary,&quot;
otherwise, print &quot;France is not in the dictionary.&quot;
"""

capitals = {"USA":" Washington DC", "France":"Paris", "Japan": "Tokyo"} #initializing dictionary for capitals of three countries
country = "France" #initializing the country france to check if it is present in the list
if country in capitals: #using if to check if the country france is present in the list
  print ("France is in the dictionary")
else:
  print ("France is not in the dictionary")

"""Task 6: Comparison Operators, Logical Operators and If/Else:
a) Create a variable called number that takes user input (we studied the input() function). Next,
write a block of code that checks if the number is even or odd
"""

number = int(input("Enter a number to check if it is even or odd ")) #initializing number as an integer value to be taken from the user
if number % 2 == 0: #using the modulus operator to check if the input number when divided by 2 must have a zero operator for it to be an even number
  print("The number entered is even")
else:
  print("The number entered is odd")

"""b) Create two variables called age and GPA. Give them values of your choice. Next, write a block of
code to check if a student with this age and GPA is eligible for admission. The following are the
conditions:
- The student must be at least 18 years old.
- The student&#39;s GPA must be 3.0 or higher on a scale of 4.0.
Your output should print “Eligible for admission” or “Not eligible for admission”.
"""

age = int(input("Kindly enter your age: ")) #Initializing the input age as an integer and taking input from the user
GPA = float(input("Kindly enter your GPA: ")) #Initializing the input GPA as a float and taking input from the user
if age >= 18: #Since the requirement of age is at least 18, the greater than and equal to comparison operator is used
 if 3.0 < GPA < 4.0: #Nested if is used as both defined requirements of age and GPA need to be met inorder to be eligible for the admission, here the GPA range is defined between 3 and 4
  print("Eligible for Admission")

else:
  print("Not eligible for Admission")

"""Task 7: Advanced Data Types
a) Create a set named &quot;fruits_set&quot; containing the following fruits: &quot;apple,&quot; &quot;banana,&quot; &quot;orange,&quot;
&quot;grape,&quot; and &quot;kiwi.&quot; Print the set.
"""

fruits_set = {'apple', 'banana', 'orange', 'grape', 'kiwi'} #initializing the set of fruits
print(fruits_set) #printing the set of fruits

"""b) Given two sets:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

Write Python code to perform the following operations and print the results:
- Union of set1 and set2.
- Intersection of set1 and set2.
- Difference between set1 and set2.
- Check if set1 is a subset of set2.
"""

set1 = {1, 2, 3, 4, 5} #initializing set1
set2 = {3, 4, 5, 6, 7} #initializing set2
print("Union of set1 and set2 is", set1.union(set2)) #finding the union of set1 and set2
print("Intersection of set1 and set2 is", set1.intersection(set2)) #finding the intersection of set1 and set2
print("Difference between set1 and set2 is", set1.difference(set2)) #finding the difference between set1 and set2
print("Is set1 subset of set2? (T/F):", set1.issubset(set2)) #checking to see if set1 is subset of set2 using the issubset function

"""Task 8: Strings Manipulation
a) Create a string variable containing the following sentence:
&quot;Python programming is fun and powerful!&quot;
Write Python code to do the following and print the results:
- Find the length of the string.
- Convert the string to uppercase.
- Replace &quot;fun&quot; with &quot;exciting.&quot;
- Check if the string contains the word &quot;Python.&quot;
- Split the string into a list of words.
"""

strn = "Python programming is fun and powerful!" #initializing a string
print("The length of the string is:", len(str))
#The .upper function allows us to print every letter in the string in Uppercase
print("The string in uppercase is:")
print(strn.upper())
#The replace function allows us to replace any character in the string
print("Replacing fun with exciting:")
strn.replace("fun", "exciting")
#The string find function returns 0 as the word Python is at the beginning of the string
print("The index of the word Python in this string is:", strn.find("Python"))
#Now to convert the string into a list the split function is used
print("Converting the string into a list")
sstrn = strn.split ()
print(sstrn)