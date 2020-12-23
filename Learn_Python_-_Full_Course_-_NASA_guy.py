
from math import * #This module can use floor(), ceil(), sqrt()
##1
"""
phrase = "Giraffe Academy"
print(phrase.replace("a", "\n"))
"""


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
#16 For loop

friends = ["Bob", "Jim", "Steve"]
for friend in friends:
    print(friend)


