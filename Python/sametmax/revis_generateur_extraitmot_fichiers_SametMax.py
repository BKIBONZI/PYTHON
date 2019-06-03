# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    revis_generateur_extraitmot_fichiers_Same          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/03 21:58:17 by bkibonzi          #+#    #+#              #
#    Updated: 2019/03/03 22:09:50 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os 

def extraire_mots(dossier) :
    for fichier in os.listdir(dossier) :
        with open(os.path.join(dossier, fichier)) as f :
                for ligne in f :
                    for mot in ligne.split() :
                        if len(mot) > 3 :
                            yield mot

for mot in extraire_mots("dossier_test") : 
    print(mot)
