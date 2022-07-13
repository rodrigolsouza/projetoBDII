
def menu_inicial():
    print("\n")
    print("---------MENU-----------")
    menu = ["Operações sobre empresas de Ônibus",
            "Operações sobre linhas de ônibus", "Sair"]
    for numero, opção in enumerate(menu):
        print(numero+1, "-", opção)
    print("------------------------")


def exibir_menu_inicial():
    while True:
        resposta = int(input("Digite a opção desejada"))
        try:
            if resposta == 1:
                menu_Empresas()
                exibir_menu_Empresas()
            elif resposta == 2:
                menu_Linhas()
                exibir_menu_Linhas()
            elif resposta == 3:
                print("Obrigado e volte sempre!")
                break
        except:
            print("opção inválida, digite apenas números")
            break


def menu_Empresas():
    print("\n")
    print("---------MENU-----------")
    menudeopções = ["Cadastrar nova Empresa", "Consultar Empresas",
                    "Alterar dados de alguma Empresa", "Excluir Empresa", "Sair"]
    for numero, opção in enumerate(menudeopções):
        print(numero+1, "-", opção)
    print("------------------------")

def exibir_menu_Empresas():
    while True:
        try:
            opção=int(input("Digite sua escolha:\n"))
            if opção==1:
                Empresa.inserir()
            elif opção==2:
                Empresa.consultar()
            elif opção==3:
                Empresa.alterar()
            elif opção==4:
                Empresa.excluir()
            elif opção==5:
                print("Obrigado por utilizar nosssos serviços!")
                break
        except:
            print("opção invalida, digite apenas números")


def menu_Linhas():
    print("\n")
    print("---------MENU-----------")
    menudeopções = ["Cadastrar nova Linha", "Consultar Linhas",
                    "Alterar dados da Linha", "Excluir Linha", "Sair"]
    for numero, opção in enumerate(menudeopções):
        print(numero+1, "-", opção)
    print("------------------------")

def exibir_menu_Linhas():
    while True:
        try:
            opção=int(input("Digite sua escolha:\n"))
            if opção==1:
                Linha.inserir()
            elif opção==2:
                Linha.consultar()
            elif opção==3:
                Linha.alterar()
            elif opção==4:
                Linha.excluir()
            elif opção==5:
                print("Obrigado por utilizar nosssos serviços!")
                break
        except:
            print("opção invalida, digite apenas números")