from verificarReserva import VerificarReserva
from reserva import Reserva

class ReservarLivro:

    def reservar_livro(self, usuario, livro):
        verifica = VerificarReserva()
        
        if verifica.limite_exemplares_reservados(livro):
            return f"O livro '{livro.titulo}' já atingiu o limite de reservas ou empréstimos."
        
        elif usuario.qtd_reservas == 0:
            return "O usuário já atingiu o limite de reservas."
        
        else:
            # Cria uma nova reserva
            nova_reserva = Reserva(usuario, livro)
            usuario.reservas.append(nova_reserva)
            livro.reservas -= 1
            usuario.qtd_reservas -= 1
            if (livro.exemplares - livro.reservas) >= 2:
                    livro.notificar_observadores()
        return f"Reserva realizada para o livro '{livro.titulo}' pelo usuário {usuario.nome}."