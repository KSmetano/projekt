class Pojistovna:
    def __init__(self, pojisteny):
        self.pojisteny = pojisteny

    def __str__(self):
        return "Výpis všech pojištěných je {0}\n".format(self.pojisteny)


