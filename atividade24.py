# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

num = 0
cont = 0
while True:
    usu = float(input("Digite um numero ou -1 para parar "))
    if usu == -1:
        break
    num += usu
    cont += 1
    if cont > 0:
        media = num/cont

print (f"{media}")