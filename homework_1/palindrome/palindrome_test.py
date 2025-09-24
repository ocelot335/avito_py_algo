from palindrome import is_palindrome


def test_positive_odd_digits_palindrome():
    assert is_palindrome(121) is True


def test_positive_even_digits_palindrome():
    assert is_palindrome(1221) is True


def test_positive_non_palindrome():
    assert is_palindrome(31) is False
    assert is_palindrome(123) is False


def test_single_digit_number():
    assert is_palindrome(7) is True


def test_large_palindrome():
    assert is_palindrome(1234567654321) is True


def test_number_ending_in_zero():
    assert is_palindrome(10) is False
    assert is_palindrome(120) is False
