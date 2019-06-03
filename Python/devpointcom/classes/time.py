
class Time :
    "Definition de la classe time"

    def affiche_heure(self) :
        print(str(self.heure)+":"+str(self.minute)+":"+str(self.seconde))


if __name__ == '__main__':
    instant = Time()
    instant.heure = 11
    instant.minute = 34
    instant.seconde = 25
    instant.affiche_heure()


