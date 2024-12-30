# Converting hexadecimal to other bases
def hexadecimal_to_binary(num):
    # Convert hexadecimal string to decimal
    decimal_value = int(num, 16)
    # Convert decimal to binary
    binary_value = bin(decimal_value)[2:]
    # Print result
    print(f"Converting {num} from hexadecimal to binary...")
    print(f"Result: {binary_value}")

def hexadecimal_to_decimal(num):
    # Convert hexadecimal string to decimal
    decimal_value = int(num, 16)
    # Print result
    print(f"Converting {num} from hexadecimal to decimal...")
    print(f"Result: {decimal_value}")

def hexadecimal_to_octal(num):
    # Convert hexadecimal string to decimal
    decimal_value = int(num, 16)
    # Convert decimal to octal
    octal_value = oct(decimal_value)[2:]
    # Print result
    print(f"Converting {num} from hexadecimal to octal...")
    print(f"Result: {octal_value}")