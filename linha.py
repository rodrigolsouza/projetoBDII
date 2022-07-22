class Linha:
    def __init__(self,codigo,nome,tarifa,frota,integração,arCondicionado):
        self.Código= codigo
        self.Nome= nome
        self.Tarifa= tarifa
        self.Frota= frota
        self.Integração=integração
        self.ArCondicionado=arCondicionado
    
    def get_codigo(self):
        return self.Código


    def get_nome(self):
        return self.Nome


    def get_tarifa(self):
        return self.Tarifa


    def get_frota(self):
        return self.Frota


    def get_integraçao(self):
        return self.Integração


    def get_ar_condicionado(self):
        return self.ArCondicionado


    def set_codigo(self, value):
        self.Código = value


    def set_nome(self, value):
        self.Nome = value


    def set_tarifa(self, value):
        self.Tarifa = value


    def set_frota(self, value):
        self.Frota = value


    def set_integraçao(self, value):
        self.Integração = value


    def set_ar_condicionado(self, value):
        self.ArCondicionado = value
