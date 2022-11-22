from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

restart = True


def caesar(message, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position % 30]
        else:
            end_text += char
    result = f"The {cipher_direction}d text is {end_text}"
    print(result)


print(logo)

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message=text, shift_amount=shift, cipher_direction=direction)

    result = input("Do you wanna restart again ?")
    if result == "no":
        restart = False
        print("GoodBye")



