import sys

try : 

    nb1 = sys.argv[1]
    nb2 = sys.argv[2]

    somme = int(nb1) + int(nb2) 
    soustraction = int(nb1) - int(nb2)
    produit = int(nb1) * int(nb2) 
    division = int(nb1) / int(nb2) 
    modulo = int(nb1) % int(nb2) 

    print("Sum: {}".format(somme))
    print("Difference: {}".format(soustraction))
    print("Product: {}".format(produit))
    print("Quotient: {}".format(division))
    print("Remainder: {}".format(modulo))

except ZeroDivisionError as division:
    print("Voici l'erreur :", division)
    
