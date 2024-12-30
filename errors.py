# Functions for printing errors
def print_invalid_entry_error():
    print("Invalid entry. Please try again.\n"
          "Reference: \n"
          "Enter 'bin' for binary\n"
          "Enter 'oct' for octal\n"
          "Enter 'dec' for decimal\n"
          "Enter 'hex' for hexadecimal\n")

def print_same_as_from_error():
    print("You cannot convert to the same number base you are converting from. Please try again.\n"
          "Reference: \n"
          "Enter 'bin' for binary\n"
          "Enter 'oct' for octal\n"
          "Enter 'dec' for decimal\n"
          "Enter 'hex' for hexadecimal\n")

def print_wrong_base_error(value, base):
    print(f"{value} is not a valid {base} number. Please try again")