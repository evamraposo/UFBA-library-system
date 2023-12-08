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
        print("\n\nBem-vindo ao Sistema de Gerenciamento de Biblioteca\n-Instruções: Para empréstimo digite emp, para devolução digite dev, para reservar digite res, para observar digite obs, seguido de um espaço digite seu código de usuário e o código do livro, se desejar encerrar o Sistema digiter sair:")

        opcao = input("Qual ação deseja realizar? ")

        if opcao != 'sai':
            acao = opcao[:3]
            codigo_usuario = int(opcao[4:7])
            codigo_livro = int(opcao[8:11])
            # print(codigo_usuario, codigo_livro)

            if acao == "emp":
                
                biblioteca.emprestar_livro(codigo_usuario, codigo_livro)

            elif acao == "dev":
               
                codigo_emprestimo = int(input("Digite o código do empréstimo: "))
                biblioteca.devolver_livro(codigo_emprestimo, codigo_usuario)

            elif acao == "res":

                biblioteca.reservar_livro(codigo_usuario, codigo_livro)
            
            elif acao == "obs":

                biblioteca.observar(codigo_usuario, codigo_livro)

        else:
            print("Saindo do sistema...")
            break

        

if __name__ == "__main__":
    main()
