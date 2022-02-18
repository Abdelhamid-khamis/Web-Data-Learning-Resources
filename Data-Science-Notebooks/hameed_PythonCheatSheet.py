"""          === Python Complete Cheat Sheet ===         """
# واقف عند الفانكشنز
# ألماتبلوتليب نص عند وقفت


''' == {1} Variables and Containers(Data Types) == '''
# -------------------------------------------------------------
'''  {1.1} Variable Assignment  '''
import math as m
from math import sin,sinh
"""
The pythonic way to name variables is to use {snake_case} 
{all lowercase letters} and {underscores} to separate words. 
my_height = 58
my_lat = 40
"""
lst = "Name: abdelhameedkhamis@yahoo.com \n Abdelhamid\'s pass: RoTaNa_CiNeMa01032775729"
name = "Abdelhamid"
years = 25

List = ['apple', 'banana', 'cherry','mango','guava']
bikes = ['trek', 'redline', 'giant']
users = ['val', 'bob', 'mia', 'ron', 'ned']

alien = {'color': 'green', 'points': 5}
alien_0 = {'color': 'green', 'points': 5}
Dictionary = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

Set = {'apple', 'banana', 'cherry'}
Set1 = {'apple', 'banana', 'cherry'}
Set2 = {'google', 'microsoft', 'apple'}

Tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5) # or 1,3,....
Tuple1 = 'apple', 'banana', 'cherry'
dimensions = (800, 600) 

x7 = 1.2 + 8 + sin(90)  # Regular assignment
x1,x2 = 2,3     # Multiple Assignment
x1,x2 = x2,x1   # values swap
x3 = x4 = 5     # same value assignment
x1 += 1         # increment value by 1
x2 *= 2         # x2 = x2 * 2


'''  {1.2}      # Arithmetic operators  '''

x1 + x2       
x1 - x2       
x1 * x2       
x1 / x2       # float division
x1 ** x2      # power (i.e. x1**(1/2) is the square root of x1)
x1 // x2      # integer division
x1 % x2       # remainder division
4.445e8 == 4.445 * 10 ** 8

'''  {1.3} Conversion  '''
type(15)
int("15")
int("3f",16)
int(15.56)
round(15.56,1)
str(15)
chr(64)                         #'@'
ord('$')                        # returns an integer representing the Unicode character.
list("abc")                     #['a','b','c']
dict([(3,"three"),(1,"one")])   # {1:'one',3:'three'}
set(["one","two"])              #{'one','two'}





















''' == {2} strings == '''
# -------------------------------------------------------------
"""
There are two things to keep in mind for each of the data types you are using:

    Are they mutable?
    Are they ordered?

"""















''' == {3} print statement & user input & Boolean Logic== '''
# -------------------------------------------------------------

Input = input("Instructions:")  # ☝ input always returns a string, convert it to required 
                                # type

















''' == {4} Formatting == '''
# -------------------------------------------------------------

print("My name is {} and i\'m {} years old".format(name,years))
print(f"My name is {name} and i\'m {years} years old")

















''' == {5} Generic Operations on Containers == '''
# -------------------------------------------------------------

len(List)          # items count - works with sequences only not integers
min(Tuple) 
max(Tuple) 
sum(Tuple)
sorted(List)        # list in order from smallest to largest, leaving the list unchanged.
"apple" in List     # boolean, membership operator in (absence not in)
enumerate(List)     # {*} iterator on (index, value)
zip(Tuple,Tuple)    #{*} iterator on tuples containing ci items at same index
all(Tuple)          # returns True if any element of an iterable is True, else False
any(Tuple)          # True if at least one item of c evaluated true, else False
help(print)

"""
A method in Python behaves similarly to a function.
Methods actually are functions that are called using dot notation. 
"""



















''' == {5} Sequence Containers Indexing == '''
# -------------------------------------------------------------
lst=[10, 20, 30, 40, 50]

lst[:-1]        # [10,20,30,40]
lst[3:]         # [40,50]
lst[1:-1]       # [20,30,40]
lst[::2]        # [10,30,50] kolo + not etnen
lst[::-1]       # [50,40,30,20,10]  kolo + not wa7d + e3ks el list
lst[::-2]       # [50,30,10]    kolo + not etnen + e3ks el list
lst[:]          # [10,20,30,40,50]
lst[1:3]        # [20,30]
lst[::2]        # [10,30,50]
lst[-3:-1]      # [30,40]
lst[:3]         # [10,20,30]
lst[3:]         # [40,50]
lst[-1]         # 50
lst[0]          # 10

''' ************** Data Structures **************'''
"""
Data Structure 	Ordered 	Mutable     Constructor 	    Example
--------------------------------------------------------------------
Lionel Tamer Data Scientist(LTDS)

List 	        Yes 	    Yes 	    [ ] or list() 	    [5.7, 4, 'yes', 5.7]
Tuple 	        Yes 	    No 	        ( ) or tuple() 	    (5.7, 4, 'yes', 5.7)
Set 	        No 	        Yes 	    {}* or set() 	    {5.7, 4, 'yes'}
Dictionary 	    No 	        No** 	    { } or dict() 	    {'Jun': 75, 'Jul': 89}
"""






















''' == {5} Lists == '''
# Lists are mutable, ordered data structures.
# -------------------------------------------------------------

# Methods
# Adding elements
users.append('val')     # Adding an element to the end of the list
users.insert(0, 'joe')  # Inserting elements at a particular position

# Removing elements
del users[-1]           # Deleting an element by its position
users.remove('mia')     # Removing an item by its value

# sorting a list
users.sort()            # Sorting a list permanently - 3ks sorted(list)
users.sort(reverse=True) # Sorting a list permanently in reverse alphabetical order
sorted(users, reverse=True)  #Sorting a list temporarily
users.reverse()          # Reversing the order of a list

# join method
new_str = "\n".join(["fore", "aft", "starboard", "port"])  # takes a list of strings only as an argument

# Membership Operators {in , not in}
5 not in [1, 2, 3, 4, 6]


# iterating through a list
for bike in bikes: print(bike)
squares = [x**2 for x in range(1, 11) if x&2 == 0]  # List comprehensions(استيعاب الليست)


# Conditionals in List Comprehensions
# List comprehensions are not found in other languages, but are very common in Python.

