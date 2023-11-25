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



    def emprestar_livro(self, usuario, livro):
        # Verificar se o livro está reservado por outro usuário
        reserva = next((r for r in self.reservas if r.livro == livro and r.usuario != usuario), None)
        if reserva:
            return f"O livro '{livro.titulo}' está reservado por outro usuário."

        # Processa o empréstimo
        emprestimo = Emprestimo(usuario, livro)
        self.emprestimos.append(emprestimo)
        usuario.emprestimos.append(emprestimo)
        usuario.qtd_emprestimos -= 1
        #Verifica se há reserva em nome do usuário e remove se houver
        reserva = next((r for r in self.reservas if r.livro == livro and r.usuario == usuario), None)
        if reserva:
            self.reservas.remove(reserva)
            print('reserva removida')

        return f"Emprestimo registrado para {usuario.nome}, Livro: {livro.titulo}, Devolução: {emprestimo.data_devolucao}. Código do empréstimo: {emprestimo.id}"



    def devolver_livro(self, emprestimo):
        # Verifique se o empréstimo está na lista de empréstimos ativos
        if emprestimo in self.emprestimos:
            # Processa a devolução
            emprestimo.usuario.qtd_emprestimos += 1
            self.emprestimos.remove(emprestimo)

            return f"Livro '{emprestimo.livro.titulo}' devolvido com sucesso."
        else:
            return "Empréstimo não encontrado."

    def reservar_livro(self, usuario, livro):
        # Verifica se o livro já está reservado ou emprestado
        if any(r.livro == livro for r in self.reservas) or \
           any(e.livro == livro for e in self.emprestimos):
            return f"O livro '{livro.titulo}' já está reservado ou emprestado."

        # Cria uma nova reserva
        nova_reserva = Reserva(usuario, livro)
        self.reservas.append(nova_reserva)
        return f"Reserva realizada para o livro '{livro.titulo}' pelo usuário {usuario.nome}."

    

