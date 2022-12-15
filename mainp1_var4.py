from pojisteny import Pojisteny
from pojistovna import Pojistovna

pojistovna = Pojistovna
pojistovna_seznam = [["David", "Capka", 33, 777333111], ["David", "Jancik", 27, 777333112]] #seznam
pomocny_list = []
while True:
    print("Vyberte si akci ")
    print("Přidat nového pojištěného - 1")
    print("Vypsat všechny pojištěné - 2")
    print("Vyhledat pojištěného - 3")
    print("Konec - 4")
    volba = int(input())
    #print()
    if (volba > 4) or (volba < 1):
        print("Chybné zadání.")

    if (volba == 1):
        jmeno = input("Zadejte jmeno: ")
        prijmeni = input("Zadejte příjmení: ")
        vek = int(input("Zadejte věk: "))
        telefon = int(input("Zadejte telefon: "))
        print()
        novy_pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        pojistovna_seznam.append(novy_pojisteny)
        pomocny_list.append(novy_pojisteny)
        print("Nový pojištěný je\n{0}".format(novy_pojisteny))
        print("Data byla uložena pokračujte libovolnou klávesou")
        print()
    if (volba == 2):
        print("Výpis všech pojištěných je:")
        seznam_poj_1 = ["David", "Capka", 33, 777333111]
        iterator_1 = iter(seznam_poj_1)
        for hodnota in iterator_1:
            print(hodnota, end="\t")
        print()
        seznam_poj_2 = ["David", "Jancik", 27, 777333118]
        iterator_2 = iter(seznam_poj_2)
        for hodnota in iterator_2:
            print(hodnota, end="\t")
        print()
        print("a nebo:")
        print("\n".join(map(str, pojistovna_seznam)))
        print()

    if (volba == 3):
        hledane_jmeno = input("Zadejte jméno pojištěného: \n")
        hledane_prijmeni = input("Zadejte příjmení: \n")

        print("Vyhledání pojištěného mi BOHUŽEL nefunguje")

        #potřebuji prohledat jednotlivé položky seznamu, které jsou také seznamy a porovnat je s vyhledávacím kritériem
        print()

    if (volba == 4):
        print("Konec")
        print()







