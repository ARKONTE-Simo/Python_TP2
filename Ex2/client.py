from compte_bancaire import CompteBancaire

class Client:
    def __init__(self, nom):
        self.nom = nom
        self.compte = CompteBancaire()

    def afficher(self):
        print(f"Client : {self.nom}, Solde : {self.compte.get_solde()}€")
