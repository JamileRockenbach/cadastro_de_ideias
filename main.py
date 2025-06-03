from recursos.basicFunc import limparTela, aguardar
from recursos.basicFunc import inicializarBanco
from recursos.basicFunc import ouvir
bd = inicializarBanco()

while True:
    limparTela()
    print("Bem-vindo ao ideOTA! :)")
    print("1 - Nova Ideia")
    print("2 - Ver Ideias")
    print("3 - Excluir Ideia")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        print("Opção 1 selecionada: Nova Ideia")
        nova_ideia = ouvir()
        if len(nova_ideia) < 5:
            print("Dados insuficientes.")
            aguardar(2)
            bd.append(nova_ideia)
            arquivo = open("database.atitus", "w")
            for ideia in bd:
                arquivo.write(ideia + "\n")
            arquivo.close()
            print("Ideia adicinada com sucesso!")
            aguardar(2)
        else:
            print("Dados insuficientes.")
            aguardar(2)

    elif opcao == "2":
        print("Opção 2 selecionada: Ver Ideias")
        if len(bd) != 0:
            for ideia in bd:
                print(f" - {ideia}")
        else:
            print("Nenhuma ideia cadastrada.")
            aguardar(2)
        input("Precione Enter para continuar...")

    elif opcao == "3":
        print("Opção 3 selecionada: Excluir Ideia")
        if len(bd) != 0:
            indice = 0
            for ideia in bd:
                print(f"{indice} - {ideia}")
                indice += 1
            try:
                idExcluir =  int(input("Qual o Id? "))
                bd.pop(idExcluir)
                print("Ideia excluída com sucesso!")
                arquivo = open("database.atitus", "w")
                for ideia in bd:
                    arquivo.write(ideia + "\n") 
                arquivo.close() 
                aguardar(2)
            except :
                print("Ops, algo deu errado!")
                aguardar(2)
        else:
            print("Nenhuma ideia cadastrada.")
            aguardar(2)
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
        aguardar(2)