from pojisteny import Pojisteny
from sprava_pojisteneho import Sprava_pojisteneho

sprava = Sprava_pojisteneho()

def menu():
    print("-----------------------")
    print("Evidence pojištených")
    print("-----------------------")
    print("Vyberte akci: ")
    print("1 — Přidat nového pojištěného")
    print("2 — Vypsat všechny pojištěné")
    print("3 — Vyhledat pojišténého")
    print("4 — Konec")

def zpracuj_volbu(volba):
    if volba == "1":
        pridej_pojisteneho()
    elif volba == "2":
        vypis_pojistene()
    elif volba == "3":
        vyhledej_pojisteneho()
    elif volba == "4":
        return False
    else:
        print("Neplatná volba.")

    return True

def pridej_pojisteneho():
    print("Zadejte jméno pojištěného:")
    jmeno = input()
    print("Zadejte příjmení:")
    prijmeni = input()
    print("Zadejte telefonní číslo:")
    telefonni_cislo = input()
    print("Zadejte věk:")
    vek = input()
    pojisteny = Pojisteny(jmeno, prijmeni, vek, telefonni_cislo)
    sprava.pridej_pojistence(pojisteny)
    print("Data byla uložena. Pokračujte klávesou dle požadované akce.")

def vypis_pojistene():
    sprava.zobraz_seznam()

def vyhledej_pojisteneho():
    print("Zadejte jméno pojištěného:")
    jmeno = input()
    print("Zadejte příjmení:")
    prijmeni = input()
    hledany = sprava.vyhledej_pojistence(jmeno, prijmeni)
    if hledany:
        print(hledany)
    else:
        print("Pojištěný nebyl nalezen.")



def main():
    while True:
        menu()
        volba = input()
        """if zpracuj_volbu(volba) == True:
            continue"""
        if zpracuj_volbu(volba) == False:
            break


main()


"""if __name__ == "__main__":
    main()"""

