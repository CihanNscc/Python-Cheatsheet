# Phython Cheatsheet
# ==================
# ==================


# Basic Syntax
# ============
# Comment
# print("Hello, World!")

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

# Conditional Switch
match a:
    case 1:
        print("a is 1")
    case 2:
        print("a is 2")
    case _:
        print("a is neither 1 nor 2")

# Conditional Ternary
a = 1 if a == 1 else 0


# Immutable Types
# ===============
# str
# int
# float
# bool
# bytes
# tuple

a = 2
b = a  # "b" is assigned the value of "a"
b = 3

# "a" is still 2, because "b" is a separate variable
print("a = ", a)  # a = 2


# Mutable Types
# =============
# list
# dict
# set

num_list = [1, 2, 3]
second_num_list = num_list  # "second_num_list" references the same list as "num_list"
second_num_list.append(4)

# "num_list" is now [1, 2, 3, 4] because "second_num_list" is a reference
print("num_list = ", num_list)  # num_list = [1, 2, 3, 4]
