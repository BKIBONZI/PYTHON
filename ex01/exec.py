import sys 

nb_arg = len(sys.argv) - 1
chaine = ""

if nb_arg > 1 : 
    for k in range(nb_arg) :
        j = k + 1
        chaine = chaine + " " + sys.argv[j]

    
#    print(" ".join(chaine.split()))
else :
    chaine = sys.argv[1]
    print(chaine)


while  nb_arg > 0 :
    mot = sys.argv[nb_arg]
    for i in reversed(mot) :
        if i.islower():
            print(i.upper(), end='')
        else :
            print(i.lower(), end='')
    if nb_arg != 1 :
        print(' ', end='')
    nb_arg = nb_arg - 1


