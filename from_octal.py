# Converting octal to other bases
def octal_to_binary(num):
    # Convert octal string to decimal
    decimal_value = int(num, 8)
    # Convert decimal to binary
    binary_value = bin(decimal_value)[2:]
    # Print result
    print(f"Converting {num} from octal to binary...")
    print(f"Result: {binary_value}")

def octal_to_decimal(num):
    # Convert octal string to decimal
    decimal_value = int(num, 8)
    # Print result
    print(f"Converting {num} from octal to decimal...")
    print(f"Result: {decimal_value}")

def octal_to_hexadecimal(num):
    # Convert octal string to decimal
    decimal_value = int(num, 8)
    # Convert decimal to hexadecimal
    hexadecimal_value = hex(decimal_value)[2:]
    # Print result
    print(f"Converting {num} from octal to hexadecimal...")
    print(f"Result: {hexadecimal_value}")