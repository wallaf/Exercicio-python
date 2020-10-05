#3 Faça um programa para solicitar o nome e as duas notas de um aluno. Calcular sua média e informá-la. Se ela for inferior a 7, escrever "Reprovado”; caso contrário escrever "Aprovado".

nome = input('Qual o nome do Aluno? ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'o aluno {nome} foi aprovado')
if media < 7 :
    print(f'o aluno {nome} foi reprovado')
print(f'Sua media foi {media}')