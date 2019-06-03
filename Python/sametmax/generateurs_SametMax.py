# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generateurs_SametMax.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/03 13:37:55 by bkibonzi          #+#    #+#              #
#    Updated: 2019/03/03 15:15:52 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

liste = [sum(range(nombre)) for nombre in range (0,10,2)]
for nombre in liste :
    print(nombre)
print(liste) 
liste[0]

generateur = (sum(range(nombre)) for nombre in range(0,10,2))
for nombre in generateur : 
    print(nombre)
print(generateur)
generateur[0]
