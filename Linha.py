from LinhaDao import *


class Linha:
    def __init__(self):
        pass

    def get_codigo(self):
        return self.__codigo


    def get_nome(self):
        return self.__nome


    def get_tarifa(self):
        return self.__tarifa


    def get_frota(self):
        return self.__frota


    def get_integraçao(self):
        return self.__integraçao


    def get_ar_condicionado(self):
        return self.__arCondicionado


    def set_codigo(self, value):
        self.__codigo = value


    def set_nome(self, value):
        self.__nome = value


    def set_tarifa(self, value):
        self.__tarifa = value


    def set_frota(self, value):
        self.__frota = value


    def set_integraçao(self, value):
        self.__integraçao = value


    def set_ar_condicionado(self, value):
        self.__arCondicionado = value


    def inserirLinha(self):
        print("Digite os seguintes dados da Linha de Ônibus: ")
        linha=Linha()

        codigo=input("CODIGO:")
        linha.set_codigo(codigo)

        nome=input("NOME:")
        linha.set_nome(nome)

        tarifa=input("TARIFA ")
        linha.set_tarifa(tarifa)

        frota=input("FROTA: ")
        linha.set_frota(frota)

        integração=("INTEGRAÇÃO? ")
        linha.set_integraçao(integração)

        arCondicionado=("ARCONDICIONADO? ")
        linha.set_ar_condicionado(arCondicionado)
        LinhaDao.inserir(linha)
