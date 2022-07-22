import ast
import json
import re
import time

from bson import ObjectId
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
        time.sleep(1)
        print(empresaBanco)
        resultado=colecaoEmpresas.insert_one(empresaBanco)
        return(resultado.inserted_id)
            
    def consultarEmpresaBanco_Por_Id(Id_Empresa):
        resultado=colecaoEmpresas.find_one({"_id": ObjectId(Id_Empresa)})
        return resultado

    def consultarEmpresaBanco_Por_Nome(self,nome):
        nome= re.compile(".*{}.*" .format(nome),re.IGNORECASE)
        resultado=colecaoEmpresas.find({"Nome": nome})
        if resultado:
            return resultado
        else:
            return None


    def alterarBanco():
        pass
    def excluirBanco():
        pass