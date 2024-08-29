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
