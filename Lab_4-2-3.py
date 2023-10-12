#Create a Python file named lab_4-2.py

#*** You must write a comment for every chunk of code you write from now on along with your author tag***

#Create a Python file named lab_4-2.py
#Create a variable called school and set it equal to "Fairfield Prep".
school = "Fairfield Prep"
#Write a statement that splits "Fairfield" and stores it as first_half, and a similar statement that splits " Prep" and stores it as second_half.
first_half = school[0:9]
second_half = school[10:14]
#Print each half on its own line, then print the two halves joined together using concatenation.
print(first_half) 
print(second_half)
print(first_half + second_half)
#____________________________________
#Create a Python file named lab_4-3.py
#*** You must write a comment for every chunk of code you write from now on along with your author tag***
string_1 = input("String one:")
string_2 = input("String two:")
#Write a program that contains a conditional similar to that on slide 4 that will compare two strings 
#provided by the user and return if the strings are equal, one string is greater than the other, or one string is less than the other.
if string_1 < string_2:
    print("string_1 < string_2")
elif string_1 > string_2:
    print("string_1 > string_2")
else:
    print("They are equal")    
