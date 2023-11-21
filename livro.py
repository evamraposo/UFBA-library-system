class Livro:
    def __init__(self, codigo, titulo, editora, autores, edicao, ano_publicacao, exemplares):
        self.codigo = codigo
        self.titulo = titulo
        self.editora = editora
        self.autores = autores
        self.edicao = edicao
        self.ano_publicacao = ano_publicacao
        self.exemplares = exemplares

    def exibir_informacoes(self):
        info = f"Titulo: {self.titulo}, Editora: {self.editora}, Autores: {', '.join(self.autores)}, "
        info += f"Edição: {self.edicao}, Ano: {self.ano_publicacao}, Exemplares: {self.exemplares}"
        return info