squares = [x**2 for x in range(9) if x % 2 == 0]

# If you want to add an else
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]

















''' == {6} Tuples == '''
#  immutable ordered sequences of elements
# -------------------------------------------------------------

# Tuples can also be used to assign multiple variables in a compact way.
dimensions = 52, 40, 100 
length, width, height = dimensions      # tuple unpacking
print("The dimensions are {} x {} x {}".format(length, width, height))


# Looping through a tuple 
for dimension in dimensions: 
    print(dimension) 
    
#Overwriting a tuple 
dimensions = (800, 600) 
dimensions = (1200, 900)
















''' == {7} Dictionaries == '''
# A dictionary is a mutable not ordered data type that stores mappings of unique keys to values
# -------------------------------------------------------------
"""
allow you to connect pieces of related information stored as a key-value pairpair. 
When you provide a key, Python returns the value associated with that key.
You can loop through all the key-value pairs, all the keys, or all the values.
Key: Must be immutable(string, int, float, tuple)
"""
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

elements["lithium"] = 3   # insert "lithium" with a value of 3 into the dictionary
elements["helium"]        # print the value mapped to "helium"
elements.get("dilithium","return this words if None")   # returns None(or a default value of your choice) 
                                                        # if the key isn't found.


# Adding a key-value pair
alien_0['x'] = 0 
alien_0['y'] = 25 
alien_0['speed'] = 1.5

# Modifying values in a dictionary
alien_0['color'] = 'yellow' 
alien_0['points'] = 10

# Deleting a key-value pair
del alien_0['points']

# Storing dictionaries in a list
users = [ 
    { 'last': 'fermi',
     'first': 'enrico',
     'username': 'efermi', 
    }, 
    { 
        'last': 'curie',
        'first': 'marie',
        'username': 'mcurie',
    },
] 
# Show all information about each user. 
for user_dict in users: 
    for k, v in user_dict.items(): 
        print(k + ": " + v) 
    print("\n")

# Storing lists in a dictionary
# Store multiple languages for each person. 
fav_languages = {
     'jen': ['python', 'ruby'],
     'sarah': ['c'],
     'edward': ['ruby', 'go'], 
     'phil': ['python', 'haskell'], 
     } 
# Show all responses for each person. 
for name, langs in fav_languages.items(): 
    print(name + ": ") 
    for lang in langs: 
        print("- " + lang)

# Using an Ordered dict

from collections import OrderedDict
# Store each person's languages, keeping track of who responded first. 
fav_languages = OrderedDict() 
fav_languages['jen'] = ['python', 'ruby'] 
fav_languages['sarah'] = ['c'] 
fav_languages['edward'] = ['ruby', 'go'] 
fav_languages['phil'] = ['python', 'haskell'] 
# Display the results, in the same order they # were entered. 
for name, langs in fav_languages.items(): 
    print(name + ":")
    for lang in langs: 
        print("- " + lang)

# Compound Data Structures
elements =  {"hydrogen": {"number": 1,
                          "weight": 1.00794,
                          "symbol": 'H'},
               "helium": {"number": 2,
                          "weight": 4.002602,
                          "symbol": "He"}, 
               "oxygen": {"number": 8, 
                          "weight": 15.999, 
                          "symbol": "O"}}

# We can access elements in this nested dictionary like this.
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight



# Looping through all key-value pairs
fav_numbers = {'eric': 17, 'ever': 4}

for name, number in fav_numbers.items():
    print(name + ' loves ' + str(number))

# Looping through all keys
for name in fav_numbers.keys():
    print(name + ' loves a number')

# Looping through all values
for number in fav_numbers.values():
    print(str(number) + ' is a favorite')























''' == {7} Sets == '''
# A set is a data type for mutable unordered collections of{ unique elements}. 
# -------------------------------------------------------------

# remove duplicates from a list
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)

6 in unique_nums    # check for element
Set.update(Set2) 
Set.copy()
Set.add(9)      # add an element
Set.remove(2)
Set.discard(5) 
Set.clear()
Set.pop()       # remove a random element

# Methods like {union, intersection, and difference} are easy to perform with sets, 
# and are much faster than such operators with other containers.









# ************************************************************************
#*********************** هنا وقفت *****************************************














''' == {8} Functions == '''
# -------------------------------------------------------------
"""
Functions are named blocks of code, 
designed to do one specific job. 
Information passed to a function is called an argument, 
and information received by a function is called a parameter.
"""
# passing an argument
def greet_user(username): 
    """Display a personalized greeting.""" 
    print("Hello, " + username + "!") 
greet_user('jesse')

# Returning a value
def greet_user(username): 
    """Display a personalized greeting.""" 
    print("Hello, " + username + "!") 
greet_user('jesse')

# Default arguments
def cylinder_volume(height, radius=5):  # لو معوضتش عن قيمة الراديوس فهى هتتحط كديفولت بخمسة
    pi = 3.14159
    return height * pi * radius ** 2

cylinder_volume(10, 7)                  # the 7 will simply overwrite the default value of 5.


# Variable scoop(Local,Global)
"""
Variable scope refers to which parts of a program a variable can be referenced, or used, from.

It's important to consider scope when using variables in functions. 
If a variable is created inside a function, it can only be used within that function. 
Accessing it outside that function is not possible.

python doesn't allow functions to change the values of  global variables
"""
# This works fine
word = "hello"      # Global variable scoop

def some_function():
    print(word)     # Local variable scoop

some_function()


"""Documentation strings{Docstrings}"""
# Documentation is used to make your code easier to understand and use.
def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT: 
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area

""" Lambda Expression """
# lambda expressions to create anonymous functions. 
# That is, functions that don’t have a name. 
# They are helpful for creating quick functions that aren’t needed later in your code.
#  lambda expressions aren’t ideal for complex functions, 
# but can be very useful for short, simple functions.

multiply = lambda x, y: x * y   # (x+y) expression that is evaluated and returned in this function.
multiply(4, 7)



""" higher-order built-in function(function,iterable) --> return an iterator """

map(population_density,bikes)   # map() is a  that takes a function and iterable as inputs, 
                                # and returns an iterator that applies the function to each element 
                                # of the iterable.

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

"""def mean(num_list):
    return sum(num_list) / len(num_list)"""
mean = lambda num_list: sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)



