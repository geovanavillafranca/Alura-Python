
def jogar():

    print('*********************************')
    print('***Bem-vindo ao jogo de Forca!***')
    print('*********************************')

    palavra_secreta = "python"
    letras_acertadas = []
    for v in range(len(palavra_secreta)):
        letras_acertadas.append('_') 

    print(letras_acertadas)

    enforcou = False
    acertou = False
    contador = 0
    errou = len(palavra_secreta)
    letras_erradas = []
    # enquanto nao enforcou e nao acertou
    while not enforcou and not acertou:

        chute = input('Qual letra? ').strip()

        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra


        

            index += 1
        print(letras_acertadas)

if __name__ == '__main__':
    jogar()
