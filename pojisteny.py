class Pojisteny():
    #vytvoření konstruktoru
    def __init__(self, jmeno, prijmeni, vek, telefon):
        #getter pro vstupní hodnoty
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon


    # Textová reprezentace pojištěného
    def __str__(self):
        return "{0}\t {1}\t {2}\t {3}".format(self.jmeno, self.prijmeni, self.vek, self.telefon)


