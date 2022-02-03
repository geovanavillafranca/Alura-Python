class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    
    
    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome


    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()

    def dar_likes(self):
        self._likes += 1

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self._nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self._likes = 0



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self._nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self._likes = 0



vingadores = Filme('vingadores - Guerra Infinita', 2018, 160)
vingadores.dar_likes()

print(f"Nome: {vingadores.nome} \nAno: {vingadores.ano} \nDuração: {vingadores.duracao} \nLikes: {vingadores.likes}")



atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()

atlanta.dar_likes()
print(f"Nome: {atlanta.nome} \nAno: {atlanta.ano} \nTemporadas: {atlanta.temporadas} \nLikes: {atlanta.likes}")
