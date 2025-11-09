class Encrypt:
    def __init__(self,  char):
        self.char = char

    def check(self):
        try:
            int(self.char)
        except:
            raise "you need put a letter"

    def encrypt(self):
        if self.char.isupper():
            return chr(155 - ord(self.char))
        elif self.char.islower():
            return chr(219 - ord(self.char))
        return self.char


