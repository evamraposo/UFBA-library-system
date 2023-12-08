class Usuario:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.emprestimos = []
        self.reservas = []
        self.emprestimos_passados = []  
        self.reservas_passadas = []     
        self.qtd_reservas = 3


