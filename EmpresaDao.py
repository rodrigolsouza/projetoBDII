import ast
import json
import time
from empresa import Empresa
from conexao import *

class EmpresaDao():
    def __init__(self):
        pass

    def inserirBanco(self,empresaView):
        #Transforma o objeto em string Json
        formaJson=json.dumps(empresaView.__dict__,ensure_ascii=False)

        #Transforma toda a string em dicionario
        empresaBanco=ast.literal_eval(formaJson)

        #Busca os valores que devem ser diferentes de string e transforma no que realmente são
        for chave,valor in empresaBanco.items():
            if chave=="FrotaTotal" or chave=="FrotaArCondicioado":
                valor=int(valor)
                empresaBanco.update({chave:valor})

        #Inserção no banco
        print("A inserir no Banco...")
        time.sleep(1)
        print(empresaBanco)
        colecaoEmpresas.insert_one(empresaBanco)
        print("Empresa inserida com sucesso!")
            
    def consultarBanco():
        pass
    def alterarBanco():
        pass
    def excluirBanco():
        pass