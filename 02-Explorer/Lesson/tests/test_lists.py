from imp import lock_held
from TDD.challenges.lists import is_in_list, longest_string_in_list


def test_is_in_list():
    """
    This function checks if a value is in a list.
    """
    assert is_in_list(1, [1, 2, 3]) == True
    assert is_in_list(4, [1, 2, 3]) == False


def test_longest_string_in_list():
    assert longest_string_in_list(["one", "two", "three"]) == "three"
    assert longest_string_in_list(["four", "five", "six"])  == "five"


