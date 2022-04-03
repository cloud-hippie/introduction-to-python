from distutils.util import check_environ
from Lesson3.challenges.strings import count_vowels


def test_vowel_count():
    assert count_vowels("hello") == 2

