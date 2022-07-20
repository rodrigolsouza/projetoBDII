import pymongo
import time
#Declaração das constantes necessárias na conexão
STRING_DE_CONEXAO="mongodb+srv://admin:admin@cluster0.ynpyc9f.mongodb.net/?retryWrites=true&w=majority"
BASE_DE_DADOS="Gestao_transportes"
COLECAO_LINHAS="Linhas"
COLECAO_EMPRESAS="Empresas"

#Realização da conexão com o servidor na nuvem e criação do banco e collection
cliente = pymongo.MongoClient(STRING_DE_CONEXAO)
bancoDeDados=cliente[BASE_DE_DADOS]
colecaoLinhas=bancoDeDados[COLECAO_LINHAS]
colecaoEmpresas=bancoDeDados[COLECAO_EMPRESAS]


def conectar():
    print("Conectando com o servidor...\n")
    time.sleep(1)
    try:
        cliente
        print("Conectado com sucesso! \n")
        #Teste para comprovar que o cluster está funcionando
        time.sleep(1)
        print("list_database_names: ", cliente.list_database_names())
        
    #Mensagem de erro caso a conexão falhe
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Falha ao conectar-se ao MongoDB " +errorConexion)
