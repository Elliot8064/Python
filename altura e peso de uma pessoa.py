altura = float(input("insere quanto medes"))
peso   = float(input("insere quanto pesas"))

imc = peso / (altura ** 2)

if imc < 18.5:
    print (f' tens {imc} de IMC portanto, estás abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print (f' tens {imc} de IMC portanto , parabéns! tens o peso ideal')
elif 25 <= imc < 30:
    print (f'tens {imc} de IMC portanto , estás acima do peso ideal')
else:
    print ("isso não é real. tente de novo")