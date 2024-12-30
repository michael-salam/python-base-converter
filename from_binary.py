# Converting binary to other bases
def binary_to_octal(num):
    # Convert binary string to decimal
    decimal_value = int(num, 2)
    # Convert decimal to octal
    octal_value = oct(decimal_value)[2:]
    # Print result
    print(f"Converting {num} from binary to octal...")
    print(f"Result: {octal_value}")

def binary_to_decimal(num):
    # Convert binary string to decimal
    decimal_value = int(num, 2)
    # Print result
    print(f"Converting {num} from binary to decimal...")
    print(f"Result: {decimal_value}")

def binary_to_hexadecimal(num):
    # Convert binary string to decimal
    decimal_value = int(num, 2)
    # Convert decimal to hexadecimal
    hexadecimal_value = hex(decimal_value)[2:]
    # Print result
    print(f"Converting {num} from binary to hexadecimal...")
    print(f"Result: {hexadecimal_value}")