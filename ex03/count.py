def text_analyzer(v_ph = "") :

#    liste = v_text.split()
#    print(liste)


    nb_maj = 0
    nb_min = 0
    nb_spaces = 0
    nb_ponct = 0
    nb_caract = 0 

    while (len(v_ph) == 0):
        v_ph = input("What is the text to analyse?")

    print(v_ph)

    l_ph = len(v_ph)

    for i in range(l_ph) :
        nb_caract += 1 
        if v_ph[i].isupper() :
            nb_maj += 1
        if v_ph[i].islower() :
            nb_min += 1
        if v_ph[i] in (' ','\t','\f','\v','\n') :
            nb_spaces += 1
        if v_ph[i] in (',',';','.',':','!', '?') :
            nb_ponct +=1

    print("The text contains {} characters:".format(nb_caract))
    print("- {} upper letters".format(nb_maj))
    print("- {} lower letters".format(nb_min))
    print("- {} punctuation marks".format(nb_ponct))
    print("- {} spaces".format(nb_spaces))
