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

def main():
    program_on = True
    while program_on == True:
        menu()
        option = input('Please enter an option:')
        if option == '1':
            inputted_password = input('Please enter your password to encode:')
            print('Your password has been encoded and stored!')
            pass
        if option == '2':
            pass
        if option == '3':
            program_on = False
