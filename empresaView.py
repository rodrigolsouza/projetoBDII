import time
from empresa import Empresa
from empresaDao import EmpresaDao
from linhaView import LinhaView

class EmpresaView():
    def __init__(self):
        pass

    def inserirEmpresa():
        print("Digite os dados da sua Empresa de transportes")
        cnpj=input("CNPJ: ").upper()
        nome=input("NOME: ").upper()
        inicioOperação=input("INÍCIO DA OPERAÇÃO: ").upper()
        frotaTotal=input("FROTA TOTAL: ").upper()
        contato=input("CONTATO: ").upper()
        frotaArCondicionado=input("FROTA COM AR-CONDICIONADO: ").upper()
        print("\n")

        if len(cnpj)!=0 and len(nome)!=0 and len(inicioOperação)!=0 and len(frotaTotal)!=0 and len(contato)!=0 and len(frotaArCondicionado)!=0:
            empresa=Empresa(cnpj,nome,inicioOperação,frotaTotal,contato,frotaArCondicionado)
            empresaDao=EmpresaDao()
            resultado=empresaDao.inserirBanco(empresa)
            if (resultado):
                print("Empresa inserida com sucesso!")
            #return("Empresa ID: {}" .format(resultado))
            else:
                print("Erro no cadastro, tente novamente!")
        else:
            print("Todos os campos precisam ser preenchidos! Por favor refaça a operação.")

    def showEmpresa(documento):
        print("\n")
        print("******** CONSULTA EFETUADA COM SUCESSO! *********")
        print("\n*************************************************")
        print("CNPJ: ", documento.get("Cnpj"))
        print("NOME: ", documento.get("Nome"))
        print("CONTATO: ", documento.get("Contato"))
        print("INÍCIO DA OPERAÇÃO: ", documento.get("InicioOperação"))
        print("FROTA TOTAL: ", documento.get("FrotaTotal"))
        print("FROTA COM AR-CONDICIONADO: ", documento.get("FrotaArCondicioado"))
        print("\n*************************************************")
        

    def consultarEmpresa_Por_Nome():
        nome=input("Digite o nome da empresa: ").upper()
        empresaDao=EmpresaDao()
        resultado=empresaDao.consultarEmpresaBanco_Por_Nome(nome)
        
        if resultado:
            time.sleep(1)
            for empr in resultado:
                return EmpresaView.showEmpresa(empr)
            time.sleep(1)
        else:
                return "Empresa não cadastrada no banco de dados"

    def consultarTudo():
        resultado=EmpresaDao.consultar_EmpresasLinhas()
        print("\n")
        print("**** CONFIRA LINHAS E EMPRESAS CADASTRADAS! *****")
        for empr in resultado:
            time.sleep(1)
            EmpresaView.showTudo1(empr)
            time.sleep(1)
            for linha in empr['juncao']:
                LinhaView.showLinha_comArCondicionado(linha)
            time.sleep(1)
        if not resultado:
            print("Empresa não cadastrada no banco de dados")
            

    def showTudo1(documento):
        
        print("\n*************************************************")
        print("LINHAS OPERADAS PELA A EMPRESA:",documento.get("Nome"))
        print("SAC: ", documento.get("Contato"))
       