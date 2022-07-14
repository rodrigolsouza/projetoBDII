import pymongo

class conexao:
    def __init__(self):
       
        self.cliente=None
        self.bancoDeDados=None
        self.colecao1=None


    def conectar(self):

        # Declaração das constantes necessárias na conexão
        BASE_DE_DADOS = "Gestao_transportes"
        COLECAO_1 = "empresas"
        STRING_DE_CONEXAO = "mongodb+srv://admin:admin@cluster0.ynpyc9f.mongodb.net/?retryWrites=true&w=majority"

        # Realização da conexão com o servidor na nuvem
        try:
            self.cliente = pymongo.MongoClient(STRING_DE_CONEXAO)
            self.bancoDeDados = self.cliente[BASE_DE_DADOS]
            self.colecao1 = self.bancoDeDados[COLECAO_1]
            
        #Exibição dos bancos já cadastrados no cluster
            print("list_database_names: ", self.cliente.list_database_names())

        # Mensagem de erro caso a conexão falhe
        except pymongo.errors.ConnectionFailure as errorConexion:
            print("Falha ao conectar-se ao MongoDB " + errorConexion)
        
