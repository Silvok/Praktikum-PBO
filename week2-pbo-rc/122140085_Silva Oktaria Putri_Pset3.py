import random

class Individu:
    def __init__(self, gol_darah):
        self.gol_darah = gol_darah

    def pilih_alel(self):
        return random.choice(self.gol_darah)

class Ortu(Individu):
    pass

class Anak(Individu):
    def __init__(self, ayah, ibu):
        super().__init__([ayah.pilih_alel(), ibu.pilih_alel()])

    def gol_darah_anak(self):
        alel = sorted(self.gol_darah)
        if alel == ['A', 'A']:
            return 'Golongan Darah A'
        elif alel == ['A', 'B']:
            return 'Golongan Darah AB'
        elif alel == ['A', 'O']:
            return 'Golongan Darah A'
        elif alel == ['B', 'B']:
            return 'Golongan Darah B'
        elif alel == ['B', 'O']:
            return 'Golongan Darah B'
        elif alel == ['O', 'O']:
            return 'Golongan Darah O'

gol_darah_ibu = input("Masukkan golongan darah ibu (A, B, AB, atau O): ").upper()
gol_darah_ayah = input("Masukkan golongan darah ayah (A, B, AB, atau O): ").upper()
ayah = Ortu(gol_darah_ayah)
ibu = Ortu(gol_darah_ibu)
anak = Anak(ayah, ibu)
print("Alel anak:", anak.gol_darah)
print("Golongan darah anak:", anak.gol_darah_anak())
