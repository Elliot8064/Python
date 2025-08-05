radar = int(input("intruduza a que velocidade passou um radar"))

if radar >80:
    x = radar -80
    resultado = x * 2
    print(f'estás acima do limite permitido. a multa foigerada no valor de {resultado} euros')
if radar <80:
    print("dentro do limite. boa viagem")