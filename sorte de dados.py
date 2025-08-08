from random import randint
dado1=1
dado2 =2
resultado = 0
while dado1 != dado2:
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    resultado = resultado + 1

print (f'demorou {resultado} vezes para girar os 2 dados iguais')