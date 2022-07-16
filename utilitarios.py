import time
from linhaView import LinhaView
from empresaView import EmpresaView


def menu_inicial():
    time.sleep(1)
    print("\n")
    print("---------------MENU-----------------")
    menu = ["Operações sobre empresas de Ônibus",
            "Operações sobre linhas de ônibus", "Sair"]
    for numero, opção in enumerate(menu):
        print(numero+1, "-", opção)
    print("------------------------------------")


def exibir_menu_inicial():
    while True:
        menu_inicial()
        time.sleep(1)
        resposta = int(input("Digite a opção desejada"))
        try:
            if resposta == 1:
                exibir_menu_Empresas()
                break
            elif resposta == 2:
                exibir_menu_Linhas()
                break
            elif resposta == 3:
                print("Obrigado e volte sempre!")
                break
        except:
            print("opção inválida, digite apenas números")
            break


def menu_Empresas():
    time.sleep(1)
    print("\n")
    print("---------------MENU-----------------")
    menudeopções = ["Cadastrar nova Empresa", "Consultar Empresas",
                    "Alterar dados de alguma Empresa", "Excluir Empresa", "Voltar", "Sair"]
    for numero, opção in enumerate(menudeopções):
        print(numero+1, "-", opção)
    print("------------------------------------")


def exibir_menu_Empresas():
    while True:
        try:
            menu_Empresas()
            time.sleep(1)
            opção=int(input("Digite sua escolha:\n"))
            if opção==1:
                EmpresaView.inserir()
            elif opção==2:
                EmpresaView.consultar()
            elif opção==3:
                EmpresaView.alterar()
            elif opção==4:
                EmpresaView.excluir()
            elif opção==5:
                exibir_menu_inicial()
                break
            elif opção==6:
                print("Obrigado por utilizar nosssos serviços!")
                break
        except:
            print("opção invalida, digite apenas números")
            break


def menu_Linhas():
    time.sleep(1)
    print("\n")
    print("---------------MENU-----------------")
    menudeopções = ["Cadastrar nova Linha", "Consultar Linhas",
                    "Alterar dados da Linha", "Excluir Linha", "Voltar" ,"Sair"]
    for numero, opção in enumerate(menudeopções):
        print(numero+1, "-", opção)
    print("------------------------------------")
    

def exibir_menu_Linhas():
    while True:
        try:
            menu_Linhas()
            time.sleep(1)
            opção=int(input("Digite sua escolha: \n"))
            if opção==1:
                LinhaView.inserirLinha()
            elif opção==2:
                LinhaView.consultar()
            elif opção==3:
                LinhaView.alterar()
            elif opção==4:
                LinhaView.excluir()
            elif opção==5:
                exibir_menu_inicial()
                break
            elif opção==6:
                print("Obrigado por utilizar nosssos serviços!")
                break
        except:
            print("opção invalida, digite apenas números")
            break
