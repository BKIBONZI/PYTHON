def text_analyzer(v_text) :

    liste = v_text.split()
    print(liste)

    nb_maj = 0
    nb_min = 0
    nb_spaces = 0
    nb_ponct = 0
    nb_caract = 0 

    for i in liste :
        nb_caract += 1 
        if i.isupper() :
            nb_maj += 1
        if i.islower() :
            nb_min += 1
        if i in (" ",' ') :
            nb_spaces += 1
        if i in ('!', '?') :
            nb_ponct +=1

    print("The text contains {} ".format(nb_caract))
    print("- {} upper letters".format(nb_maj))
    print("- {} lower letters".format(nb_min))
    print("- {} punctuation marks".format(nb_ponct))
    print("- {} spaces".format(nb_spaces))

