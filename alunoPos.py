from usuario import Usuario
from emprestimoAluno import EmprestimoAluno
from devolverLivro import DevolverLivro

class AlunoPosGraduacao(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.qtd_emprestimos = 4
        self.data_devolucao = 4

    def exibir_informacoes(self):
        tipo_usuario = 'Aluno de Pós-Graduação:'
        super().exibir_informacoes(tipo_usuario)
    
    def emprestimo(self, livro):
        emp = EmprestimoAluno()
        return emp.emprestimo_aluno(self, livro)
    
    def devolucao(self, emprestimo):
        devolver = DevolverLivro()
        self.qtd_emprestimos += 1
        return devolver.devolver_livro(emprestimo, self)
        