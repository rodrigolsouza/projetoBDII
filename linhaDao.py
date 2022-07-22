
import ast
import json
import time
import bson
from bson import objectid
from linha import Linha
from conexao import *

class LinhaDao():
    def __init__(self):
        pass
    
    def inserirBanco(self,linhaView):
        #Transforma o objeto em string Json
        formaJson=json.dumps(linhaView.__dict__,ensure_ascii=False)

        #Transforma toda a string em dicionario
        linhaBanco=ast.literal_eval(formaJson)

        #Busca os valores que devem ser diferentes de string e transforma no que realmente são
        for chave, valor in linhaBanco.items():
            if chave=="Código" or chave=="Frota":
                valor=int(valor)
                linhaBanco.update({chave:valor})
            if chave=="Tarifa":
                valor=round(float(valor,),3)
                linhaBanco.update({chave:valor})
                
        #Inserção no banco
        print("A inserir no Banco...")
        time.sleep(1)
        print(linhaBanco)
        resultado=colecaoLinhas.insert_one(linhaBanco)
        print("Linha ID: {}" .format(resultado.inserted_id))

    def consultar(self):
        pass
    def alterar(self):
        pass
    def excluir(self):
        pass
