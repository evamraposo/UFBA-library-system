from emprestimo import Emprestimo

class EmprestarLivro:

    def emprestimo_livro(self, usuario, livro):
            
            devedor = next((u for u in usuario.emprestimos if u.verificar_atraso() == True), None)

            if devedor:
                return "O empréstimo não será possível até que o livro em atraso seja devolvido"

            elif livro.exemplares > 0:
            # Processa o empréstimo
                emprestimo = Emprestimo(usuario, livro)
                usuario.emprestimos.append(emprestimo)
                livro.exemplares -= 1

                return f"Emprestimo registrado para {usuario.nome}, Livro: {livro.titulo}, Devolução: {emprestimo.data_devolucao}. Código do empréstimo: {emprestimo.id}"
            
            else:
                return f"O livro '{livro.titulo}' já atingiu o limite de empréstimos."