from observador import Observador
from reservarLivro import ReservarLivro
from datetime import datetime, timedelta


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.observador = Observador()
        self.reserva = ReservarLivro()


    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def emprestar_livro(self, codigo_usuario, codigo_livro):

        usuario = next((u for u in self.usuarios if u.codigo == codigo_usuario), None)
        livro = next((l for l in self.livros if l.codigo == codigo_livro), None)

        if usuario and livro:
                
                mensagem = usuario.emprestimo(livro)
                print(mensagem)

        else:

            print("Usuário ou livro não encontrado.")

    def devolver_livro(self, codigo_emprestimo, codigo_usuario):
        usuario = next((u for u in self.usuarios if u.codigo == codigo_usuario), None)
        emprestimo = next((e for e in usuario.emprestimos if e.id == codigo_emprestimo), None)

        if emprestimo:

                mensagem = usuario.devolucao(emprestimo)
                print(mensagem)

        else:
            print("Empréstimo não encontrado.")


    def reservar_livro(self, codigo_usuario, codigo_livro):
        usuario = next((u for u in self.usuarios if u.codigo == codigo_usuario), None)
        livro = next((l for l in self.livros if l.codigo == codigo_livro), None)
    
        if usuario and livro:
            mensagem = self.reserva.reservar_livro(usuario, livro)
            print(mensagem)
        else:
            print("Usuário ou livro não encontrado.")

    
    def observar(self, codigo_usuario, codigo_livro):
        usuario = next((u for u in self.usuarios if u.codigo == codigo_usuario), None)
        livro = next((l for l in self.livros if l.codigo == codigo_livro), None)

        if usuario and livro:
            mensagem = livro.registrar_observador(usuario)
            print(mensagem)


    def exibir_info_livro(self, codigo_livro):
        livro = next((l for l in self.livros if l.codigo == codigo_livro), None)
        if livro:
            print(f"Titulo: {livro.titulo}, Quantidade de Reservas: {livro.reservas}")
            for usuario in self.usuarios:
                for emprestimo in usuario.emprestimos:
                    if emprestimo.livro.codigo == codigo_livro:
                        # Verificar se a data de devolução é posterior à data atual
                        status = 'Emprestado' if emprestimo.data_devolucao > datetime.now() else 'Disponível'
                        print(f"Exemplar {emprestimo.id}: Status: {status}, Emprestado a: {usuario.nome}, Data de empréstimo: {emprestimo.data_emprestimo}, Data de devolução: {emprestimo.data_devolucao}")
        else:
            print("Livro não encontrado.")

    def exibir_info_usuario(self, codigo_usuario):
        usuario = next((u for u in self.usuarios if u.codigo == codigo_usuario), None)
        if usuario:
            print(f"Empréstimos e reservas do usuário {usuario.nome}:")

            if not (usuario.emprestimos or usuario.reservas or usuario.emprestimos_passados or usuario.reservas_passadas):
                print("Não há empréstimos ou reservas para este usuário.")
                return

            for emprestimo in usuario.emprestimos + usuario.emprestimos_passados:  # Inclui empréstimos atuais e passados
                status = "Em curso" if emprestimo.data_devolucao > datetime.now() else "Finalizado"
                print(f"Titulo do livro: {emprestimo.livro.titulo}, Data do empréstimo: {emprestimo.data_emprestimo}, Status: {status}, Data da devolução: {emprestimo.data_devolucao}")

            for reserva in usuario.reservas + usuario.reservas_passadas:  # Inclui reservas atuais e passadas
                print(f"Titulo do livro reservado: {reserva.livro.titulo}, Data da reserva: {reserva.data_reserva}")
        else:
            print("Usuário não encontrado.")



    def exibir_notificacoes_professor(self, codigo_usuario):
        usuario = next((u for u in self.usuarios if u.codigo == codigo_usuario and isinstance(u, Professor)), None)
        if usuario:
            print(f"Notificações para o professor {usuario.nome}: {len(usuario.notificacoes)} vezes")
        else:
            print("Professor não encontrado ou código inválido.")