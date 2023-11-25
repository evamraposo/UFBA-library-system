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
        print("\n\nBem-vindo ao Sistema de Gerenciamento de Biblioteca\n-Instruções: Para empréstimo digite emp, para devolução digite dev, para reservar digite res, seguido de um espaço digite seu código de usuário e o código do livro, se desejar encerrar o Sistema digiter sair:")

        opcao = input("Qual ação deseja realizar? ")

        if opcao != 'sair':
            acao = opcao[:3]
            codigo_usuario = int(opcao[4])
            codigo_livro = int(opcao[6])
            
            if acao == "emp":
                # Lógica para empréstimo de livro
                usuario = next((u for u in biblioteca.usuarios if u.codigo == codigo_usuario), None)
                livro = next((l for l in biblioteca.livros if l.codigo == codigo_livro), None)
                if usuario and livro:
                    mensagem = biblioteca.emprestar_livro(usuario, livro)
                    print(mensagem)
                else:
                    print("Usuário ou livro não encontrado.")
            elif acao == "dev":
                # Lógica para devolução de livro
                codigo_emprestimo = int(input("Digite o código do empréstimo: "))
                emprestimo = next((e for e in biblioteca.emprestimos if e.id == codigo_emprestimo), None)
                if emprestimo:
                    mensagem = biblioteca.devolver_livro(emprestimo)
                    print(mensagem)
                else:
                    print("Empréstimo não encontrado.")
            elif acao == "res":
                # Lógica para reserva de livro
                usuario = next((u for u in biblioteca.usuarios if u.codigo == codigo_usuario), None)
                livro = next((l for l in biblioteca.livros if l.codigo == codigo_livro), None)
                if usuario and livro:
                    mensagem = biblioteca.reservar_livro(usuario, livro)
                    print(mensagem)
                else:
                    print("Usuário ou livro não encontrado.")

        else:
            print("Saindo do sistema...")
            break

        

if __name__ == "__main__":
    main()
