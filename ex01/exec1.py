import sys 

nb_arg = len(sys.argv) - 1

while  nb_arg > 0 :
    mot = sys.argv[nb_arg]
    for i in reversed(mot) :
        if i.islower():
            print(i.upper(), end=' ')
        else :
            print(i.lower(), end=' ')
    nb_arg = nb_arg - 1
    print(' ', end =' ')


