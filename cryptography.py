import string

alphabet = list(string.ascii_lowercase)

def encode(text:string, shift):
    enc_msg = ''
    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
            enc_msg += alphabet[index - shift]
        else:
            enc_msg += char 
               
    return enc_msg    
                
def decode(text, shift):
    dec_msg = ''
    for char in text:
        if char.isalpha():
            index = alphabet.index(char)
            dec_msg += alphabet[index - (26 - shift)]
        else:
            dec_msg += char 
               
    return dec_msg     

direction = input("type 'encode' to encrypt 'decode' to decrypt\n").lower()
text = input("type the message:\n").lower()
shift = int(input("type the shift number:\n"))



if direction == 'encode':
    enc_message = encode(text=text, shift=shift)
    print(enc_message)
elif direction == 'decode':
    dec_message =  decode(text=text, shift=shift)
    print(dec_message)

else:
    print("Wrong input please try again!")


