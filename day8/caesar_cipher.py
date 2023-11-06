from caesar_logo import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]


def caesar(direction_to_code, text_to_code, shift_amount):
    shift_amount %= 26
    coded_text = ""
    if direction_to_code == "decode":
        shift_amount = shift_amount * -1
    for char in text_to_code:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            coded_text += alphabet[new_position]
        else:
            coded_text += char
    return f"The {direction_to_code}d text is {coded_text}"


print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n>>> ").strip().lower()
    text = input("Type your message:\n>>> ").strip().lower()
    shift = int(input("Type the shift number:\n>>> ").strip())
    print(caesar(direction_to_code=direction, text_to_code=text, shift_amount=shift))
    should_want = input("Type (yes) if you want to continue otherwise no: ").strip().lower()
    if should_want == "no":
        print("GoodBye!")
        break
