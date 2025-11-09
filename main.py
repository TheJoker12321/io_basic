from classes.encript_file import EncryptFile




message = input("print some message: ")
EncryptFile(message).encrypt_file("secret.txt")
with open("secret.txt") as f:
    f = f.read()
    print("before the encrypt:")
    print(f)
    print("after the encrypt:")
    print(EncryptFile(f).encrypt())


