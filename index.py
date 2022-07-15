
from conexao import Conexao
from utilitarios import *

#Conexão com o banco de dados
conexao = Conexao()
conexao.conectar()

#Exibição do Menu de atividades operacionais
ShowMenu.menu_inicial()
ShowMenu.exibir_menu_inicial()