filter()            # is a higher-order built-in function that takes 
                    # a function and iterable as inputs and returns an iterator 
                    # with the elements from the iterable for which the function returns True.

cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

"""def is_short(name):
    return len(name) < 10
"""
short_cities = list(filter(lambda name: len(name) < 10, cities))
print(short_cities)


"""  Iterators and Generators   """
# Iterables قابل للتكرار are objects that can return one of their elements at a time, such as a list.    
# iterator مكرر is an object that represents a stream of data.
# Generators صناع المكررات are a simple way to create iterators using functions.
        # Generators are a lazy way to build iterables
        
def my_range(x):
    i = 0
    while i < x:
        yield i     # instead of return
                    # This allows the function to return values one at a time, 
                    #and start where it left off each time it’s called.
        i += 1

for x in my_range(5):
    print(x)















''' == {9} Loops == '''
# -------------------------------------------------------------

''' = {9.1} for Loops = '''

""" 
A for loop iterates over a sequence of elements,
executing the body of the loop for each element in the sequence.

An iterable is an object that can return one of its elements at a time. 
This can include sequence types, such as strings, lists, and tuples, as well as non-sequence types,
 such as dictionaries and files.
"""

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)


range(start=0, stop=5, step=1)         # is a built-in function used to create an iterable sequence of numbers.


''' = {9.2} while Loops = '''
"""
A while loop repeats a block of code
as long as a certain condition is true.
"""

#Counting to 5 
current_number = 1 
while current_number <= 5: 
    print(current_number) 
    current_number += 1

current_value = 1           # initialize value
while current_value <= 5:   # condition
    print(current_value) 
    current_value += 1      # increment value


''' = Loops control = '''
"""
break --> exit the code
continue --> skip the current iteration if true
"""
banned_users = ['eve', 'fred', 'gary', 'helen'] 

prompt = "\nAdd a player to your team." 
prompt += "\nEnter 'quit' when you're done. " 

players = [] 
while True: 
    player = input(prompt) 
    if player == 'quit': 
        break 
    elif player in banned_users: 
        print(player + " is banned!") 
        continue 
    else: players.append(player) 
    
print("\nYour team:") 
for player in players: 
    print(player)



"""
Zip and Enumerate
"""
"""
zip returns list of Tuples
an iterator that combines multiple iterables into one sequence of tuples. 
Each tuple contains the elements in that position from all the iterables. 
For example, printing

list(zip(['a', 'b', 'c'], [1, 2, 3])) 
--> [('a', 1), ('b', 2), ('c', 3)]
"""
"""
enumerate is a built in function that returns an iterator of 
tuples containing indices and values of a list. 

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
"""
















''' == {11} if statements == '''
# -------------------------------------------------------------

# examine the current state of a program and respond appropriately to that state.
# statement block executed only if a condition is true
age = 25 
if age<=18 and age >=8:
    state="Kid"
elif age>65:
    state="Retired"
else:
    state="Active"

# In Python, indents conventionally come in multiples of four spaces. 

# Complex Boolean Expression
weight = 75 
height = 175
if 18.5 <= weight / height**2 < 25:
    print("BMI is considered 'normal'")


# Truth Value Testing
"""
Here are most of the built-in objects that are considered False in Python:

    constants defined to be false: None and False
    zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
    empty sequences and collections: '"", (), [], {}, set(), range(0)

"""









"""     Why Object-Oriented Programming?        """
"""
Object-oriented programming has a few benefits over procedural programming, 
which is the programming style you first learned.

    * Object-oriented programming allows you to create large, modular programs 
    that can easily expand over time.
    * Object-oriented programs hide implementation from the end-user


- When you train a machine learning algorithm with scikit-learn, 
you don't have to know anything about how the algorithm's code.
"""
# from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y) 
"""
How does scikit-learn train the SVM model? You don't need to know because the 
implementation is hidden with object-oriented programming. 
(Whether or not you SHOULD understand how SVM works is a different question).
"""

"""
Objects are defined by {{characteristics(Attributes) and actions(Methods)}}
    Characteristics and Actions in English Grammar
Another way to think about characteristics and actions is in terms of English grammar. 
{A characteristic would be a noun}. On the other hand, {an action would be a verb}.

Let's pick something from the real-world: {a dog.}
A few characteristics could be the dog's weight, color, breed, and height. These are all nouns. 
What actions would a dog take? A dog can bark, run, bite and eat. These are all verbs.
"""
# Class: Scientist - chancellor - Actor
# object: Stephen Hawkings - Angela Merkel - Brad Pitt
# Attribute: Height - Size - shape - Nationality
# Method: to speak - to do search - to lead
# Value: 160 - white - big

"""
=== Object-Oriented Programming (OOP) Vocabulary ====
    - class - a blueprint consisting of methods and attributes
    - object - an instance of a class. It can help to think of objects as something 
        in the real world like a yellow pencil, a small dog, a blue shirt, etc. 
        However, as you'll see later in the lesson, objects can be more abstract.
    - attribute - a descriptor or characteristic. Examples would be color, length, 
        size, etc. These attributes can take on specific values like blue, 3 inches, 
        large, etc.
    - method - an action that a class or object could take
    - OOP - a commonly used abbreviation for object-oriented programming
    - encapsulation - one of the fundamental ideas behind object-oriented programming is 
        called encapsulation: you can combine functions and data all into a single entity. 
        In object-oriented programming, this single entity is called a class. 
        Encapsulation allows you to hide implementation details much like 
        how the scikit-learn package hides the implementation of machine learning algorithms.

"""

"""
Function vs Method

A function and a method look very similar. They both use the def keyword. 
They also have inputs and return outputs. The difference is that 
{a method is inside of a class whereas a function is outside of a class}.
"""


""" What is self?   """
"""
# If you instantiate two objects, how does Python differentiate between these two objects?

shirt_one = Shirt('red', 'S', 'short-sleeve', 15)
short_two = Shirt('yellow', 'M', 'long-sleeve', 20)
# That's where self comes into play. If you call the change_price method on shirt_one, 
# how does Python know to change the price of shirt_one and not of shirt_two?

shirt_one.change_price(12)
# Behind the scenes, Python is calling the change_price method:

def change_price(self, new_price):

    self.price = new_price

Self tells Python where to look in the computer's memory for the shirt_one object. 
And then Python changes the price of the shirt_one object. When you 
call the change_price method, shirt_one.change_price(12), self is implicitly passed in.

The word self is just a convention. You could actually use any other name as 
long as you are consistent; however, you should always use self rather than some 
other word or else you might confuse people.
"""




















