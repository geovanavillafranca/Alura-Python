from random import randint

print('*********************************')
print('Bem-vindo ao jogo de adivinhação!')
print('*********************************')

tentativas = 0
numero_secreto = randint(1, 100)

print('Qual o nícel de dificuldade?')
print('(1) Fácil (2) Médio (3) Difícil')

nivel = int(input('Digite o nível: '))

pontos = 1000

if nivel == 1:
    tentativas = 15
elif nivel == 2:
    tentativas = 10
elif nivel == 3:
    tentativas = 5

for rodada in range(1, tentativas + 1):
    print(f'Tentativa {rodada} de {tentativas}')


    chute_str = int(input('Digite um número entre 1 e 100: '))
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto

    print('Você digitou', chute)

    if chute > 100 or chute < 1:
        print('Você deve digitar um número entre 1 e 100!')

    else:
        if (acertou):
            print(f'Você acertou e fez {pontos} pontos!')
            break

        else:

            if (maior):
                print('Seu chute foi muito alto')
            
            else:
                print('Seu chute foi muito baixo')

            pontos_perdidos = abs(numero_secreto - chute) # ex: num_sec= 30 e chute= 10 | 30 - 10 = 20 pont_perdidos
            pontos -= pontos_perdidos


print('Fim de jogo')
