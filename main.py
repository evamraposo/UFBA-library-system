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
        print("\n\nBem-vindo ao Sistema de Gerenciamento de Biblioteca\n-Instruções: [1] Emprestar Livro, [2] Devolver Livro, [3] Reservar Livro, [4] Sair")
        opcao = input("-Escolha uma opção: ")
        if opcao == "4":
            print("Saindo do sistema...")
            break
        elif opcao == "1":
            # Lógica para empréstimo de livro
            codigo_usuario = int(input("Digite o código do usuário: "))
            codigo_livro = int(input("Digite o código do livro: "))
            usuario = next((u for u in biblioteca.usuarios if u.codigo == codigo_usuario), None)
            livro = next((l for l in biblioteca.livros if l.codigo == codigo_livro), None)
            if usuario and livro:
                mensagem = biblioteca.emprestar_livro(usuario, livro)
                print(mensagem)
            else:
                print("Usuário ou livro não encontrado.")
        elif opcao == "2":
            # Lógica para devolução de livro
            codigo_emprestimo = int(input("Digite o código do empréstimo: "))
            emprestimo = next((e for e in biblioteca.emprestimos if e.id == codigo_emprestimo), None)
            if emprestimo:
                mensagem = biblioteca.devolver_livro(emprestimo)
                print(mensagem)
            else:
                print("Empréstimo não encontrado.")
        elif opcao == "3":
            # Lógica para reserva de livro
            codigo_usuario = int(input("Digite o código do usuário: "))
            codigo_livro = int(input("Digite o código do livro: "))
            usuario = next((u for u in biblioteca.usuarios if u.codigo == codigo_usuario), None)
            livro = next((l for l in biblioteca.livros if l.codigo == codigo_livro), None)
            if usuario and livro:
                mensagem = biblioteca.reservar_livro(usuario, livro)
                print(mensagem)
            else:
                print("Usuário ou livro não encontrado.")


        

if __name__ == "__main__":
    main()
