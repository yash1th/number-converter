import pytest
from smallest_palindrome_base import is_palindrome

def test_single_character():
    '''testing a single character is a palindrome or not'''
    assert is_palindrome('1') == True
    assert is_palindrome('a') == True
    assert is_palindrome('A') == True

def test_empty_string():
    '''testing for an empty string'''
    assert is_palindrome('') == True

def test_whitespace_string():
    '''testing for whitespace in string'''
    assert is_palindrome('     ') == True
    assert is_palindrome('a  a  ') == True
    assert is_palindrome('a   a  a  ') == False

def test_palindrome():
    '''testing when it is a palindrome'''
    assert is_palindrome('12321') == True
    assert is_palindrome('abcba') == True
    assert is_palindrome('ABCBA') == True
    assert is_palindrome('AB232BA') == True
    assert is_palindrome('ab232ba') == True
    assert is_palindrome('Ab232Ba') == True

def test_not_palindrome():
    '''testing when it is not a palindrome'''
    assert is_palindrome('179') == False
    assert is_palindrome('abc') == False
    assert is_palindrome('XYZ') == False
    assert is_palindrome('AB23BA') == False
    assert is_palindrome('ab23yz') == False
    assert is_palindrome('Ya23Pk') == False

def test_return_type():
    '''testing return type of a palindrome'''
    assert type(is_palindrome('123')) == bool
