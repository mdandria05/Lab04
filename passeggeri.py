class Passeggeri:
    def __init__(self,cod,nome,cognome):
        self.__cod = cod
        self.__nome = nome
        self.__cognome = cognome
        self.__cabina = None

    @property
    def cod(self):
        return self.__cod

    @property
    def cabina(self):
        return self.__cabina
    @cabina.setter
    def cabina(self,cabina):
        self.__cabina = cabina

    def __str__(self):
        if self.__cabina is None:
            return f'{self.__cod} | {self.__nome} | {self.__cognome}'
        else: return f'{self.__cod} | {self.__nome} | {self.__cognome} | {self.__cabina}'
    def __repr__(self):
        return f'cod = {self.__cod} | nome = {self.__nome=} | cognome = {self.__cognome=}'
    def __eq__(self,cod):
        return self.__cod == cod