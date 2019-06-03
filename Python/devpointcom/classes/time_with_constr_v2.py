
class Time :
    "Definition de la classe time"
    def __init__(self, hh = 0, mm=0, ss=0):
        self.heure =hh
        self.minute =mm
        self.seconde =ss


    def affiche_heure(self) :
        print(str(self.heure)+":"+str(self.minute)+":"+str(self.seconde))


if __name__ == '__main__':
    instant = Time(10,15,18)
    instant.affiche_heure()


