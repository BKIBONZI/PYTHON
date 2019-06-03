
class Point :
    "Definition de la classe Point"
    
class Rectangle :
    "Definition de la class rectangle"

    def trouveCentre(box) :
        p = Point()
        p.x = box.coin.x + box.largeur/2.0
        p.y = box.coin.y + box.hauteur/2.0
        return p


if __name__ == '__main__':
    boite = Rectangle()
    boite.largeur = 50.0
    boite.longueur = 35.0
    boite.coin = Point()
    boite.coin.x = 12.0
    boite.coin.y = 27.0
    print(boite.coin.x)
    centre = boite.trouveCentre(boite)
    print (centre.x, centre.y)


