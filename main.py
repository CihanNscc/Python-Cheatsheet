# Phython Cheatsheet
# ==================

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
print("a = ", a)


# Mutable Types
# =============
# list
# dict
# set

num_list = [1, 2, 3]
second_num_list = num_list  # "second_num_list" references the same list as "num_list"
second_num_list.append(4)

print(
    "num_list = ", num_list
)  # "num_list" is now [1, 2, 3, 4] because "second_num_list" is a reference
