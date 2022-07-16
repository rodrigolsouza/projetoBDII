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
        integração=input("INTEGRAÇÃO:")
        arCondicionado=input("AR-CONDICIONADO: ")
        linha= Linha(codigo,nome,tarifa,frota,integração,arCondicionado)
        linhaDao=LinhaDao()
        linhaDao.inserirBanco(linha)

