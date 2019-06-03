# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    boucle_for_SamMax.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/02 16:26:56 by bkibonzi          #+#    #+#              #
#    Updated: 2019/03/02 16:45:44 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

sequence = [ "a", "b", "c" ]
for element in sequence :
    print(element)

new_sequence = []
for element in sequence :
    new_sequence.append(element.upper())
    
print(new_sequence)

retour_sequence = [element.lower() for element in sequence]
print(retour_sequence)

sequence2 = [1, 2, 3]
print(sequence2)
sequence2 = [str(nombre) for nombre in sequence2 ]
print(sequence2)

