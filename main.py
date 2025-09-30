from app import App

def menu():
    app = App()

    while True:
        print("\n=== Sistema de Usuários ===")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Desativar usuário")
        print("4 - Buscar usuário na API")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            user = app.adicionar_usuario(nome, email)
            print(f"Usuário {user.nome} adicionado com sucesso!")

        elif opcao == "2":
            usuarios = app.listar_usuarios()
            print("\nLista de Usuários:")
            for u in usuarios:
                status = "Ativo" if u.ativo else "Inativo"
                print(f"{u.id}: {u.nome} ({u.email}) - {status}")

        elif opcao == "3":
            user_id = int(input("ID do usuário: "))
            if app.desativar_usuario(user_id):
                print("Usuário desativado com sucesso.")
            else:
                print("Usuário não encontrado.")

        elif opcao == "4":
            user_id = input("ID do usuário na API: ")
            dados = app.buscar_usuario_api(user_id)
            if dados:
                print(f"Usuário encontrado: {dados['name']} ({dados['email']})")
            else:
                print("Usuário não encontrado na API.")

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
