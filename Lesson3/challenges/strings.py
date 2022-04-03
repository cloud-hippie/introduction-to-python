# Write a function that takes in a name and returns the amount of vowels in the name.
def count_vowels(name):
    count = 0
    for i in name:
        if i in "aeiou":
            count += 1
    return count


# Write a function that takes a string and tells you if it is a palindrome.
def is_palindrome(string):
    if len(string) == 0:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return is_palindrome(string[1:-1])


# Write a function that take a string and reverses it.
def reverse_string(string):
    if len(string) == 0:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

