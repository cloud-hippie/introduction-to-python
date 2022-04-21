import pytest

from TDD.challenges.numbers import is_odd, factorial


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, "odd"),
        (2, "even"),
        (3, "odd"),
        (4, "even"),
        (5, "odd"),
        (6, "even"),
        (7, "odd"),
        (8, "even"),
        (9, "odd"),
        (10, "even"),
    ],
)
def test_is_odd(number, expected):
    assert is_odd(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320),
        (9, 362880),
        (10, 3628800),
    ],
)
def test_factorial(number, expected):
    assert factorial(number) == expected
