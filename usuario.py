class Usuario:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.emprestimos = []
        self.reservas = []
        self.qtd_reservas = 3

    def exibir_informacoes(self,  tipo_usuario):
        return f"{tipo_usuario}, {self.nome}, Código: {self.codigo}"
