'''
Python Challenge(Palindromic Numbers)

Write a Python prgram determines the smallest base (greater than or equal to 2)
in which the first 1000 positive decimal integers are palindromes. Please include
unit test for any function you write.
'''
import sys
import csv


error_codes = {'-1':'cannot find palindrome under base 38',
                '-2': 'number should be less than 1001'}

def is_palindrome(number):
    ''' Checks a String, returns if it is a palindrome or not
    args:
        number
    returns:
        a bool value whether the palindrome is true or not
    '''
    #return number[:].strip().upper() == number[::-1].strip().upper()
    return number[:].strip().upper() == number[::-1].strip().upper()


def number_to_base(number, base):
    '''Convert a decimal number from base 2 to base 37 inclusive
    args:
        number, base
    returns:
        a string with the converted number
    '''
    if base not in range(0,38):
        sys.exit('base should be in between 0 and 37')
    base_string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYVZ'
    if number < base:
        return base_string[number]
    else:
        q, r = divmod(number, base)
        return ''.join((number_to_base(q, base), base_string[r]))


def minimum_palindrome_base(number):
    '''finds the minimum base of a number in which it is a palindrome
    args:
        number
    returns:
        -minimum base of number in which it is palindrome
        - -1 when no palindrome number can be found
        - -2 when the number that a palindrome need to be found is greater than 1000
    '''
    if number<1001:
        for base in range(2, 38):
            converted_number = number_to_base(number, base)
            if is_palindrome(converted_number):
                return base
        return -1
    return -2


if __name__ == '__main__':
    with open('log.csv','w') as Output:
        OutputWriter = csv.writer(Output, delimiter = ',', quotechar = '"', quoting=csv.QUOTE_NONNUMERIC)
        OutputWriter.writerow(['decimal','smallest base in which the number is a palindrome'])
        for number in range(1, 1001):
            minimum_palindrome = minimum_palindrome_base(number)
            base = error_codes.get(str(minimum_palindrome), minimum_palindrome)
            OutputWriter.writerow([number,base])
