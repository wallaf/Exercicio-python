#5.    Crie um programa que leia a altura de 10 pessoas. Ao final o programa deve informar o total de pessoas cadastradas,
# a quantidade de pessoas com altura inferior a 1,60 metros; a quantidade de pessoas com altura entre 1,60 metros
# e 1,80 metros e a quantidade de pessoas com altura superior a 1,80 metros.

menor160 = maior180 = entre160e180 = 0

for calc in range(10):
    altura = float(input(f'Digite a altura da {calc + 1}º pessoa: '))

    if altura < 1.60:
        menor160 += 1
    elif altura > 1.80:
        maior180 += 1
    elif 1.60 < altura < 1.80:
        entre160e180 += 1

print(f'Menores ou iguais a 1.60 foram {menor160}')
print(f'Maiores ou iguais a 1.80 foram {maior180}')
print(f'Entre 1.60 e 1.80 foram {entre160e180}')
