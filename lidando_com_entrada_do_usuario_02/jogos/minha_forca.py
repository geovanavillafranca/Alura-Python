def jogar():

    print('*********************************')
    print('***Bem-vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "python".upper()
    letras_acertadas = []
    enforcou = False
    acertou = False
    contador = 0
    letras_erradas = []

    for v in range(len(palavra_secreta)):
        letras_acertadas.append('_') 

    print(letras_acertadas)

    erros = 0
    # enquanto nao enforcou e nao acertou
    while not enforcou and not acertou:

        chute = input('Qual letra? ').strip().upper()

        index = 0
        if chute not in palavra_secreta:
            letras_erradas.append(chute)
            erros += 1
                
            print(f"Seus chutes: {letras_erradas}")
        elif chute in letras_acertadas:
            print('Você já chutou essa letra.')

        else:

            for letra in palavra_secreta:

                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                    if "_" not in letras_acertadas:
                        print('Parabéns! Você acertou a palavra secreta!')
                        acertou = True

                index += 1
            print(letras_acertadas)
        
        enforcou = erros == 6
        if enforcou:
            print('Você perdeu!')


    print('Fim do jogo')

if __name__ == '__main__':
    jogar()
