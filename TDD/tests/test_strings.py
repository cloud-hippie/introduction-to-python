import pytest
from TDD.challenges.strings import count_vowels, is_palindrome, reverse_string

@pytest.mark.parametrize(
    "name, expected",
    [
        ("", 0),
        ("a", 1),
        ("ab", 1),
        ("abcde", 2)
    ],
)
def test_count_vowels(name, expected):
    assert count_vowels(name) == expected
    

@pytest.mark.parametrize(
    "string, expected",
    [
        ("", True),
        ("a", True),
        ("ab", False),
        ("abcde", False),
        ("abcba", True)
    ],
)
def test_is_palindrome(string, expected):
    assert is_palindrome(string) == expected

@pytest.mark.parametrize(
    "string, expected",
    [
        ("", ""),
        ("a", "a"),
        ("ab", "ba"),
        ("abcde", "edcba")
    ],
)
def test_reverse_string(string, expected):
    assert reverse_string(string) == expected
    
