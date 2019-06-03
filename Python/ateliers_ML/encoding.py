
#                                                                              #
#                                                         :::      ::::::::    #
#    encoding.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/16 01:22:06 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/16 02:13:14 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# - * - coding: utf-8 - # -
#! /Sgoinfre/groinfre/Perso/bkibonzi/miniconda3/bin/python

print(7 * 3)

a = 7 * 3 + \
5 / 2

print(a)

b = ['a', 'b', 'c',
'd', 'e']

print(b)

c = range(1,
11)

for i in c:
    print(i)

print(list(c))

for i in [234, 654, 378, 798]:
    if i % 3 == 0:
        print(i,'/3 =', i/3)
