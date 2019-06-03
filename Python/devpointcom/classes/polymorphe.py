class Atome :
    """atomes simplifies, choisis parmmi les 10 premiers éléments du TP"""
    table = [None, ('hydrogène', 0), ('hélium',2), ('lithium',4), ('berylium',5),
            ('bore',6), ('carbone',6), ('azote',7), ('oxygène',8), ('fluor',10), 
            ('néon', 10)]

    def __init__(self, nat):
            "le num atomique deternmine le nombre de protons, d'electrons et  de neutrons"
            self.np, self.ne = nat, nat   # nat = numero atomique 
            self.nn = Atome.table[nat][1]  # nb de neutrons trouves dans la table 

    def affiche(self):
            print() 
            print("Nom de l'element :", Atome.table[self.np][0])
            print("%s protons, %s electrons, %s neutrons" % (self.np, self.ne, self.nn))

class Ion(Atome) :
    """les ions sont les atomes qui ont gagné ou perdu des electrons"""

    def __init__(self, nat, charge) :
        "le num atomique et la charge electrique determinent l'ion"
        Atome.__init__(self, nat)
        self.ne = self.ne - charge 
        self.charge =  charge 

    def affiche(self):
        "cette methode remplace celle heritee de la classe parente"
        Atome.affiche(self)             #...tout en utilisant elle-même !
        print("Particule electrisee. charge =", self.charge)

if __name__ == '__main__' :
    a1 = Atome(5)
    a2 = Ion(3,1)
    a3 = Ion(8, -2)
    a1.affiche()
    a2.affiche()
    a3.affiche()







