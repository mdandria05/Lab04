from cabine import Cabine
class CDeluxe(Cabine):
    def __init__(self, cod, n_letti, ponte, prezzo, n_animali,stile):
        super().__init__(cod, n_letti, ponte, prezzo, n_animali)
        self.__prezzo = prezzo * 1.20
        self.__stile = stile
    def __str__(self):
        return f'{super().__str__()} | stile = {self.__stile}'
