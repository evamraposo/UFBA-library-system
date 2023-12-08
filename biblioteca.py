from reservarLivro import ReservarLivro

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
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