import time
from linha import Linha
from linhaDao import LinhaDao
from empresa import Empresa
from empresaDao import EmpresaDao
from conexao import *

class LinhaView:
    def __init__(self):
        pass
    
    def inserirLinha():
        print("Digite os dados da sua linha de transportes")
        codigo=input("CÓDIGO: ").upper()
        nome=input("NOME: ").upper()
        tarifa=input("TARIFA: ").upper()
        frota=input("FROTA: ").upper()
        integração=input("INTEGRAÇÃO? ").upper()
        arCondicionado=input("AR-CONDICIONADO? ").upper()
        empresaOperadora=input("EMPERESA OPERADORA: ").upper()
        print("\n")

        if len(codigo)!=0 and len(nome)!=0 and len(tarifa)!=0 and len(frota)!=0 and len(integração)!=0 and len(arCondicionado)!=0:
            linha= Linha(codigo,nome,tarifa,frota,integração,arCondicionado,empresaOperadora)
            linhaDao=LinhaDao()
            resultado=linhaDao.inserirBanco(linha)
            print("Linha inserida com sucesso!")
            return(resultado)
        else:
            print("Todos os campos precisam ser preenchidos! Por favor refaça a operação.")
        
    def consultarLinha_Por_Nome():
        nome=input("Busque uma linha de Ônibus: ").upper()
        linhaDao=LinhaDao()
        resultado=linhaDao.consultar(nome)
        print("\n")
        #print("********LINHA(S) ENCONTRADA(S)! *********")
        
        if resultado:
            for empr in resultado:
                time.sleep(1)
                LinhaView.showLinha(empr)
                time.sleep(1)
        else:
                print("Linha não encontrada!")
        
    def showLinha(documento):
        
        print("\n*************************************************")
        print("CÓDIGO: ", documento.get("Código"))
        print("NOME: ", documento.get("Nome"))
        print("TARIFA: ", documento.get("Tarifa"))
        print("FROTA: ", documento.get("Frota"))
        print("A LINHA FAZ INTEGRAÇÃO? : ", documento.get("Integração"))
        print("A LINHA POSSUI VÉICULO COM AR-CONDICIONADO?: ", documento.get("ArCondicionado"))
        print("EMPRESA OPERADORA : ", documento.get("empresaOperadora"))
        print("\n*************************************************")

    def consultar_LinhascomArCondicionado():

        linhaDao = LinhaDao()
        resultado = linhaDao.linhasClimatizadas()
        print("\n")
        print("********LINHA(S) QUE POSSUEM AR-CONDICIONADO! ***")

        if resultado:
            for empr in resultado:
                time.sleep(1)
                LinhaView.showLinha_comArCondicionado(empr)
                time.sleep(1)
        else:
                print("Nenhuma linha encontrada!")        

    def showLinha_comArCondicionado(documento):
        
        print("\n")
        print(documento.get("Código"),"\t",documento.get("Nome"))            