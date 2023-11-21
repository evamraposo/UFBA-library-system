class Observador:
    def __init__(self):
        self.observadores = []

    def registrar_observador(self, observador):
        self.observadores.append(observador)

    def notificar_observadores(self, mensagem):
        for observador in self.observadores:
            observador.notificar(mensagem)

class ProfessorObservador:
    def __init__(self, nome):
        self.nome = nome

    def notificar(self, mensagem):
        print(f"Notificação para {self.nome}: {mensagem}")
