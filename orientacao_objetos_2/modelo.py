class Filme:
    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.__ano = ano
        self.duracao = duracao
        self.__likes = 0


    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @property
    def ano(self):
        return self.__ano

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    def dar_likes(self):
        self.__likes += 1



class Serie:
    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.__ano = ano
        self.temporadas = temporadas
        self.__likes = 0


    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()
    
    @property
    def ano(self):
        return self.__ano

    def dar_likes(self):
        self.__likes += 1



vingadores = Filme('vingadores - Guerra Infinita', 2018, 160)
vingadores.dar_likes()

print(f"Nome: {vingadores.nome} \nAno: {vingadores.ano} \nDuração: {vingadores.duracao} \nLikes: {vingadores.likes}")



atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()

atlanta.dar_likes()
print(f"Nome: {atlanta.nome} \nAno: {atlanta.ano} \nTemporadas: {atlanta.temporadas} \nLikes: {atlanta.likes}")
