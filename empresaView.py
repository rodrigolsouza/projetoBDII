from empresa import Empresa
from empresaDao import EmpresaDao

class EmpresaView():
    def __init__(self):
        pass

    def inserirEmpresa():
        pass
    def inserirEmpresa():
        print("Digite os dados da sua Empresa de transportes")
        cnpj=input("CNPJ: ")
        nome=input("NOME: ")
        inicioOperação=input("INÍCIO DA OPERAÇÃO: ")
        frotaTotal=input("FROTA TOTAL: ")
        contato=input("CONTATO: ")
        frotaArCondicionado=input("FROTA COM AR CONDICIONADO: ")
        print("\n")

        if len(cnpj)!=0 and len(nome)!=0 and len(inicioOperação)!=0 and len(frotaTotal)!=0 and len(contato)!=0 and len(frotaArCondicionado)!=0:
            empresa=Empresa(cnpj,nome,inicioOperação,frotaTotal,contato,frotaArCondicionado)
            empresaDao=EmpresaDao()
            empresaDao.inserirBanco(empresa)
        else:
            print("Todos os campos precisam ser preenchidos! Por favor refaça a operação.")

