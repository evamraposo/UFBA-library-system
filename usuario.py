class Usuario:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

class AlunoGraduacao(Usuario):
    def exibir_informacoes(self):
        return f"Aluno de Graduação: {self.nome}, Código: {self.codigo}"

class AlunoPosGraduacao(Usuario):
    def exibir_informacoes(self):
        return f"Aluno de Pós-Graduação: {self.nome}, Código: {self.codigo}"

class Professor(Usuario):
    def exibir_informacoes(self):
        return f"Professor: {self.nome}, Código: {self.codigo}"
