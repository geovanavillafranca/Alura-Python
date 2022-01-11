print('*********************************')
print('Bem-vindo ao jogo de adivinhação!')
print('*********************************')

tentativas = 3
rodada = 1

while (tentativas > 0):
    print(f'Tentativa {rodada} de {tentativas}')

    numero_secreto = 42

    chute_str = int(input('Digite o seu número: '))
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto

    print('Você digitou', chute)

    if (acertou):
        print('Você acertou')
        break

    else:

        if (maior):
            print('Seu chute foi muito alto')
        
        else:
            print('Seu chute foi muito baixo')

    rodada += 1
    tentativas -= 1
print('Fim de jogo')
