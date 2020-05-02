import string
import random

# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# print (string.printable)

defaultLength = 10

def generatePassword(length):
	password = ''
	
	for n in range(length):
		x = random.randint(0,94)
		password += string.printable[x]
	
	return password

# length = input("¿De que tamaño quieres la contraseña? ")

# length = int(length)

# print (generatePassword(length))

print (generatePassword(defaultLength))

# for x in range(10):
#     print (generatePassword(defaultLength))