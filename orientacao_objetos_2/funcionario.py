class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')
    
    def mostrar_tarefas(self):
        print('Fer muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')
    
    def buscar_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')


    def  busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum.')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass


luan = Senior('Luan')
print(luan)


# print('Junior')
# jose = Junior()
# jose.mostrar_tarefas()
# jose.busca_perguntas_sem_resposta()

# print('Pleno')
# luan = Pleno()
# luan.buscar_cursos_do_mes()
# luan.busca_perguntas_sem_resposta()
# luan.mostrar_tarefas()







