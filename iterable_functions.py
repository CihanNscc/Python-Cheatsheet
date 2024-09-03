# Iterable Functions
# =====================
# map
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

capitalized_fruits = map(lambda x: x.capitalize(), fruits)
print(list(capitalized_fruits))


# filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))


# enumerate
names = ["John", "Tim", "Michael", "Sarah"]

indexed_names = list(enumerate(names))
print(indexed_names)


# zip
names = ["John", "Tim", "Michael", "Sarah", "Jessica"]
ages = [27, 31, 22, 38, 29]
owns_pets = [True, False, True, False, True]

combined = list(zip(names, ages, owns_pets))
print(combined)