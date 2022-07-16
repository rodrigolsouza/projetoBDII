class Empresa:
    def __init__(self, cnpj, nome, inicioOperação, frotaTotal, contato, frotaArCondicionado):
        self._cnpj = cnpj
        self._nome = nome
        self._inicioOperação = inicioOperação
        self._frotaTotal = frotaTotal
        self._contato = contato
        self._frotaArCondicioado = frotaArCondicionado

    def get_cnpj(self):
        return self.__cnpj


    def get_nome(self):
        return self.__nome


    def get_inicio_operação(self):
        return self.__inicioOperação


    def get_frota_total(self):
        return self.__frotaTotal


    def get_contato(self):
        return self.__contato


    def get_frota_ar_condicioado(self):
        return self.__frotaArCondicioado


    def set_cnpj(self, value):
        self.__cnpj = value


    def set_nome(self, value):
        self.__nome = value


    def set_inicio_operação(self, value):
        self.__inicioOperação = value


    def set_frota_total(self, value):
        self.__frotaTotal = value


    def set_contato(self, value):
        self.__contato = value


    def set_frota_ar_condicioado(self, value):
        self.__frotaArCondicioado = value
