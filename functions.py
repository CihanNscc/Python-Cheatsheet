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
