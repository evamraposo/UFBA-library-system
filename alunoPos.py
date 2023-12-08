from usuario import Usuario
from emprestimoAluno import EmprestimoAluno
from devolverLivro import DevolverLivro

class AlunoPosGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.qtd_emprestimos = 4
        self.data_devolucao = 4

    def exibir_informacoes(self):
        return f"Aluno de Pós-Graduação: {self.nome}, Código: {self.codigo}"
    
    def emprestimo(self, livro):
        emp = EmprestimoAluno()
        return emp.emprestimo_aluno(self, livro)
    
    def devolucao(self, emprestimo):
        devolver = DevolverLivro()
        self.qtd_emprestimos += 1
        return devolver.devolver_livro(emprestimo, self)
        