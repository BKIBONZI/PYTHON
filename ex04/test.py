while True:
    try :
        a = input("entrez un entier: ")
        nombre=int(a)
        inverse=1/nombre
        print("l'inverse de %d est %f" % (nombre,inverse))
        break 

    except ZeroDivisionError:
        print("Erreur Division par Zéro !")

    except ValueError:
        print("Erreur:Valeur non-numerique")

