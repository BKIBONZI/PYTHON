
class Time :
    "Definition de la classe time"
    def __init__(self):
        self.heure =0
        self.minute = 0
        self.seconde = 0


    def affiche_heure(self) :
        print(str(self.heure)+":"+str(self.minute)+":"+str(self.seconde))


if __name__ == '__main__':
    instant = Time()
    instant.affiche_heure()


