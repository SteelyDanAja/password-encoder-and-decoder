def menu():
    print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
    print()

def encode(inputted_password):
    encoded_password = ''
    for char in inputted_password:
        if int(char) > 6:
            if char == '7':
                encoded_password += '0'
            if char == '8':
                encoded_password += '1'
            if char == '9':
                encoded_password += '2'
        else:
            char = int(char) + 3
            encoded_password += str(char)
    return encoded_password


def decode(encoded_password):
    decoded_password = ''

    for digit in encoded_password:
        if digit == '2':
            decoded_digit = '9'
        elif digit == '1':
            decoded_digit = '8'
        elif digit == '0':
            decoded_digit = '7'
        else:
            decoded_digit = int(digit) - 3

        decoded_password += str(decoded_digit)

    return decoded_password


def main():
    program_on = True
    while program_on == True:
        menu()
        option = input('Please enter an option:')
        if option == '1':
            inputted_password = input('Please enter your password to encode:')
            encoded_password = encode(inputted_password)
            print('Your password has been encoded and stored!')
            pass
        if option == '2':
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        if option == '3':
            program_on = False


while __name__ == "__main__":
    main()