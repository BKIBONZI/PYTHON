# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    iterateurs_devpointcom.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/21 04:18:35 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/21 05:37:31 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

chaine = 'hello world'
for lettre in chaine :
    print(lettre, end ='')

print()
chaine = 'hello world'
iterateur = iter(chaine)
print(iterateur)

print()
chaine = ('h','e','l','l','o',' ','w','o','r','l','d')
iterateur = chaine.__iter__()
print(iterateur)

print()
chaine = ['h','e','l','l','o',' ','w','o','r','l','d']
iterateur = chaine.__iter__()
print(iterateur)


chaine = 'Hello World'
iterateur = iter(chaine)
for i in range(len(chaine)) :
    print(iterateur.next ())