"""     Docstrings and Object-Oriented Code     """
class Pants:
    """The Pants class represents an article of clothing sold in a store
    """

    def __init__(self, color, waist_size, length, price):
        """Method for initializing a Pants object

        Args: 
            color (str)
            waist_size (int)
            length (int)
            price (float)

        Attributes:
            color (str): color of a pants object
            waist_size (str): waist size of a pants object
            length (str): length of a pants object
            price (float): price of a pants object
        """

        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

    def change_price(self, new_price):
        """The change_price method changes the price attribute of a pants object

        Args: 
            new_price (float): the new price of the pants object

        Returns: None

        """
        self.price = new_price

    def discount(self, percentage):
        """The discount method outputs a discounted price of a pants object

        Args:
            percentage (float): a decimal representing the amount to discount

        Returns:
            float: the discounted price
        """
        return self.price * (1 - percentage)






''' == {12} Classes == '''
# -------------------------------------------------------------
"""
A class defines the behavior of an object and the kind of information an object can store. 
The information in a class is stored in attributes, 
and functions that belong to a class are called methods. 
A child class inherits the attributes and methods from its parent class.
"""

# Creating a dog class
class Dog(): 
    """Represent a dog.""" 
    def __init__(self, name): 
        """Initialize dog object.""" 
        self.name = name 
    
    def sit(self): 
        """Simulate sitting.""" 
        print(self.name + " is sitting.") 

my_dog = Dog('Peso') 
print(my_dog.name + " is a great dog!") 
my_dog.sit()

# Inheritance
class SARDog(Dog): 
    """Represent a search dog.""" 
    def __init__(self, name): 
        """Initialize the sardog.""" 
        super().__init__(name) 
    
    def search(self): 
        """Simulate searching.""" 
        print(self.name + " is searching.") 

my_dog = SARDog('Willie') 
print(my_dog.name + " is a search dog.") 
my_dog.sit() 
my_dog.search()




















''' == {13} Syntax errors & Exceptions == '''
# -------------------------------------------------------------
"""
There are two kinds of errors in Python - syntax errors and exceptions. 
{Syntax errors} occur when you don't use correct syntax and 
Python doesn't know how to run your code. 
{Exceptions} occur when Python runs into unexpected situations 
while executing your code and can happen even if you used correct syntax.
"""

"""
Exceptions help you respond appropriately to errors that are likely to occur. 
You place code that might cause an error in the try block. 
Code that should run in response to an error goes in the except block. 
Code that should run only if the try block was successful goes in the else block.
"""

"""
BUILT-IN EXCEPTION

ValueError
AssertionError
IndexError
KeyError
TypeError

"""



#Catching an exception 
prompt = "How many tickets do you need? "
num_tickets = input(prompt) 
try: 
     num_tickets = int(num_tickets) 
except ValueError: 
    print("Please try again.") 
else: 
    print("Your tickets are printing.")


try:    # This is the only mandatory clause in a try statement.
    pass
except ValueError:      #  it catches the ValueError exception, but not other exceptions
    #  If Python runs into an exception while running the try block, 
    # it will jump to the except block that handles that exception.
    pass
except KeyboardInterrupt:   # we can include a parenthesized tuple after the except with the exceptions.
   pass
else:
    pass
finally:
    pass        # this code will run no matter what happens


# The party_planner
def party_planner(cookies, people):
    leftovers = None
    num_each = None

    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError as e:
        print("Oops, you entered 0 people will be attending.")
        print("Please enter a good number of people for a party.")
        print("ZeroDivisionError occurred: {}".format(e))
    return(num_each, leftovers)



































''' == {14} Working with files == '''
# -------------------------------------------------------------
"""
Your programs can read from files and write to files. Files
are opened in read mode ('r') by default, but can also be
opened in write mode ('w') and append mode ('a').
"""

# Reading a file and storing its lines 
filename = 'siddhartha.txt' 
with open(filename) as file_object: 
    lines = file_object.readlines() 

for line in lines: 
    print(line) 

# Writing to a file 
filename = 'journal.txt' 
with open(filename, 'w') as file_object: 
    file_object.write("I love programming.") 
    
# Appending to a file 
filename = 'journal.txt' 
with open(filename, 'a') as file_object: 
    file_object.write("\nI love making games.")



# I/O reading and writing from Udacity
"""     Reading and Writing Files        """

# Reading a File
f = open('my_path/my_file.txt', 'r')        # f is a file object and 'r' is the default type mode
file_data = f.read()                        # read is a method for returning a string from the file object
f.close()                                   # When finished with the file, use the close method 
                                            # to free up any system resources taken up by the file.


# Writing to a File
f = open('my_path/my_file.txt', 'w')        # ('w') mode. If the file does not exist, Python will create it for
                                            # you. 
                                            # If you open an existing file in writing mode, any content that it 
                                            # had contained previously will be deleted. If you're interested in 
                                            # adding to an existing file, without deleting its content, you should
                                            # use the append ('a') mode instead of write.
f.write("Hello there!")
f.close()



# With: Python provides a special syntax that {auto-closes} a file for you once you're finished using it.
with open('my_path/my_file.txt', 'r') as f: # This with keyword allows you to open a file, do operations on it,
                                            # and automatically close it after the indented code is executed,
                                            # in this case, reading from the file.
    
    file_data = f.read()                    # If you pass the read method an integer argument, it will read up to
                                            # that number of characters, output all of them, and keep the 'window'
                                            # at that position ready to read on.


f.readline()                                  # file method tells a program to go down to the next line.


"""         for line in file       """
# we can use this to create a list of lines in the file. Because each line still has its 
# newline character attached, I remove this using {.strip()}.

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)    # Outputs:      ["We're the knights of the round table", "We dance whenever we're able"]













''' == {15} RegEx == '''
# -------------------------------------------------------------

























