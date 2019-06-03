# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generateur_devpoitcom.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/21 06:14:18 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/21 07:08:50 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def mon_generateur(data):
    iterateur = iter(data)
    for idx in range(len(data)):
        yield iterateur.next()

if __name__ == ('__main__'):
    generateur = mon_generateur("hello world")
    print(generateur)
    for value in generateur :
        print(value)
