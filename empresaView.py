from empresa import Empresa
from empresaDao import EmpresaDao

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
            print("A inserir no Banco...")
            empresaDao=EmpresaDao()
            resultado=empresaDao.inserirBanco(empresa)
            print("Empresa inserida com sucesso!")
            return("Empresa ID: {}" .format(resultado))
        else:
            print("Todos os campos precisam ser preenchidos! Por favor refaça a operação.")

    def montar_Dicionario(documento):
        return("{ " +"Cnpj: {} ".format(documento.get("Cnpj")), "Nome: {} ".format(documento.get("Nome")), "InicioOperação: {}" .format(documento.get("InicioOperação")),"FrotaTotal: {}" .format(documento.get("FrotaTotal")) , "Contato: {}" .format(documento.get("Contato")) , "FrotaArCondicioado: {}" .format(documento.get("FrotaArCondicioado"))+" }")
        #return("CNPJ: {}".format(documento.get("Cnpj")))

    def montar_Dicionario2(documento):
        return("{ " +"Cnpj: {} ".format(documento.get("Cnpj")), "Nome: {} ".format(documento.get("Nome")), "InicioOperação: {}" .format(documento.get("InicioOperação")),"FrotaTotal: {}" .format(documento.get("FrotaTotal")) , "Contato: {}" .format(documento.get("Contato")) , "FrotaArCondicioado: {}" .format(documento.get("FrotaArCondicioado")) , "Empresa Operadora: {}" .format(documento.get("empresaOperadora")), "Código: {}" .format(documento.get("Código")) +" }")
    
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
            for empr in resultado:
                #return EmpresaView.montar_Dicionario(empr)
                return EmpresaView.showEmpresa(empr)
        else:
                return resultado

    def consultarTudo():
        resultado=EmpresaDao.consultar_EmpresasLinhas()
        for empr in resultado:
            resul=EmpresaView.montar_Dicionario2(empr)
            print(empr)