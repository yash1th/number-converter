import pytest
from smallest_palindrome_base import number_to_base

def test_base_not_in_range():
    '''testing for system exception when the base is not in between 2 and 38'''
    with pytest.raises(SystemExit) as e:
        number_to_base(100, 38)
    assert e.type == SystemExit
    assert 'base should be in between 0 and 37' in str(e.value)

def test_return_type():
    '''testing for return type when a number and base are passed'''
    assert type(number_to_base(10,5)) == str

def test_result():
    '''testing for the result when number and the appropriate are passed'''
    assert number_to_base(5,5) == '10'
    assert number_to_base(5,10) == '5'
    assert number_to_base(10,5) == '20'
    assert number_to_base(1000,37) == 'R1'
