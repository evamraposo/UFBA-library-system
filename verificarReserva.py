
class VerificarReserva:

    def verificar_reserva(self, usuario, livro):
        reserva = next((r for r in usuario.reservas if r.livro == livro and r.usuario == usuario), None)
        if reserva:
            usuario.reservas.remove(reserva)
            livro.reservas += 1
            usuario.qtd_reservas += 1
            return True
        return False
    
    def limite_exemplares_reservados(self, livro):

        if livro.exemplares_disponiveis == 0:
            return True
        
        elif livro.exemplares_disponiveis == 1 and livro.exemplares_disponiveis == livro.reservas:
            return True
        
        elif livro.exemplares_disponiveis <= 0:
            return True