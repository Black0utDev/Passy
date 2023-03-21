import random, time
from colorama import Fore as F, init

init()

char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"£$%^&*()@~#/<>/.,[]'

pass_length = int(input('[+] Password Length: '))

pass_word = []

for i in range(pass_length):
    randomchar = random.choice(char_set)
    pass_word.append(randomchar)

print("")
print(f'{F.WHITE}[{F.GREEN}+{F.WHITE}] {F.GREEN}' + "".join(pass_word))
input("")