''' == {16} Anaconda == '''
# conda: manage dependencies and isolate projects with support other languages than Python.
# -------------------------------------------------------------
"""
- Anaconda is an open source distribution for Python designed for large-scale data. 
    With Anaconda you will be able to simplify package management.
- It comes with conda, a package and environment manager. You'll be using conda 
    to create environments for isolating your projects that use different versions 
    of Python and/or different packages.

- You can install multiple packages at the same time. Something like 
conda install numpy scipy pandas
conda create -n my_env python=3.6 numpy pandas

- Conda also automatically {installs dependencies }for you. For example.
    {scipy depends on numpy}, it uses and requires numpy. If you install just scipy 
    {conda install scipy}, Conda will also install numpy if it isn't already installed.

- If you don't know the exact name of the package you're looking for, you can 
    try searching with 

conda search *search_term*         # conda search '*beautifulsoup*' هيرجعلك اسم الباكدج الصح
    e.g., I know I want to install Beautiful Soup, but I'm not sure of the exact package name.

### Managing environments
--------------------------
For example, {to create an environment named my_env and install numpy in it}, type 
conda create -n my_env numpy    # create my_env environment and install numpy in it
conda activate          # activate conda environment
conda deactivate        # deactivate conda environment


### Why we're using Python 3
-----------------------------
    - Jupyter is switching to Python 3 only
    - Python 2.7 is being retired
    - Python 3 has been out for almost 10 years, and there are very few dependencies.


### The main breakage between Python 2 and 3?
----------------------------------------------
    The place where your Python 2 code will fail most often is {the print statement}.

# Python 2
    print "Hello", "world!"

# In Python 2.6+
    from __future__ import print_function
    print("Hello", "world!")
    > Hello world!

# This was changed in Python 3 to a function.
    print("Hello", "world!")
    > Hello world!


### Why using conda?
--------------------

    -First, since Anaconda comes with a bunch of data science packages, you'll be 
        all set to start working with data. Secondly, using conda to manage your 
        packages and environments will reduce future issues dealing with the various 
        libraries you'll be using.

    - Package managers are used to install libraries and other software on your computer. 
        You’re probably already familiar with pip, it’s the default package manager 
        for Python libraries. Conda is similar to pip except that the available 
        packages are focused around data science while pip is for general use.
    
    - {conda} is not Python specific like {pip} is, it can also install non-Python packages.
        It is a package manager for any software stack.

"""























 
''' == {17} Jupyter notebooks == '''
# -------------------------------------------------------------
"""
The notebook is a web application that allows you to combine explanatory text, math equations, 
code, and visualizations all in one easily sharable document. 

Notebooks have quickly become an essential tool when working with data. You'll find them being 
    used for data cleaning and exploration, visualization, machine learning, 
    and big data analysis.


=== Headers ===
----------------
# Header 1
## Header 2
### Header 3


=== Links ===
----------------
Linking in Markdown is done by enclosing text in square brackets and the URL in parentheses, 
like this for a link to Udacity's home page.

[Udacity's home page](https://www.udacity.com) 
[I'm an inline-style link with title](https://www.google.com "Google's Homepage")


=== Emphasis ===
----------------

- You can add emphasis through bold or italics with asterisks or underscores (* or _).
    For italics, wrap the text in one asterisk or underscore, {_gelato_ or *gelato*} 
    renders as gelato(italic).

- Bold text uses {two} symbols, {**aardvark** or __aardvark__} 
    looks like aardvark(bold).

- Either asterisks or underscores are fine as long as you use the same symbol on both sides of the text.




=== Code ===
----------------
There are two different ways to display code, inline with text and as a code block separated 
from the text. To format inline code, 
(1) wrap the text in backticks. 
    For example, `string.punctuation`   الزرار اللى تحت الescape
                    renders as string.punctuation.

    To create a code block, start a new line and wrap the text in three backticks

```python
import requests
response = requests.get('https://www.udacity.com')
```



(2) or {indent each line of the code block with four spaces}.

    import requests
    response = requests.get('https://www.udacity.com')







=== Math expressions ===
----------------

You can create math expressions in Markdown cells using LaTeX symbols. 
Notebooks use MathJax to render the LaTeX symbols as math symbols. 
To start math mode, wrap the LaTeX in dollar signs $y = mx + b$ for inline math. 
For a math block, use double dollar signs,

$$
y = \frac{a}{b+c}
$$
    renders as (y=a/b+c)









=== Lists ===
----------------

(In this example, leading and trailing spaces are shown with with dots: ⋅)

1. First ordered list item
2. Another item

⋅⋅* Unordered sub-list. 
1. Actual numbers don't matter, just that it's a number
⋅⋅1. Ordered sub-list
4. And another item.

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks
- Or minuses
+ Or pluses







=== Images ===
---------------
Here's our logo (hover to see the title text):

Inline-style: 
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")






===Line Breaks===
------------------
My basic recommendation for learning how line breaks work is to experiment and discover -- 
{hit <Enter> once (i.e., insert one newline)}, then hit it twice (i.e., insert two newlines), 
see what happens. You'll soon learn to get what you want. "Markdown Toggle" is your friend.

Here are some things to try out:

Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.





=== Horizontal Rule ===
-----------------------
Three or more...

---

Hyphens

***

Asterisks

___

Underscores








=== Code and Syntax Highlighting ===
-------------------------------------
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```






=== Tables ===
---------------

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3






=== YouTube Videos ===
-------------

They can't be added directly but you can add an image with a link to the video like this:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>








=== Magic keywords ===
------------------------
Magic keywords are special commands you can run in cells that let you 
control the notebook itself or perform system calls such as changing directories. 
For example, you can set up matplotlib to work interactively in the notebook with %matplotlib.

Magic commands are preceded with one or two percent signs (% or %%)


== Timing code==
At some point, you'll probably spend some effort optimizing code to run faster. 
Timing how quickly your code runs is essential for this optimization. 
You can use the timeit magic command to time how long it takes for a function to run.


%timeit function call()
%%timeit            put it at the first line of code to print the code execution time
"""



































''' == {18} Libraries == '''
# -------------------------------------------------------------
"""
Using a main block
To avoid running executable statements in a script when it's imported as a module in another script, 
include these lines in an if __name__ == "__main__" block. Or alternatively, 
include them in a function called main() and call this in the if main block.

Whenever we run a script like this, Python actually sets a special built-in variable called __name__ 
for any module. When we run a script, Python recognizes this module as the main program, 
and sets the __name__ variable for this module to the string "__main__". 
For any modules that are imported in this script, 
this built-in __name__ variable is just set to the name of that module.
Therefore, the condition if __name__ == "__main__"is just checking whether this module is the main program.

"""

