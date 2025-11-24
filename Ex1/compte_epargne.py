from compte_bancaire import CompteBancaire

class CompteEpargne(CompteBancaire):
    def __init__(self, titulaire, solde_initial=0, taux=0.02):
        super().__init__(titulaire, solde_initial)
        self._taux = taux

    def calculer_interet(self):
        return self.solde * self._taux
