# Converting decimal to other bases
def decimal_to_binary(num):
    # Convert decimal to binary
    binary_value = bin(int(num))[2:]
    # Print result
    print(f"Converting {num} from decimal to binary...")
    print(f"Result: {binary_value}")

def decimal_to_octal(num):
    # Convert decimal to octal
    octal_value = oct(int(num))[2:]
    # Print result
    print(f"Converting {num} from decimal to octal...")
    print(f"Result: {octal_value}")

def decimal_to_hexadecimal(num):
    # Convert decimal to hexadecimal
    hexadecimal_value = hex(int(num))[2:]
    # Print result
    print(f"Converting {num} from decimal to hexadecimal...")
    print(f"Result: {hexadecimal_value}")

