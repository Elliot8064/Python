nota_500=0
nota_200=0
nota_100=0
nota_50=0
nota_20=0
nota_10=0
nota_5=0
ding = int (input("insere quanto dinheiro queres levantar"))

if ding % 5 !=0:
    print ("não é possivel fazer a operação. por favor tente mais tarde.")
    exit()
else:
    while ding != 0:
        if ding > 500:
            ding = ding - 500
            nota_500= nota_500 +1
        elif ding >= 200:
            ding = ding -200
            nota_200 = nota_200 + 1
        elif ding >= 100:
            ding = ding - 100
            nota_100 = nota_100 + 1
        elif ding >= 50:
            ding = ding - 50
            nota_50= nota_50 +1
        elif ding >= 20:
            ding = ding - 20
            nota_20= nota_20 +1
        elif ding >= 10:
            ding = ding - 10
            nota_10= nota_10 +1
        elif ding >= 5:
            ding = ding - 5
            nota_5= nota_5 +1

print (f'foi necessário {nota_500} notas de 500, { nota_200} notas de 200, { nota_100} notas de 100, { nota_50} notas de 50, { nota_20} notas de 20 , { nota_10} notas de 10 e { nota_5} notas de 5 ')