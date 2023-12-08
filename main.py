

from biblioteca import Biblioteca
import dados_usuarios
import dados_livros

def main():
    biblioteca = Biblioteca()

    # Carregar dados pré-definidos
    for usuario in dados_usuarios.usuarios:
        biblioteca.registrar_usuario(usuario)
    for livro in dados_livros.livros:
        biblioteca.adicionar_livro(livro)

    while True:
        print("\n\nBem-vindo ao Sistema de Gerenciamento de Biblioteca")
        print("- Instruções: \n - Para empréstimo digite 'emp', seguido do código de usuário e do livro.")
        print(" - Para devolução digite 'dev', seguido do código do empréstimo e do usuário.")
        print(" - Para reserva digite 'res', seguido do código de usuário e do livro.")
        print(" - Para observar digite 'obs', seguido do código de usuário e do livro.")
        print(" - Para informações de um livro digite 'liv', seguido do código do livro.")
        print(" - Para informações de um usuário digite 'usu', seguido do código do usuário.")
        print(" - Para notificações de um professor digite 'ntf', seguido do código do professor.")
        print(" - Para sair digite 'sai'.")

        opcao = input("Qual ação deseja realizar? ").split()

        if opcao[0] != 'sai':
            acao = opcao[0]

            if acao in ["emp", "res", "obs"]:
                codigo_usuario = int(opcao[1])
                codigo_livro = int(opcao[2])

                if acao == "emp":
                    biblioteca.emprestar_livro(codigo_usuario, codigo_livro)
                elif acao == "res":
                    biblioteca.reservar_livro(codigo_usuario, codigo_livro)
                elif acao == "obs":
                    biblioteca.observar(codigo_usuario, codigo_livro)

            elif acao == "dev":
                codigo_emprestimo = int(opcao[1])
                codigo_usuario = int(opcao[2])
                biblioteca.devolver_livro(codigo_emprestimo, codigo_usuario)

            elif acao == "liv":
                codigo_livro = int(opcao[1])
                biblioteca.exibir_info_livro(codigo_livro)

            elif acao == "usu":
                codigo_usuario = int(opcao[1])
                biblioteca.exibir_info_usuario(codigo_usuario)

            elif acao == "ntf":
                codigo_usuario = int(opcao[1])
                biblioteca.exibir_notificacoes_professor(codigo_usuario)

        else:
            print("Saindo do sistema...")
            break

if __name__ == "__main__":
    main()
