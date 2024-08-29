# PYTHON CHEATSHEET
# ==================

# Basic Syntax
# ============
# Comment
# This is a one line comment

# docstring
def example_function():
    """
    This function does nothing but serves as an example
    of a docstring, which is a string literal used to
    document modules, classes, methods, or functions.
    """
    pass


# Variable
a = 1


# Function
def add(a, b):
    return a + b


# Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Loop
for i in range(10):
    print(i)

# Conditional If-Else
if a == 1:
    print("a is 1")
elif a == 2:
    print("a is 2")
else:
    print("a is neither 1 nor 2")

# Structural Pattern Matching (introduced in Python 3.10)
match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case _:
        print("a is neither 1 nor 2")

# Ternary conditional operator
a = 1 if a == 1 else 0


# Immutable Types
# ===============
# str, int, float, bool, bytes, tuple

a = 2
b = a  # "b" is assigned the value of "a"
b = 3

# "a" is still 2 because "b" is a separate variable
print("a = ", a)  # a = 2


# Mutable Types
# =============
# list, dict, set

num_list = [1, 2, 3]
second_num_list = num_list  # "second_num_list" references the same list as "num_list"
second_num_list.append(4)

# "num_list" is now [1, 2, 3, 4] because "second_num_list" is a reference
print("num_list = ", num_list)  # num_list = [1, 2, 3, 4]


# List Comprehension
# ==================
# example 1
x = [i for i in range(10)]

# example 2 (2D list comprehension)
x = [[i for i in range(10)] for j in range(10)]

# example 3 (conditional list comprehension)
x = [i for i in range(10) if i % 2 == 0]


# Function Argument & Parameter Types
# ===================================
# Positional
def subtract(a, b):
    return a - b


subtract(2, 1)  # 2 is a, 1 is b

# Keyword
subtract(b=2, a=1)  # 1 is a, 2 is b


# Default
def subtract(a, b=1):
    return a - b


subtract(2)  # 2 is a, 1 is b by default


# Optional
def print_stuff(a, b=1, c=None):
    print(a, b, c)


print_stuff(1, 2)  # c is optional


# Variable-Length Arguments
def print_any_number_of_stuff(*args):
    print(args)


print_any_number_of_stuff(1, 2, 3)  # (1, 2, 3) is args


# Keyword Arguments
def print_any_number_of_stuff(**kwargs):
    print(kwargs)


print_any_number_of_stuff(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3} is kwargs


# Combining Variable-Length and Keyword Arguments
def sample_function(a, b, c=True, d=False):
    print(a, b, c, d)


sample_function(*[1, 2], **{"c": "hello", "d": "world"})


# Error Handling
# ==============
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always run.")
