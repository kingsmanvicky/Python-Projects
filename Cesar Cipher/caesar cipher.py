import logo


#Creating the function to do the encryption and decryption
def caesar(start_text,shift_amount,cipher_direction):
    end_text =""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d message is: {end_text}")



#Printing this at start to get inputs from user and calling the function
print(logo.logo)
should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    caesar(start_text=text, shift_amount=shift,cipher_direction=direction)
    reply = input("Type 'yes' if you want to run again or Type 'no' to exit:\n")
    if reply == "no" :
        should_continue = False
        print("Exiting project.....")