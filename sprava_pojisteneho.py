from pojisteny import Pojisteny


class Sprava_pojisteneho():
    def __init__(self):
        self.seznam_pojistencu = []

    def pridej_pojistence(self, pojisteny):
        self.seznam_pojistencu.append(pojisteny)

    def zobraz_seznam(self):
        for pojisteny in self.seznam_pojistencu:
            print(pojisteny)

    def vyhledej_pojistence(self, jmeno, prijmeni):
        for hledany in self.seznam_pojistencu:
            if hledany.jmeno == jmeno and hledany.prijmeni == prijmeni:
                return hledany
        else:
            return None