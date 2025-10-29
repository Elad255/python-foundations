
from utils.strings import is_palindrome

def test_basic_palindromes():
    assert is_palindrome("A man, a plan, a canal: Panama!")
    assert is_palindrome("RaceCar")
    assert not is_palindrome("hello")

def test_numbers_and_mixed():
    assert is_palindrome("12321")
    assert not is_palindrome("123210")
