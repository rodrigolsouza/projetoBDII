class Linha:
    def __init__(self,codigo,nome,tarifa,frota,integração,arCondicionado):
        self.Código= codigo
        self.Nome= nome
        self.Tarifa= tarifa
        self.Frota= frota
        self.Integração=integração
        self.ArCondicionado=arCondicionado
    
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
