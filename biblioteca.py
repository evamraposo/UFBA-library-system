from observador import Observador
from emprestimo import Emprestimo
from reserva import Reserva



class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []
        self.reservas = []
        self.observador = Observador()

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)



    def emprestar_livro(self, usuario, livro, professor):

        #Verifica se o livro atingiu o máximo de exemplares emprestados
        if livro.exemplares > 0:

            #Verifica se há reserva em nome do usuário
            reserva = next((r for r in self.reservas if r.livro == livro and r.usuario == usuario), None)
            if reserva:
                self.reservas.remove(reserva)
                livro.reservas += 1

            #Verifica se o livro já atingiu o máximo de exemplares reservados
            elif professor == 0:
                
                if livro.reservas <= 0 or livro.reservas == livro.exemplares: 
                    return f"O livro '{livro.titulo}' está reservado por outro usuário."
                else:
                    usuario.qtd_emprestimos -= 1

            # Processa o empréstimo
            emprestimo = Emprestimo(usuario, livro)
            self.emprestimos.append(emprestimo)
            usuario.emprestimos.append(emprestimo)
            livro.exemplares -= 1

            return f"Emprestimo registrado para {usuario.nome}, Livro: {livro.titulo}, Devolução: {emprestimo.data_devolucao}. Código do empréstimo: {emprestimo.id}"
        
        else:
            return f"O livro '{livro.titulo}' já atingiu o limite de empréstimos."

    def devolver_livro(self, emprestimo, professor):
        # Verifique se o empréstimo está na lista de empréstimos ativos
        if emprestimo in self.emprestimos:
            # Processa a devolução
            if professor == 0:
                emprestimo.usuario.qtd_emprestimos += 1

            emprestimo.livro.exemplares += 1
            self.emprestimos.remove(emprestimo)

            return f"Livro '{emprestimo.livro.titulo}' devolvido com sucesso."
        else:
            return "Empréstimo não encontrado."

    def reservar_livro(self, usuario, livro):
        if livro.exemplares == 0:
            return f"O livro '{livro.titulo}' já está reservado ou emprestado."
        
        elif livro.exemplares == 1 and livro.exemplares == livro.reservas:
            return f"O livro '{livro.titulo}' já está reservado ou emprestado."
        
        elif livro.reservas <= 0:
            return f"O livro '{livro.titulo}' já atingiu o limite de reservas."
        
        # Cria uma nova reserva
        nova_reserva = Reserva(usuario, livro)
        self.reservas.append(nova_reserva)
        livro.reservas -= 1
        return f"Reserva realizada para o livro '{livro.titulo}' pelo usuário {usuario.nome}."

    