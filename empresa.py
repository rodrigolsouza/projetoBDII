class Empresa:
    def __init__(self, cnpj, nome, inicioOperação, frotaTotal, contato, frotaArCondicionado):
        self.Cnpj = cnpj
        self.Nome = nome
        self.InicioOperação = inicioOperação
        self.FrotaTotal = frotaTotal
        self.Contato = contato
        self.FrotaArCondicioado = frotaArCondicionado

    def get_cnpj(self):
        return self.Cnpj


    def get_nome(self):
        return self.Nome


    def get_inicio_operação(self):
        return self.InicioOperação


    def get_frota_total(self):
        return self.FrotaTotal


    def get_contato(self):
        return self.Contato


    def get_frota_ar_condicioado(self):
        return self.FrotaArCondicioado


    def set_cnpj(self, value):
        self.Cnpj = value


    def set_nome(self, value):
        self.Nome = value


    def set_inicio_operação(self, value):
        self.InicioOperação = value


    def set_frota_total(self, value):
        self.FrotaTotal = value


    def set_contato(self, value):
        self.Contato = value


    def set_frota_ar_condicioado(self, value):
        self.FrotaArCondicioado = value
