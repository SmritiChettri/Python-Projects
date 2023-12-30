import random
import string
import secrets
alphabets = string.ascii_letters
digits = string.digits
special_char = string.punctuation
pass_value = alphabets + digits +special_char
pass_len = int(input("Enter the length of the password: "))
password = ""
for i in range(pass_len):
    password += "".join(secrets.choice(pass_value))
print(f"Your password is {password}" )