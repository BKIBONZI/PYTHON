# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    typeList.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/18 00:29:58 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/18 02:39:35 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

progs = ['Yes', 'Genesis', 'Pink Floyd', 'Elp']

for prog in progs :
    print(prog)

print()

progs[-1] = 'King Crimson'
for prog in progs :
    print(prog)

print()
progs.append('camel')
for prog in progs :
    print(prog)

print()
progs.remove('Pink Floyd')
for prog in progs :
    print(prog)

print()
progs.sort()
for prog in progs :
    print(prog)

print()
progs.reverse()
for prog in progs :
    print(prog)
