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
        try:
            menu_inicial()
            time.sleep(1)
            resposta = int(input("Digite a opção desejada: "))
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
                print("Opção Inválida, Escolha uma opção entre 1 e 3!")
        break


def menu_Empresas():
    time.sleep(1)
    print("\n")
    print("---------------MENU-----------------")
    menudeopções = ["Cadastrar nova Empresa", "Consultar dados sobre uma empresa de transportes",
                    "Exibir linhas agrupadas por empresa", "Voltar", "Sair"]
    for numero, opção in enumerate(menudeopções):
        print(numero+1, "-", opção)
    print("------------------------------------")


def exibir_menu_Empresas():
    while True:
        try:
            menu_Empresas()
            time.sleep(1)
            opção=int(input("Digite sua escolha: \n"))
            if opção==1:
                resultado=EmpresaView.inserirEmpresa()
                print(resultado)
                exibir_menu_inicial()
            elif opção==2:
                resultado=EmpresaView.consultarEmpresa_Por_Nome()
                exibir_menu_inicial()
            elif opção==3:
                EmpresaView.consultarTudo()
                exibir_menu_inicial()
            elif opção==4:
                exibir_menu_inicial()
                break
            elif opção==5:
                print("Obrigado por utilizar nosssos serviços!")
                break
                
        except:
                print("Opção Inválida, Escolha uma opção entre 1 e 5!")
        break


def menu_Linhas():
    time.sleep(1)
    print("\n")
    print("---------------MENU-----------------")
    menudeopções = ["Cadastrar Nova Linha", "Consultar infomações sobre uma linha de Ônibus",
                    "Consultar Linhas Com Ar-Condicionado", "Voltar" ,"Sair"]
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
                exibir_menu_inicial()
            elif opção==2:
                resultado=LinhaView.consultarLinha_Por_Nome()
                exibir_menu_inicial()
            elif opção==3:
                resultado=LinhaView.consultar_LinhascomArCondicionado()
                exibir_menu_inicial()
            elif opção==4:
                exibir_menu_inicial()
            elif opção==5:
                print("Obrigado por utilizar nosssos serviços!")
                break          
            
        except:
                print("Opção Inválida, Escolha uma opção entre 1 e 5!")
        break