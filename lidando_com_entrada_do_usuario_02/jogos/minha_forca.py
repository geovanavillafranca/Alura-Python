def jogar():

    print('*********************************')
    print('***Bem-vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "python".upper()
    letras_acertadas = []
    enforcou = False
    acertou = False
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
            desenha_forca(erros)
        elif chute in letras_acertadas:
            print('Você já chutou essa letra.')

        else:

            for letra in palavra_secreta:

                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                    if "_" not in letras_acertadas:
                        imprime_mensagem_vencedor
                        acertou = True

                index += 1
            print(letras_acertadas)
        
        enforcou = erros == 6
        if enforcou:
            imprime_mensagem_perdedor(palavra_secreta)


    print('Fim do jogo')


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()





if __name__ == '__main__':
    jogar()