# The python Standard Library: https://pymotw.com/3/py-modindex.html#cap-m

# useful_functions.py ( An example of a library)

def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

if __name__ == '__main__':
    main()







# demo.py(python script)

# # import useful_functions as uf

# scores = [88, 92, 79, 93, 85]

# mean = uf.mean(scores)
# curved = uf.add_five(scores)

# mean_c = uf.mean(curved)

# print("Scores:", scores)
# print("Original Mean:", mean, " New Mean:", mean_c)

# print(__name__)
# print(uf.__name__)









"""
Our favorite modules

The Python Standard Library has a lot of modules! 
To help you get familiar with what's available, 
here are a selection of our favorite Python Standard Library modules and why we use them!

    csv:        very convenient for reading and writing csv files
    collections: useful extensions of the usual data types including OrderedDict, defaultdict and namedtuple
    random:     generates pseudo-random numbers, shuffles sequences randomly and chooses random items
    string:     more functions on strings. This module also contains useful collections of letters like 
                string.digits (a string containing all characters which are valid digits).
    re:         pattern-matching in strings via regular expressions
    math:       some standard mathematical functions
    os:         interacting with operating systems
    os.path:    submodule of os for manipulating path names
    sys:        work directly with the Python interpreter
    json:       good for reading and writing json files (good for web work)
"""




# Techniques for Importing Modules
    # There are other variants of import statements that are useful in different situations.

# To import an individual function or class from a module:
"""from module_name import object_name"""
# To import multiple individual objects from a module:
"""from module_name import first_object, second_object"""
# To rename a module:
"""import module_name as new_name"""
# To import an object from a module and rename it:
"""from module_name import object_name as new_name"""

import os.path      # {path} is a submodule of the {os} Package
os.path.isdir("scripting.py")



"""Third-Party Libraries """
# There are tens of thousands of third-party libraries written by independent developers! 
# You can install them using pip, a package manager that is included with Python 3. 
# pip is the standard package manager for Python, but it isn't the only one. 
# One popular alternative is Anaconda which is designed specifically for data science.


"""Using a requirements.txt File"""
# Larger Python programs might depend on dozens of third party packages. 
# To make it easier to share these programs, programmers often list a project's dependencies 
# in a file called requirements.txt. This is an example of a requirements.txt file.

"""
beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1
"""
# You can use pip to install all of a project's dependencies at once by typing 
# {pip install -r requirements.txt} in your command line.


# to be an effective programmer you also need to know what libraries are available 
# for you to use. People typically learn about useful new libraries from 
# online recommendations or from colleagues. If you're a new Python programmer 
# you may not have many colleagues, so to get you started here's a list of packages 
# that are popular with engineers at Udacity.
"""
IPython -  A better interactive Python interpreter
requests - Provides easy to use methods to make web requests. Useful for accessing web APIs.
Flask -    a lightweight framework for making web applications and APIs.
Django -   A more featureful framework for making web applications. Django is particularly good 
            for designing complex, content heavy, web applications.
Beautiful Soup - Used to parse HTML and extract information from it. Great for web scraping.
pytest -   extends Python's builtin assertions and unittest module.
PyYAML -   For reading and writing YAML files.
NumPy -    The fundamental package for scientific computing with Python. 
            It contains among other things a powerful N-dimensional array object and useful linear algebra capabilities.
pandas -   A library containing high-performance, data structures and data analysis tools. 
            In particular, pandas provides dataframes!
matplotlib-a 2D plotting library which produces publication quality figures in a variety 
                of hardcopy formats and interactive environments.
ggplot -   Another 2D plotting library, based on R's ggplot2 library.
Pillow -   The Python Imaging Library adds image processing capabilities to your Python interpreter.
pyglet -   A cross-platform application framework intended for game development.
Pygame -   A set of Python modules designed for writing games.
pytz -     World Timezone Definitions for Python
"""








''' = {16.1} NumPy = '''
"""
- NumPy stands for Numerical Python and it's a fundamental package for scientific 
    computing in Python. NumPy provides Python with an extensive math library 
    capable of performing numerical computations effectively and efficiently.

- Why should we use NumPy?
1- NumPy uses much less memory to store data
    The NumPy arrays takes significantly less amount of memory as compared to python lists. 
    It also provides a mechanism of specifying the data types of the contents, 
    which allows further optimization of the code.

2- One such feature is speed. When performing operations on large arrays NumPy can 
    often perform several orders of magnitude faster than Python lists. 




- At the core of NumPy is the ndarray, where nd stands for n-dimensional. 
    An ndarray is a multidimensional array of elements all of the same type. 
    In other words, an ndarray is a grid that can take on many shapes and can 
    hold either numbers or strings. In many Machine Learning problems you will 
    often find yourself using ndarrays in many different ways. 
    For instance, you might use an ndarray to hold the pixel values of an image 
    will be fed into a Neural Network for image classification.

"""
import numpy as np

"""
There are several ways to create ndarrays in NumPy. 
In the following lessons we will see two ways to create ndarrays:

    1- Using regular Python lists       np.array() 
    2-Using built-in NumPy functions
"""
# We import NumPy into Python
import numpy as np


# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])       

# Let's print the ndarray we just created using the print() command
print('x = ', x)            # x = [1 2 3 4 5]



"""
Let's pause for a second to introduce some useful terminology. We refer to 1D arrays as rank 1 arrays. 
    In general N-Dimensional arrays have rank N. Therefore, we refer to a 2D array as a rank 2 array. 
    Another important property of arrays is their shape. The shape of an array is the size along each of its dimensions. 
    For example, the shape of a rank 2 array will correspond to the number of rows and columns of the array. 
    As you will see, NumPy ndarrays have attributes that allow us to get information about them 
    in a very intuitive way. 
    For example, the shape of an ndarray can be obtained using the .shape attribute. 
    The shape attribute returns a tuple of N positive integers that specify the sizes of each dimension. 
    In the example below we will create a rank 1 array and learn how to obtain its shape, 
    its type, and the data-type (dtype) of its elements.
"""

# We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

# We print x
print()
print('x = ', x)
print()

