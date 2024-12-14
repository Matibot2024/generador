import random
longitud = int(input("Hagamos una contraseña, ingresa la longitud(no mas de 10):"))
password = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
x = ""
for i in range(longitud):
    y = random.choice(password)
    x += y
print(x)