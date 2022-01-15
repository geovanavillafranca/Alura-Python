
def jogar():

    print('*********************************')
    print('***Bem-vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "python"
    letras_acertadas = []
    enforcou = False
    acertou = False
    contador = 0
    letras_erradas = []

    for v in range(len(palavra_secreta)):
        letras_acertadas.append('_') 

    print(letras_acertadas)

    errou = len(palavra_secreta)
    # enquanto nao enforcou e nao acertou
    while not enforcou and not acertou:

        chute = input('Qual letra? ').strip()

        index = 0
        if chute not in palavra_secreta:
            letras_erradas.append(chute)
            errou -= 1
            if errou == 0:
                print('Você se enforcou!')
                enforcou = True
            print(f"Seus chutes: {letras_erradas}")
        elif chute in letras_acertadas:
            print('Você já chutou essa letra.')

        else:

            for letra in palavra_secreta:

                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                    contador += 1
                    if contador == len(palavra_secreta):
                        print('Parabéns! Você acertou a palavra secreta!')
                        acertou = True

                index += 1

            print(letras_acertadas)

    print('Fim do jogo')

if __name__ == '__main__':
    jogar()
