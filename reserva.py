class Reserva:
    def __init__(self, usuario, livro):
        self.usuario = usuario
        self.livro = livro

    def realizar_reserva(self):
        return f"Reserva realizada para {self.usuario.nome}, Livro: {self.livro.titulo}"

    def cancelar_reserva(self):
        return f"Reserva cancelada para {self.usuario.nome}, Livro: {self.livro.titulo}"
