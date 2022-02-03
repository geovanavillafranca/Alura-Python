class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.likes = 0

    def dar_likes(self):
        self.likes += 1



class Serie:
    def __init__(self, nome, ano, temporadas):
        self.nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.likes = 0

    def dar_likes(self):
        self.likes += 1



vingadores = Filme('vingadores - Guerra Infinita', 2018, 160)
vingadores.dar_likes()

print(f"Nome: {vingadores.nome} \nAno: {vingadores.ano} \nDuração: {vingadores.duracao} \nLikes: {vingadores.likes}")



atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_likes()

atlanta.dar_likes()
print(f"Nome: {atlanta.nome} \nAno: {atlanta.ano} \nTemporadas: {atlanta.temporadas} \nLikes: {atlanta.likes}")