# We print information about x
print('x has dimensions:', x.shape)     # (5,)
print('x is an object of type:', type(x))   # type: <class 'numpy.ndarray'>
print('The elements in x are of type:', x.dtype)    #  type: int32





# We create a rank 1 ndarray from a Python list that contains integers and strings
x = np.array([1, 2, 'World'])

# We print the ndarray

print('x = ', x)

# We print information about x
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)


"""
We can see that even though the Python list had mixed data types, the elements in x are all of the same type, 
namely, Unicode strings of 21 characters. We won't be using 
ndarrays with strings for the remaining of this introduction to NumPy, 
but it's important to remember that ndarrays can hold strings as well.
"""




''' == {16.1.1}  NumPy DataCamp == '''
# -------------------------------------------------------------
## NumPy DataCamp
"""
The NumPy library is the core library for scientific computing in
Python. It provides a high-performance multidimensional array
object, and tools for working with these arrays.
"""

## Creating Arrays
a = np.array([1,2,3])
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],dtype = float)





## Initial Placeholders
np.zeros((3,4))                      # Create an array of zeros
np.ones((2,3,4),dtype=np.int16)      # Create an array of ones
d = np.arrange(10,25,5)               # Create an array of evenly spaced values (step value)
np.linspace(0,2,9)                  #Create an array of evenly spaced values (number of samples)
e = np.full((2,2),7)                # Create a constant array
f = np.eye(2)                       # Create a 2X2 identity matrix
np.random.random((2,2))             # Create an array with random values
np.empty((3,2))                     # Create an empty array



## I/O ##

# Saving & Loading On Disk
np.save('my_array', a)
np.savez('array.npz', a, b)
np.load('my_array.npy')

# Saving & Loading Text Files
np.loadtxt("myfile.txt")
np.genfromtxt("my_file.csv", delimiter=',')
np.savetxt("myarray.txt", a, delimiter=" ")


## Data Types ##
np.int64        # Signed 64-bit integer types
np.float32      # Standard double-precision floating point
np.complex      # Complex numbers represented by 128 floats
np.bool         # Boolean type storing TRUE and FALSE values
np.object       # Python object type
np.string_      # Fixed-length string type
np.unicode_     # Fixed-length unicode type



## Inspecting Your Array ##
a.shape         # Array dimensions
len(a)          # Length of array
b.ndim          # Number of array dimensions
e.size          # Number of array elements
b.dtype         # Data type of array elements
b.dtype.name    # Name of data type
b.astype(int)   # Convert an array to a different type

np.info(np.ndarray.dtype)



## Array Mathematics ##

# Arithmetic Operations
np.subtract(a,b)        # Substraction
np.add(b,a)             # Addition
np.divide(a,b)          # Division
np.multiply(a,b)        # Multiplication
np.exp(b)               # Exponentiation
np.sqrt(b)              # Square root
np.sin(a)               # Print sines of an array
np.cos(b)               # Element-wise cosine
np.log(a)               # Element-wise natural logarithm
e.dot(f)                # Dot product


# Comparison
a == b                  # Element-wise comparison
a < 2                   # Element-wise comparison   array([True, False, False], dtype=bool)
np.array_equal(a, b)    # Array-wise comparison

# Aggregate Functions
a.sum()                 # Array-wise sum
a.min()                 # Array-wise minimum value
b.max(axis=0)           # Maximum value of an array row
b.cumsum(axis=1)        # Cumulative sum of the elements
a.mean()                # Mean
b.median()              # Median
a.corrcoef()            # Correlation coefficient
np.std(b)               # Standard deviation


## Copying Arrays ##
h = a.view()            # Create a view of the array with the same data
np.copy(a)              # Create a copy of the array
h = a.copy()            # Create a deep copy of the array

## Sorting Arrays ##
a.sort()            # Sort an array
c.sort(axis=0)      # Sort the elements of an array's axis




## Subsetting, Slicing, Indexing ##
# Subsetting
a[2]                    # Select the element at the 2nd index in 1D array
b[1,2]                  # Select the element at row 1 column 2
b[1][2]


# Slicing
a[0:2]                  # Select items at index 0 and 1
b[0:2,1]                # Select items at rows 0 and 1 in column 1
b[:1]                   # Select all items at row 0
b[0:1, :]
c[1,...]
a[ : :-1]               # Reversed array a 


# Boolean Indexing
a[a<2]                  # Select elements from a less than 2

#  Fancy Indexing
b[[1, 0, 1, 0],[0, 1, 2, 0]]        # Select elements (1,0),(0,1),(1,2) and (0,0)
b[[1, 0, 1, 0]][:,[0,1,2,0]]        # Select a subset of the matrix’s rows and matrix




## Array Manipulation ##
#  Transposing Array
i = np.transpose(b)                 # Permute array dimensions
i.T                                 # Permute array dimensions
# Changing Array Shape
b.ravel()                           # Flatten the array
g.reshape(3,-2)                     # Reshape, but don’t change data
# Adding/Removing Elements
h.resize((2,6))                     # Return a new array with shape (2,6)
np.append(h,g)                      # Append items to an array
np.insert(a, 1, 5)                  # Insert items in an array
np.delete(a,[1])                    # Delete items from an array
# Combining Arrays
np.concatenate((a,d),axis=0)        # Concatenate arrays
np.vstack((a,b))                    # Stack arrays vertically (row-wise)
np.r_[e,f]                          # Stack arrays vertically (row-wise)
np.hstack((e,f))                    # Stack arrays horizontally (column-wise)
np.column_stack((a,d))              # Create stacked column-wise arrays
np.c_[a,d]                          # Create stacked column-wise arrays

# Splitting Arrays
np.hsplit(a,3)                      # Split the array horizontally at the 3rd index
np.vsplit(c,2)                      # Split the array vertically at the 2nd index























''' = {16.3} MatplotLip = '''
"""
Data visualization involves exploring data through visual representations. 
The matplotlib package helps you make visually appealing representations of the data you’re working with. 
matplotlib is extremely flexible; these examples will help you get started with a few simple visualizations.
"""
# Line Graphs and Scatter Plots

# Making a line graph
import matplotlib.pyplot as plt 
x_values = [0, 1, 2, 3, 4, 5] 
squares = [0, 1, 4, 9, 16, 25] 
plt.plot(x_values, squares) 
plt.show()

