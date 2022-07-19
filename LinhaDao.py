
import ast
import json
import time
from linha import Linha
from conexao import *

class LinhaDao():
    def __init__(self):
        pass
    
    def inserirBanco(self,linhaView):
        formaJson=json.dumps(linhaView.__dict__,ensure_ascii=False)
        linhaBanco=ast.literal_eval(formaJson)
        for chave, valor in linhaBanco.items():
            if chave=="Código" or chave=="Frota":
                valor=int(valor)
                linhaBanco.update({chave:valor})
            if chave=="Tarifa":
                valor=round(float(valor,),3)
                linhaBanco.update({chave:valor})
        print("A inserir no Banco...")
        time.sleep(1)
        print(linhaBanco)
        colecaoLinhas.insert_one(linhaBanco)
        print("Linha inserida com sucesso!")

    def consultar(self):
        pass
    def alterar(self):
        pass
    def excluir(self):
        pass
