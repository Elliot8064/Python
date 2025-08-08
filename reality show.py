ana = 0
bruno= 0
carla=0
print("bem vindo á votação")
print ("Ana: tecla 1 ")
print ("Bruno: tecla 2 ")
print ("Carla: tecla 3 ")
print ("finalizar votação: tecla 0 ")

while True:
    voto = int(input("insira o seu voto aqui"))
    if voto == 1:
        ana = ana + 1
    elif voto == 2:
        bruno = bruno + 1
    elif voto == 3:
        carla = carla + 1
    elif voto == 0:
        break

print (f'a ana teve {ana}, o bruno teve {bruno} e a carla teve {carla}')
if ana > bruno and carla:
    print ("ana ganhou")
if bruno > ana  and carla:
        print("bruno ganhou")
if carla > bruno and ana:
            print("carla ganhou")

