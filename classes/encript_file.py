from classes.encrypt import Encrypt
import os


class EncryptFile:
    def __init__(self, text):
        self.text = text

    def encrypt(self):
        encrypt_text = ""
        for i in self.text:
            encrypt_char = Encrypt(i).encrypt()
            encrypt_text += encrypt_char

        return encrypt_text

    def encrypt_file(self, file):
        with open(file, "a") as file:
            file.write(self.encrypt())





