
from conexao import *
#from linha import Linha

class LinhaDao():
    def __init__(self):
        self.linha=Linha()
        self.conexao=conexao()

    def inserir(self,linha):
        colecaoBanco=self.conexao.colecao1
        linhaBanco = {
        "CÓDIGO": self.linha.get_codigo ,
        "LINHA": self.linha.get_nome ,
        "TARIFA": self.linha.get_tarifa ,
        "FROTA": self.linha.get_frota ,
        "INTEGRAÇÃO": self.linha.get_integraçao ,
        "AR-CONDICIONADO": self.linha.get_ar_condicionado
        }
        colecaoBanco.insert_one(linhaBanco)

    def consultar(self):
        pass
    def alterar(self):
        pass
    def excluir(self):
        pass
