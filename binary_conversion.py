#this function will convert the user's decimal number to binary
def decimalToBinary(num):
    """This function converts decimal number
    to binary and prints it"""
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')

