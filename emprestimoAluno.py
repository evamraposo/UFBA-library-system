from emprestimoLivro import EmprestarLivro
from verificarReserva import VerificarReserva

class EmprestimoAluno(EmprestarLivro):


    def emprestimo_aluno(self, usuario, livro):
        verifica = VerificarReserva()
        if usuario.qtd_emprestimos == 0:
            return "Usuário atingiu a quantidade máxima de empréstimos"
        
        reserva = verifica.verificar_reserva(usuario, livro)
        if reserva == False:
            verifica.limite_exemplares_reservados(livro)
        
        usuario.qtd_emprestimos -= 1
        return super().emprestimo_livro(usuario, livro)
        
