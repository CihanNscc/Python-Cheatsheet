# List Comprehension
# ==================
# example 1
x = [i for i in range(10)]

# example 2 (2D list comprehension)
x = [[i for i in range(10)] for j in range(10)]

# example 3 (conditional list comprehension)
x = [i for i in range(10) if i % 2 == 0]
