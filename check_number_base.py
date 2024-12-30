# Functions to check the number base
def is_binary_string(num):
    return all(char in '01' for char in num)

def is_octal_string(num):
    return all(char in '01234567' for char in num)

def is_decimal_string(num):
    return num.isdigit()

def is_hexadecimal_string(num):
    return all(char in '0123456789abcdefABCDEF' for char in num)