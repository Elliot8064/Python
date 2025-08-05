
nota1 = int (input("intruduza a primeira nota"))
nota2 = int (input("intruduza a segunda nota"))

media = (nota1 + nota2)/2

if media <50:
  print ("estás reprovado!")
if media > 50 and media < 70:
  print ("é satisfaz!")
if media >=70:
  print ("é bom!")