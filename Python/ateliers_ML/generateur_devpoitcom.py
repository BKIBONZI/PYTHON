# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generateur_devpoitcom.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/21 06:14:18 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/21 06:19:22 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def mon_generateur():
    yield 'h'
    yield 'e'
    yield 'l'
    yield 'l'
    yield 'o'
    yield ' '
    yield 'w'
    yield 'o'
    yield 'r'
    yield 'l'
    yield 'd'

if __name__ == ('__main__'):
    generateur = mon_generateur()
    print(generateur)
    for value in generateur :
        print(value)
