# Write a program in python that:
# 1. converts binary to decimal, octal and hexadecimal
# 2. converts octal to binary, decimal and hexadecimal
# 3. converts decimal to binary, octal and hexadecimal
# 4. converts hexadecimal to binary, octal and decimal

# Import conversion functions
from from_binary import *
from from_octal import *
from from_decimal import *
from from_hex import *

# Import checker functions
from check_number_base import *

# Import error printing functions
from errors import *

# Describe to the user how to use the program
print("Welcome to number base converter! \n"
      "Reference: \n"
      "Enter 'bin' for binary\n"
      "Enter 'oct' for octal\n"
      "Enter 'dec' for decimal\n"
      "Enter 'hex' for hexadecimal\n")


# Define the available number bases
number_bases = ["bin", "oct", "dec", "hex"]

# Get user to input a number
number = input("Enter number: ")

# Get user to select base of inputted number
convert_from = input("Convert from: ")

# Input must be valid
while convert_from not in number_bases:
    print_invalid_entry_error()
    convert_from = input("Convert from: ")


# Get user to input desired number base
convert_to = input("Convert to: ")

# Input must be valid
while convert_to not in number_bases:
    print_invalid_entry_error()
    convert_to = input("Convert to: ")
    

# Input must not be the same as in convert_from
while convert_to == convert_from:
    print_same_as_from_error()
    convert_to = input("Convert to: ")


# Note: always verify that the number entered is actually of the
# base specified in convert_from

# Run functions to convert binary to other bases
if convert_from == "bin":
    if is_binary_string(number):
        if convert_to == "oct":
            binary_to_octal(number)
        elif convert_to == "dec":
            binary_to_decimal(number)
        elif convert_to == "hex":
            binary_to_hexadecimal(number)
    else:
        print_wrong_base_error(number, "binary")

# Run functions to convert octal to other bases
elif convert_from == "oct":
    if is_octal_string(number):
        if convert_to == "bin":
            octal_to_binary(number)
        elif convert_to == "dec":
            octal_to_decimal(number)
        elif convert_to == "hex":
            octal_to_hexadecimal(number)
    else:
        print_wrong_base_error(number, "octal")

# Run functions to convert decimal to other bases
elif convert_from == "dec":
    if is_decimal_string(number):
        if convert_to == "bin":
            decimal_to_binary(number)
        elif convert_to == "oct":
            decimal_to_octal(number)
        elif convert_to == "hex":
            decimal_to_hexadecimal(number)
    else:
        print_wrong_base_error(number, "decimal")

# Run functions to convert hexadecimal to other bases
elif convert_from == "hex":
    if is_hexadecimal_string(number):
        if convert_to == "bin":
            hexadecimal_to_binary(number)
        elif convert_to == "oct":
            hexadecimal_to_octal(number)
        elif convert_to == "dec":
            hexadecimal_to_decimal(number)
    else:
        print_wrong_base_error(number, "hexadecimal")