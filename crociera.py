from csv import reader
import cabine
from cabine import Cabine
from passeggeri import Passeggeri
from cDeluxe import CDeluxe

class Crociera:
    caricamento = False
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.__cabine = []
        self.__passeggeri = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""
        # TODO
        if not self.caricamento:
            try:
                with open(file_path) as infile:
                    csvReader = reader(infile)
                    for row in csvReader:
                        row = [campo for campo in row if campo]
                        if row[0].startswith("C"):
                            if len(row) <= 4: self.__cabine.append(Cabine(row[0],row[1],row[2],float(row[3]),0))
                            elif row[4].isdigit(): self.__cabine.append(Cabine(row[0],row[1],row[2],float(row[3]),int(row[4])))
                            else: self.__cabine.append(CDeluxe(row[0], row[1], row[2], float(row[3]), 0,row[4]))
                        elif row[0].startswith("P"):
                            self.__passeggeri.append(Passeggeri(row[0],row[1],row[2]))
                self.caricamento = True
            except FileNotFoundError:
                raise FileNotFoundError("File not found")
        else: print("File già caricato")

    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO
        for cabina in self.__cabine:
            if cabina.cod == codice_cabina:
                for passeggero in self.__passeggeri:
                    if codice_passeggero == passeggero.cod:
                        passeggero.cabina = codice_cabina
                        print(f'Passeggero: {codice_passeggero} associato alla cabina: {codice_cabina}')
                        return None
            else: raise Exception('Associazione non avvenuta')

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO
        cabine_ordinate = sorted(self.__cabine, key=lambda x: x.prezzo)
        return cabine_ordinate

    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO
        for passeggero in self.__passeggeri:
            print(passeggero)
