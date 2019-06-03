# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generateur_devpoitcom.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/21 06:14:18 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/21 07:08:26 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def mon_generateur(data):
    for value in data :
        yield value 

if __name__ == ('__main__'):
    generateur = mon_generateur("hello world")
    print(generateur)
    for value in generateur :
        print(value)
