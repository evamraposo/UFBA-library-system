from usuario import Usuario
from emprestimoLivro import EmprestarLivro
from verificarReserva import VerificarReserva
from devolverLivro import DevolverLivro

class Professor(Usuario):
    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)
        self.data_devolucao = 7
        self.notificacoes = []
        self.qtd_notificacoes = len(self.notificacoes)
        
    def exibir_informacoes(self):
        return f"Professor: {self.nome}, Código: {self.codigo}"
    
    def emprestimo(self, livro):
        emp = EmprestarLivro()
        verifica = VerificarReserva()

        verifica.verificar_reserva(self, livro)
        return emp.emprestimo_livro(self, livro)
    
    def devolucao(self, emprestimo):
        devolver = DevolverLivro()

        return devolver.devolver_livro(emprestimo, self)