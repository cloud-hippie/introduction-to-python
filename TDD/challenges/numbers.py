# Write a function that takes a number and tells you if it is odd or even.
def is_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

# Write a function that takes in a number and returns the factorial of that number.
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)







