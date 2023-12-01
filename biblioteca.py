from observador import Observador

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.observador = Observador()

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)




    

    