import pymongo
from utilitarios import *
from Linha import *
from Empresa import *


#Declaração das constantes necessárias na conexão
BASE_DE_DADOS="Gestao_transportes"
COLECAO_1="empresas"
STRING_DE_CONEXAO="mongodb+srv://admin:admin@cluster0.ynpyc9f.mongodb.net/?retryWrites=true&w=majority"

try:
    #Realização da conexão com o servidor na nuvem
    cliente = pymongo.MongoClient(STRING_DE_CONEXAO)
    bancoDeDados=cliente[BASE_DE_DADOS]
    colecao1=bancoDeDados[COLECAO_1]

    #Teste para comprovar que o cluster está funcionando
    print("list_database_names: ", cliente.list_database_names())
    
#Mensagem de erro caso a conexão falhe
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Falha ao conectar-se ao MongoDB " +errorConexion)

#Exibição do Menu de atividades operacionais
menu_inicial()
exibir_menu_inicial()

