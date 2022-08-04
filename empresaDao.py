import ast
import json
import re
import time

#from bson import ObjectId
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

        #Inserção no banco
        time.sleep(1)
        print("A inserir no Banco...")
        resultado=colecaoEmpresas.insert_one(empresaBanco)
        return(resultado.inserted_id)

    def consultarEmpresaBanco_Por_Nome(self,nome):
        nome= re.compile(".*{}.*" .format(nome),re.IGNORECASE)
        resultado=colecaoEmpresas.find({"Nome": nome})
        return resultado

    def consultar_EmpresasLinhas():
        resultado=cliente['Gestao_transportes']['Empresas'].aggregate([
            {
                '$lookup':{
                    'from': 'Linhas',
                    'localField': 'Nome',
                    'foreignField': 'empresaOperadora',
                    'as': 'juncao'
                }
            }
        ])
        return resultado
