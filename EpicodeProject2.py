import numpy as np

#Parte 1 - Variabili e tipi di dati

nome1 = "Mario"
cognome1 = "Rossi"
codice_fiscale1 = "RSSMRA81A01F205X"
età1 = 45
peso1 = 78.5
analisi1 = ["emocromo", "glicemia", "colesterolo"]

nome2 = "Arianna"
cognome2 = "Moretti"
codice_fiscale2 = "MRTNNA91B42F205Y"
età2 = 35
peso2 = 62.3
analisi2 = ["glicemia", "colesterolo", "trigliceridi"]

nome3 = "Enea"
cognome3 = "Bellini"
codice_fiscale3 = "BLLNEA76C15F205Z"
età3 = 50
peso3 = 84.7
analisi3 = ["emocromo", "glicemia", "colesterolo"]


#Parte 2 - Classi e OOP

class Paziente:
    def __init__(self, nome, cognome, codice_fiscale, età, peso, analisi_effettuate):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.età = età
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate

    def scheda_personale(self):
        return ( f"Nome: {self.nome} {self.cognome}", f"Codice fiscale: {self.codice_fiscale}", f"Età: {self.età}", f"Peso: {self.peso} kg", f"Analisi effettuate: {self.analisi_effettuate}")
    
class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome = nome
        self.cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        print( f"Il medico {self.nome} {self.cognome} ", f"sta visitando il paziente {paziente.nome} {paziente.cognome}")

class Analisi:
    def __init__(self, tipo, risultato):
        self.tipo = tipo
        self.risultato = risultato

    def valuta(self):
        if self.tipo == "glicemia":
            if 70 <= self.risultato <= 100:
                return "Valore nella norma"
            else:
                return "Valore fuori dalla norma"

        if self.tipo == "colesterolo":
            if self.risultato <= 200:
                return "Valore nella norma"
            else:
                return "Valore fuori dalla norma"

paziente_esempio = Paziente( "Mario", "Rossi", "RSSMRA81A01F205X", 45, 78.5, ["emocromo", "glicemia", "colesterolo"])

medico_esempio = Medico( "Luca",  "Bianchi", "Medicina generale")

analisi_esempio = Analisi( "glicemia", 92)

print(paziente_esempio.scheda_personale())
medico_esempio.visita_paziente(paziente_esempio)
print(analisi_esempio.valuta())


#Parte 3 - Uso di NumPy

risultati_esame = np.array([85, 92, 78, 105, 96, 88, 110, 75, 99, 90])

print(risultati_esame)

media = np.mean(risultati_esame)
massimo = np.max(risultati_esame)
minimo = np.min(risultati_esame)
deviazione_standard = np.std(risultati_esame)

print("Media:", media)
print("Valore massimo:", massimo)
print("Valore minimo:", minimo)
print("Deviazione standard:", deviazione_standard)


#Parte 4 - Integrazione Numpy e OOP

class Paziente:
    def __init__( self, nome, cognome, codice_fiscale, età, peso, analisi_effettuate, risultati_analisi):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.età = età
        self.peso = peso
        self.analisi_effettuate = analisi_effettuate
        self.risultati_analisi = np.array(risultati_analisi)

    def scheda_personale(self):
        return ( f"Nome: {self.nome} {self.cognome}", f"Codice fiscale: {self.codice_fiscale}", f"Età: {self.età}", f"Peso: {self.peso} kg", f"Analisi effettuate: {self.analisi_effettuate}")

    def statistiche_analisi(self):
        media = np.mean(self.risultati_analisi)
        minimo = np.min(self.risultati_analisi)
        massimo = np.max(self.risultati_analisi)
        deviazione_standard = np.std(self.risultati_analisi)

        return ( f"Media: {media}", f"Minimo: {minimo}", f"Massimo: {massimo}", f"Deviazione standard: {deviazione_standard}")

paziente_esempio = Paziente( "Mario", "Rossi", "RSSMRA81A01F205X", 45, 78.5, ["emocromo", "glicemia", "colesterolo"], [85, 92, 180])

print(paziente_esempio.statistiche_analisi())


#Parte 5 - Applicazione completa

def main():

    medico1 = Medico("Luca", "Bianchi", "Medicina generale")
    medico2 = Medico("Giulia", "Verdi", "Cardiologia")
    medico3 = Medico("Paolo", "Romano", "Endocrinologia")

    paziente1 = Paziente("Mario", "Rossi", "RSSMRA81A01F205X", 45, 78.5, ["emocromo", "glicemia", "colesterolo"], [85, 92, 180])

    paziente2 = Paziente( "Arianna", "Moretti", "MRTNNA91B42F205Y", 35, 62.3, ["glicemia", "colesterolo", "trigliceridi"],[90, 175, 115])

    paziente3 = Paziente( "Enea", "Bellini", "BLLNEA76C15F205Z", 50, 84.7, ["emocromo", "glicemia", "colesterolo"], [88, 102, 190])

    paziente4 = Paziente( "Laura", "Conti", "CNTLRA88D44F205A", 38, 59.8, ["emocromo", "glicemia", "colesterolo"], [82, 95, 165])

    paziente5 = Paziente( "Marco", "Ferrari", "FRRMRC72E20F205B", 54, 81.2, ["emocromo", "glicemia", "colesterolo"], [95, 108, 195])

    pazienti = [ paziente1, paziente2, paziente3, paziente4, paziente5]

    medico1.visita_paziente(paziente1)
    medico2.visita_paziente(paziente2)
    medico3.visita_paziente(paziente3)
    medico1.visita_paziente(paziente4)
    medico2.visita_paziente(paziente5)

    for paziente in pazienti:
        print(paziente.scheda_personale())
        print(paziente.statistiche_analisi())


if __name__ == "__main__":
    main()
