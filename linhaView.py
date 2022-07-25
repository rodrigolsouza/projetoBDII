import time
from linha import Linha
from linhaDao import LinhaDao


class LinhaView:
    def __init__(self):
        pass
    
    def inserirLinha():
        print("Digite os dados da sua linha de transportes")
        codigo=input("CÓDIGO: ")
        nome=input("NOME: ")
        tarifa=input("TARIFA: ")
        frota=input("FROTA: ")
        integração=input("INTEGRAÇÃO? ")
        arCondicionado=input("AR-CONDICIONADO? ")
        empresaOperadora=input("EMPERESA OPERADORA: ")
        print("\n")

        if len(codigo)!=0 and len(nome)!=0 and len(tarifa)!=0 and len(frota)!=0 and len(integração)!=0 and len(arCondicionado)!=0:
            linha= Linha(codigo,nome,tarifa,frota,integração,arCondicionado,empresaOperadora)
            linhaDao=LinhaDao()
            resultado=linhaDao.inserirBanco(linha)
            print("Linha inserida com sucesso!")
            return(resultado)
        else:
            print("Todos os campos precisam ser preenchidos! Por favor refaça a operação.")
            
    def showLinha(documento):
        
        print("\n")
        print("********LINHA ENCONTRADA! *********")
        print("\n*************************************************")
        print("CÓDIGO: ", documento.get("Código"))
        print("NOME: ", documento.get("Nome"))
        print("TARIFA: ", documento.get("Tarifa"))
        print("FROTA: ", documento.get("Frota"))
        print("A LINHA FAZ INTEGRAÇÃO? : ", documento.get("Integração"))
        print("A LINHA POSSUI VÉICULO COM AR-CONDICIONADO?: ", documento.get("ArCondicionado"))
        print("EMPRESA OPERADORA : ", documento.get("empresaOperadora"))
        print("\n*************************************************")
        

    def consultarLinha_Por_Nome():
        nome=input("Busque uma linha de Ônibus: ")
        linhaDao=LinhaDao()
        resultado=linhaDao.consultar(nome)
        
        if resultado:
            for empr in resultado:
                #return LinhaView.showLinha(empr)
                print(LinhaView.showLinha(empr))
        else:
                print("Linha não encontrada!")
        

