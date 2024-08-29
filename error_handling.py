# Error Handling
# ==============
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always run.")
