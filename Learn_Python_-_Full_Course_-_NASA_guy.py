
from math import * #This module can use floor(), ceil(), sqrt()
##1
"""
phrase = "Giraffe Academy"
print(phrase.replace("a", "\n"))
"""

<<<<<<< HEAD
=======

>>>>>>> 708b897b7c19225dbb92167a40582a0c7684ad45
##2
""""
print(3 + 3 * 3)
print(10 % 3)

my_num = -5
print(str(my_num) + " my fav number") #convert to string
print(my_num)
print(abs(my_num)) #absolute value
print(pow(my_num, 2)) #power to
print(sqrt(36))
"""

##3
"""
name = input("Enter thy name: ")
age = input("Enter thy age: ")

print("Hello " + name +  "! " "You arth " + age + " years old")
"""

#5 Lists
"""
friends = ["Kevin", "Karen", "Jim"]
#             0        1       2

print(friends)
print(str(friends) + friends[1])
print(friends[-1])
print(friends[1:3])

friends[1] = "Mike"
print(friends[1:3])
"""

#6 List functions
"""
lucky_numbers = [1, 2, 3, 4, 5, 6]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.extend(lucky_numbers) #add a list to extend to the friends list
friends.append("Bob") # add a name to the end of the list
friends.insert(1, "Kelly")  # add a name Kelly at index posotion 1
friends.remove("Kelly") #remove the element "kelly" from the list
friends.clear() #remove all elements from the list
friends.pop() #remove the last element in the list
friends.index("Kevin") #extracts the element number of "Kevin"
friends.count("Jim") #how many times does Jim repeat in friends
friends.sort() #Sort friends in alphabetical order
lucky_numbers.sort() #Sort numbers in Accending order.
lucky_numbers.reverse() #reverse the order of the elements

print(friends)
"""

#7 Tuples
"""
coordinates = (4, 5)
coordinates = [(4, 5), (1, 2), (2, 1)]
#coordinates[1] = 10 # can not change tuple values, this gets an error
print(coordinates[1])
"""

#8 Functions
"""
def say_hi(name, age):

    print("Hello " + name + "you are " + str(age))

say_hi("Mike", 13)
say_hi("Bob", 12)
say_hi("Steven", 50)
"""

#9 Return statement
"""
def cube(num):
    return num*num*num

result = cube(4)

print(result)
"""

#10 If statements
"""
is_male = False
is_tall = False

if is_male and is_tall:
    print("You are a male and tall")
elif is_male and not(is_tall):
    print("You are a short male")
else:
    print("You neither male or not tall or both")
"""

#11 if statements and comparisons
"""
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(5000, 11, 12))
"""

#12 Building a better calculator
"""
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Not a valid operator")
"""

#13 Dictionaries
"""
monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}

print(monthConversions.get("Mok", "Not a valid key"))
"""

#14 While loops
"""
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done!")
"""

#15 Build a guessing game
"""
secret_word = "Whale"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOST!")
else:
    print("YOU WON!")
"""
<<<<<<< HEAD

#16 For loop
"""
friends = ["Bob", "Jim", "Steve"]
for friend in friends:
    print(friend)
"""

#17 Exponent function
"""
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result *base_num
    return result

print(raise_to_power(2, 3))
"""

#18 2D lists and Nested loops
"""
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

for row in number_grid:
    for col in row:
        print(col)
"""

#19 Building a translator
"""
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("Enter a phrase: ")))
"""

#20 Comments
"""
print("Comments are fun")
"""

#21 Try Except
"""
try:
    ans = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")
"""

#21 Reding from files
"""
emp_file = open("emp.txt", "r") #open in read mode

print(emp_file.readable())     # returns a bool if we can read the file or not
print(emp_file.read())         # read the file
print(emp_file.readlines()[1]) # read the first line of the file
print(emp_file.readlines())    # read all the lines and put them in list

emp_file.close() #close file
"""

#22 Writing to files

emp_file = open("emp.txt", "a") #open in append mode
emp_file.write("\n7 - Ken")

emp_file.close()

emp_file = open("emp1.txt", "w") #open in write mode
emp_file.write("\n7 - Ken")

emp_file.close()

#23 Modules and pip's
"""
# google -> list of python modules
# python-docx pip install python-docx

import docx

docx.
"""

#24 Classes and objects
"""
from Student import Student

student1 = Student("Jim", "Physics", 4.3, False)
student2 = Student("Pam", "Art", 3.7, True)
print(student2.gpa)
"""

#25Build a multiple choice quiz

"""
from Question import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct!")

run_test(questions)
"""

#26 Object functions
"""
from Student import Student

student1 = Student("Jim", "Physics", 4.3, False)
student2 = Student("Pam", "Art", 3.4, True)
print(student2.gpa)
print(student2.on_honor_roll())
"""
#27 Inheritance

from Chef import Chef

#28 Python interpreter
"""
python3 in terminal
"""





=======
#16 For loop

friends = ["Bob", "Jim", "Steve"]
for friend in friends:
    print(friend)
>>>>>>> 708b897b7c19225dbb92167a40582a0c7684ad45


