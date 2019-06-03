# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generateur_extraitmot_fichiers_SametMax.p          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/03 17:21:46 by bkibonzi          #+#    #+#              #
#    Updated: 2019/03/03 18:08:36 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

def extraire_mots(dossier):
    for fichier in os.listdir(dossier):
        with open(os.path.join(dossier, fichier)) as f:
            for ligne in f:
                for mot in ligne.split():
                    if len(mot) > 3:
                        yield mot

if __name__ == '__main__':
    for mot in extraire_mots("dossier_test"):
         print(mot)

