#4 Faça um programa que leia dois números e mostre qual o maior dos dois. O programa deve informar caso sejam iguais.

n1 = float(input('Digite o primeiro número : '))
n2 = float(input('Digite o segundo número : '))
if n1 > n2:
    print(f'O número {n1} é maior que {n2}')
if n2 > n1:
    print(f'O número {n2} é maior que {n1}')
else:
    print(f'Os números {n1} {n2} são iguais')