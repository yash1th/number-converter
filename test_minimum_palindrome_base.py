import pytest
from smallest_palindrome_base import minimum_palindrome_base

def test_error_codes():
    '''testing for error codes'''
    assert minimum_palindrome_base(47) == -1
    assert minimum_palindrome_base(1001) == -2

def test_minimum_value():
    '''testing for the minimum base value when a number is passed'''
    assert minimum_palindrome_base(15) == 2
    assert minimum_palindrome_base(100) == 3
    assert minimum_palindrome_base(174) == 28
