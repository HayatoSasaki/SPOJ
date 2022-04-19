# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

def alphabet_position(text):
    text = list(text.strip("").upper())
    text_ = []
    for x in range(len(text)):
        if text[x].isalpha():
                text_.append(str(ord(text[x]) - 64))
    return " ".join(text_)