
from palindrome import is_palindrome


def test_palindrome():
    assert is_palindrome("madam") == True


def test_non_palindrome():
    assert is_palindrome("hello") == False


def test_single_character():
    assert is_palindrome("a") == True


def test_palindrome_with_uppercase():
    assert is_palindrome("level".lower()) == True


def test_empty_string():
    assert is_palindrome("") == True