# Making a scatter plot
import matplotlib.pyplot as plt 
x_values = list(range(1000)) 
squares = [x**2 for x in x_values] 
plt.scatter(x_values, squares, s=10) 
plt.show()




























''' == {17} Testing == '''
# -------------------------------------------------------------





























''' == {17} Additional Python resources == '''
# -------------------------------------------------------------

"""
 some of the most popular online interpreters and codepads.

    https://www.python.org/shell/
    https://www.onlinegdb.com/online_python_interpreter
    https://repl.it/languages/python3
    https://www.tutorialspoint.com/execute_python3_online.php
    https://rextester.com/l/python3_online_compiler
    https://trinket.io/python3
 Python articles:

    https://stackoverflow.blog/2017/09/06/incredible-growth-python/
    https://www.netguru.com/blog/why-python-is-growing-so-quickly-future-trends
    https://opensource.com/article/18/5/numbers-python-community-trends
    https://insights.stackoverflow.com/survey/2018#technology


"""

"""
How to Search - Here are some techniques for effective web searching:

1- Try using "Python" or the name of the library you're using as the first word of your query. 
2- This tells the search engine to prioritize results that are explicitly related to the tools you're using.
3- Writing a good search query can take multiple attempts. 
4- If you don't find helpful results on your first attempt, try again.
5- Try using keywords found on the pages you found in your initial search to direct the 
    search engine to better resources in the subsequent search.
6- Copy and paste error messages to use as search terms. This will lead you to explanations 
    of the error and potential causes. An error message might include references 
    to specific line numbers of code that you wrote. Only include the part of the error 
    message that comes before this in your search.
7- If you can't find an answer to your question, ask it yourself! Communities like 
    StackOverflow have etiquette rules you must learn if you want to participate, 
    but don't let this stop you from using these resources.

e.g. UnboundLocalError: local variable 'egg_count' referenced before assignment
        my search query should be: python UnboundLocalError: local variable
"""

"""
{Hierarchy of Online Resources}
While there are many online resources about programming, not all of the them are created equal. 
This list of resources is in approximate order of reliability.

    1- https://docs.python.org/3/tutorial/ - The Python Tutorial - This section of the 
        official documentation surveys Python's syntax and standard library. 
        It uses examples, and is written using less technical language than the main 
        documentation. Make sure you're reading the Python 3 version of the docs!

    2- https://docs.python.org/3/index.html - The Python Language and Library References - 
        The Language Reference and Library Reference are more technical than the tutorial, 
        but they are the definitive sources of truth. As you become increasingly 
        acquainted with Python you should use these resources more and more.
    3- http://stackoverflow.com/ - StackOverflow - This question and answer site has 
        a good amount of traffic, so it's likely that someone has asked 
        (and someone has answered) a related question before! However, 
        answers are provided by volunteers and vary in quality. Always understand 
        solutions before putting them into your program. One line answers without any 
        explanation are dubious. This is a good place to find out more about your 
        question or discover alternative search terms.
"""



"""
=========== Production Consultant  ===========

إستشارى إنتاج بإذن الله والنية صافية لله ولخدمة الاسلام عن طريق التعلم والتعليم المستمرين واظهار صورة العرب والمسلمين كأفراد مثقفون 
ومتعلمون أفوى العلوم، وان شاء الله دة يحسن الصورة النمطية عن الاسلام ويجعل غير المسلمين يهتمو بدراسة هذا الدين الذى يتمتع اصحابه بالبحث الدائم والخلق الحسن
* وان شاء الله ناوى اكتفى بمبلغ يقضى حاجتى والباقى هطلعو لوجه الله وف حب الله 
الحمدلله دائماً وأبداً ^ ^

{Digital Manufacturing and Design Technology DMD}
    1- UB DMD Professional Certificate                                                      [ 1 out of 9 ]
    2- AutoDesk CAD, CAM and CNC Manufacturing Professional Certificate                     [ 0 out of 4 ]
    3- TUM Six Sigma & Lean Production Professional Certificate                             [ 0 out of 3 ]

    4- Related but not program courses:
        4.1- Introduction to Computer Numerical Control
        4.2- A Hands-on Introduction to Engineering Simulations
        4.3- Mathematical Modelling Basics
        4.4- The Mechatronics Revolution: Fundamentals and Core Concepts
        4.5- Fundamentals of Manufacturing Processes
    5- KTHx Risk Management of Work Related Injuries using RAMP Professional Certificate    [ 0 out of 3 ]
    6- NHCPS Basic Life Support Certified + CPR, AED & First Aid Certificate                [ 0 out of 2 ]
    7- MIT Principle of Manufacturing MicroMasters                                          [ 0 out of 8 ]


{Opeartions Management}
    1- MIT Supply chain Management MicroMasters                                             [ 0 out of 5 ]
    2- Macquarie Excel Skills for Business Professional Certificate                         [ 0 out of 4 ]
    3- PMI PMP Certified
    4- Related but not program courses:
        4.1- Enterprise Systems
        4.2- Project Management for life



{Information Technology}
    1- Google IT Automation Professional Certificate                                        [ 0 out of 4 ]
    2- AI Programming Nanodegree
    3- Data Science Nanodegree

{ Language skills}
    1- English -->                                  Ielts 8.5 [ Speaking 8.5, Reading 9, Listening 9, Writing 8]
    2- Deutsch -->                                                                          Goethe Institut B2






[[[[    1st Stage   1 week next Tue]]]]
    
    
    Introduction to Computer Numerical Control
    A Hands-on Introduction to Engineering Simulations
    The Mechatronics Revolution: Fundamentals and Core Concepts
    Deutsch

    Mathematical Modelling Basics
    Macquarie Excel Skills for Business Professional Certificate    [ 1 ]
    Deutsch

    AI Programming Nanodegree
    Google IT Automation Professional Certificate                   [ 1 ]
    Deutsch

[[[[    2nd Stage   ]]]]

    AutoDesk CAD, CAM and CNC Manufacturing Professional Certificate        [ 1 ]
    TUM Six Sigma & Lean Production Professional Certificate                [ 2 ]
    Fundamentals of Manufacturing Processes
    Macquarie Excel Skills for Business Professional Certificate            [ 1 ]
    Enterprise Systems
"""