# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    boucle_for_SametMax.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/02 23:15:13 by bkibonzi          #+#    #+#              #
#    Updated: 2019/03/03 12:02:29 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

sequence = ["a", "b", "c"]

for element  in sequence :
    print(element)

new_sequence = []
for element in sequence :
    new_sequence.append(element.upper())
print(new_sequence)


new_sequence2 = []
new_sequence2 = [element.upper() for element in sequence]
print(new_sequence2)


new_sequence2 = [element.lower() for element in new_sequence2]
print(new_sequence2)

sequence3 = [1, 2, 3]
print([str(nombre) for nombre in sequence3])

print([nombre * 'a' for nombre in sequence3])

print(list(range(5)))

sequence4 = [(nombre, list(range(nombre))) for nombre in sequence3]
print(sequence4)

print(sequence4[-1])

print(sequence4[-1][0])

print(sequence4[-1][1])

nombres = range(10)
nombres_pairs = []
for nombre in nombres :
    if nombre % 2 == 0 :
        nombres_pairs.append(nombre)

print(list(nombres))
print("la suite")
print(nombres_pairs)

print([nombre for   nombre in nombres if nombre % 2 == 0])


