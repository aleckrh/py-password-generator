import random

numbers = '0123456789'
alphaUppercase = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
alphaLowercase = 'abcdefghijklmnñopqrstuvwxyz'
symbols = '!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

defaultLength = 10

x = random.randint(0,3)

if x == 0:
    char = alphaLowercase + numbers + alphaUppercase + symbols
elif x==1:
    char = alphaLowercase + symbols + numbers + alphaUppercase
elif x==2:
    char = symbols + alphaUppercase + alphaLowercase + numbers
else:
    char = numbers + alphaLowercase + alphaUppercase + symbols

def generatePassword(length):
    password = ''

    for c in range(length):
        password += random.choice(char)

    return password

 
# length = input("¿De que tamaño quieres la contraseña? ")

# length = int(length)

# print (generatePassword(length))

print (generatePassword(defaultLength))

# for x in range(10):
#     print (generatePassword(defaultLength))