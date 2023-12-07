
class DevolverLivro:

    def devolver_livro(self, emprestimo, usuario):
        # Verifique se o empréstimo está na lista de empréstimos ativos
        if emprestimo in usuario.emprestimos:
            # Processa a devolução

            emprestimo.livro.exemplares_disponiveis += 1
            usuario.emprestimos.remove(emprestimo)
            
            return f"Livro '{emprestimo.livro.titulo}' devolvido com sucesso."
        
        else:
            return "Empréstimo não encontrado."