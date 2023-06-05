from cinema_poo import Filme


f1 = Filme()
while True:
    print("====Menu====")
    print("1. Cadastra filme")
    print("2. Consulta filmes")
    print("3. Deletar filme")
    print("4. Atualizar filme")
    print("5. Sair")

    opcao = input("Digite a opção desejada:")

    if opcao == "1":
        codigo = int(input("Informe p codigo do filme: "))
        titulo = input("Título: ")
        genero = input("Gênero: ")
        duracao = input("Duração: ")
        classificacao_indicativa = input("Classificação Indicativa: ")
        
        f1.cadastraFilme(
            codigo = codigo,
            titulo = titulo,
            genero = genero,
            duracao = duracao,
            classificacao_indicativa = classificacao_indicativa
        )

        print("Filme cadastrado com sucesso.")

    elif opcao == "2":
        f1.consultarFilmes()

    elif opcao == "3":
        codigo = input("Digite o código do filme que deseja deletar: ")


        f1.deletarFilme()

    elif opcao == "4":
        codigo = input("Digite o código do filme que deseja atualizar: ")

        print("Digite o campo que deseja atualizar:")
        print("1. Título")
        print("2. Gênero")
        print("3. Duração")
        print("4. Classificação Indicativa")

        campo_opcao = input("Opção: ")

        if campo_opcao == "1":
            campo = "titulo"
        elif campo_opcao == "2":
            campo = "genero"
        elif campo_opcao == "3":
            campo = "duracao"
        elif campo_opcao == "4":
            campo = "classificacao_indicativa"
        else:
            print("Opção inválida.")
            continue

        valor = input("Digite o novo valor: ")
        
        f1.atualizarFilme(titulo, genero, duracao, classificacao_indicativa )

    elif opcao == "5":
        break

    else:
        print("Opção inválida. Digite novamente.")