class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.a = alphabet
        self.k = key
    
    def encode(self, text):
        return "".join([self.a[(self.a.find(letter) + self.a.find(self.k[index % len(self.k)])) % len(self.a)] if letter in self.a else letter for index,letter in enumerate(text)])
    
    def decode(self, text):
        return "".join([self.a[(self.a.find(letter) - self.a.find(self.k[index % len(self.k)])) % len(self.a)] if letter in self.a else letter for index,letter in enumerate(text)])
