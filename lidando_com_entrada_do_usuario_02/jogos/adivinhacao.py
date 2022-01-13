from random import randint

print('*********************************')
print('Bem-vindo ao jogo de adivinhação!')
print('*********************************')

tentativas = 3
numero_secreto = randint(1, 100)

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
            print('Você acertou!!')
            break

        else:

            if (maior):
                print('Seu chute foi muito alto')
            
            else:
                print('Seu chute foi muito baixo')


print('Fim de jogo')
