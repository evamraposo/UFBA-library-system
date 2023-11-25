class Usuario:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.emprestimos = []

class AlunoGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.qtd_emprestimos = 3

    def exibir_informacoes(self):
        return f"Aluno de Graduação: {self.nome}, Código: {self.codigo}"

class AlunoPosGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.qtd_emprestimos = 4

    def exibir_informacoes(self):
        return f"Aluno de Pós-Graduação: {self.nome}, Código: {self.codigo}"

class Professor(Usuario):
    def exibir_informacoes(self):
        return f"Professor: {self.nome}, Código: {self.codigo}"
