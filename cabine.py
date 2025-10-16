class Cabine:
    def __init__(self, cod, n_letti, ponte, prezzo, n_animali):
        self.__cod = cod
        self.__n_letti = n_letti
        self.__ponte = ponte
        self.__prezzo = prezzo if n_animali == 0 else prezzo * (1 + 0.10 * n_animali)
        self.__n_animali = n_animali
    @property
    def cod(self):
        return self.__cod
    @property
    def prezzo(self):
        return self.__prezzo
    def __str__(self):
        return f'cod = {self.__cod} | numero letti = {self.__n_letti} | ponte = {self.__ponte} | prezzo = {self.prezzo} | massimo animali = {self.__n_animali}'

