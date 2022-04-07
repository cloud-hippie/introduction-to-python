# Homework

The idea behind Test Driven Development is to write tests first, then write code that passes the tests.

## Setup

1. Create a new repository called `tdd-homework` and clone it to your computer.

2. Create a virtual enviorment called `tdd-homework` and activate its virtual environment. Checkout the [docs](https://docs.python.org/3/library/venv.html) for more information on virtual environments. There are also some open source packages that can be used to create virtual environments. Poetry, pipenv, and virtualenv are some of them.

2. Create a new file called `README.md` in the root of the repository.

3. Write a brief description of the project in the `README.md` file.

4. Create a folder called `challeneges` and a folder called `tests`.

5. Add a new file called `test_challenges.py` to the `tests` folder.

6. Add a new file called `challenges.py` to the `challenges` folder.

7. Import the functiosn from `lists.py` file into the `test_lists.py` file. You may need to use a `__init__.py` file to make sure the functions are imported.

## Assignment

Write a test and a function that will pass the test for the following:

1. A function that takes two strings and returns a list of the characters that are in both strings.
2. A function that takes a list and returns a new list with all the duplicates removed.
3. A function that takes a string and a delimiter and returns a list of the string split by the delimiter.
4. A function that takes a list and a delimiter and returns a string with the list items joined by the delimiter.
5. A function that takes a `dict` and a string and returns the value of the object's attribute with the name of the string. It returns `None` if not found.
6. A function that takes a list of dictionaries and a key and returns a list of the values for that key in each dictionary.
7. A function that takes a list of dictionaries and a key and returns the list of dicts SORTED BY the key. If the key is not found in the dictionary, the item should be at the end of the list.




