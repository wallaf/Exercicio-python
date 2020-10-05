#2 Elabore um programa para solicitar o nome de uma equipe de futebol, a quantidade de derrotas, empates e vitórias
# obtidas por ela no campeonato. No futebol, cada vitória vale três pontos e cada empate vale um ponto. Calcular e
# informar: a quantidade de pontos ganhos, a quantidade de pontos perdidos e o percentual de aproveitamento da equipe

vitoria = int(input('Digite o número de jogos vitoriosos: '))
empate = int(input('Digite o número de empates: '))
derrota = int(input('Digite o número de derrotas: '))
jogos = vitoria + empate + derrota
pontos_ganhos = vitoria*3
perdidos = derrota*3 + empate*2
print(f'O time jogou {jogos} jogos e obteve {pontos_ganhos} pontos e teve {perdidos} pontos peridos')
