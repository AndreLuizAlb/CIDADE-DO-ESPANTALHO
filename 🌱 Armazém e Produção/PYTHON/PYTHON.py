import random

#Coleta de dados
ht = int(input('Horas trabalhadas: '))
tc = int(input('Tempo de coleta em segundos: '))
cc = int(input('Chance de coleta (0 a 100): '))

#horas para segundos
htCompleta = ht * 3600

#Calculo do total de tentativas de coleta
tentativas = htCompleta // tc  

coletado = 0

for i in range(tentativas):
    chance = random.randint(1, 100)
    if chance <= cc:  
        coletado += 1  # Coletou

print(f'Total coletado: {coletado}')
