# Some Basic Functions
# ====================
# len
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(len(fruits))


# sum, max, min
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(numbers, start=15))
print(max(numbers))
print(min(numbers))

# round
number = 3.14159265358979323846

print(round(number, 2))


# sorted
people = [
    {"name": "John", "age": 27},
    {"name": "Tim", "age": 31},
    {"name": "Michael", "age": 22},
    {"name": "Sarah", "age": 38},
]

sorted_people = sorted(people, key=lambda x: x["age"], reverse=True)
print(sorted_people)


# open
with open("example.txt", "r") as file:
    text = file.read()

    print(text)
