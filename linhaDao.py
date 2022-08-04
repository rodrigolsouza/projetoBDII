
import ast
import json
import time
import re
# import bson
# from bson import objectid
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

        #Inserção no banco
        print("A inserir no Banco...")
        time.sleep(1)
        resultado=colecaoLinhas.insert_one(linhaBanco)
        return(resultado.inserted_id)

    def consultar(self,nome):
        nome= re.compile(".*{}.*" .format(nome),re.IGNORECASE)
        resultado=colecaoLinhas.find({"Nome": nome}).sort("Código")   
        return resultado

    def linhasClimatizadas(self):
        resultado=colecaoLinhas.find({"ArCondicionado": "SIM"}).sort("Código")
        return resultado
            
