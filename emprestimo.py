from datetime import datetime, timedelta
from usuario import AlunoGraduacao, AlunoPosGraduacao, Professor


class Emprestimo:
    contador_id = 0

    def __init__(self, usuario, livro, data_emprestimo=None):
        self.id = Emprestimo.contador_id
        Emprestimo.contador_id += 1
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo if data_emprestimo else datetime.now()
        self.data_devolucao = self.calcular_data_devolucao(usuario)

    def calcular_data_devolucao(self, usuario):
        if isinstance(usuario, AlunoGraduacao):
            return self.data_emprestimo + timedelta(days=3)
        elif isinstance(usuario, AlunoPosGraduacao):
            return self.data_emprestimo + timedelta(days=4)
        elif isinstance(usuario, Professor):
            return self.data_emprestimo + timedelta(days=7)
        else:
            return self.data_emprestimo  # Retornar uma data padrão ou gerar um erro


    def verificar_atraso(self):
        if datetime.now() > self.data_devolucao:
            print(f"Devolução pendente, em atraso desde o dia {self.data_devolucao}")
            return True
        else:
            
            return "Em dia"
