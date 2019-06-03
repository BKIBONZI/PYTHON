# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filter_avec_liste_intension.py                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/03 12:03:53 by bkibonzi          #+#    #+#              #
#    Updated: 2019/03/03 12:33:57 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

nombres = range(10)
sommes = []
for nombre in nombres :
    if nombre % 2 == 0 :
        somme = 0
        for i in range (nombre) : 
            somme += i
        sommes.append(somme)

print(sommes)

sommes2 =[]
for nombre in nombres :
    if nombre % 2 == 0:
        sommes2.append(sum(range(nombre)))

print(sommes2)

print([sum(range(nombre)) for nombre in nombres if nombre % 2 == 0])
print([sum(range(nombre)) for nombre in range(0,10,2)])
