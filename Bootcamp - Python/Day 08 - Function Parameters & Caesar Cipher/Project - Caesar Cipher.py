# Version Based in CODEWARS ROT13 problem. 
# Should probably do the alph-list version.

def encrypt(message, shift): 
    message = list(message)

    for x in range(len(message)):
        if ord(message[x]) >= 65 and ord(message[x]) <= 122:
            if ord(message[x]) <= 90:
                y = ord(message[x])+shift
                if y > 90:
                    y -= 26
                message[x] = chr(y)
            elif ord(message[x]) >= 97:
                y = ord(message[x])+shift
                if y > 122:
                    y -= 26
                message[x] = chr(y)
    
    return "".join(message)

def decrypt(message, shift):
    message = list(message)

    for x in range(len(message)):
        if ord(message[x]) >= 65 and ord(message[x]) <= 122:
            if ord(message[x]) <= 90:
                y = ord(message[x])-shift
                if y < 65:
                    y += 26
                message[x] = chr(y)
            elif ord(message[x]) >= 97:
                y = ord(message[x])-shift
                if y < 97:
                    y += 26
                message[x] = chr(y)
    
    return "".join(message)

while True:
    caesar = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if caesar == 'encode' or caesar == 'decode':
        if caesar == 'encode':
            print(encrypt(input("Type your message:\n"), int(input("Type the shift number:\n"))))
        elif caesar == 'decode':
            print(decrypt(input("Type your message:\n"), int(input("Type the shift number:\n"))))
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if again != 'yes':
            break