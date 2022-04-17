# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet.
# Create a function that takes a string and returns the string ciphered with Rot13. 
# If there are numbers or special characters included in the string, they should be returned as they are. 
# Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

def rot13(message): 
    message = list(message)

    for x in range(len(message)):
        if ord(message[x]) >= 65 and ord(message[x]) <= 122:
            if ord(message[x]) <= 90:
                y = ord(message[x])+13
                if y > 90:
                    y -= 26
                message[x] = chr(y)
            elif ord(message[x]) >= 97:
                y = ord(message[x])+13
                if y > 122:
                    y -= 26
                message[x] = chr(y)
    
    return "".join(message)
