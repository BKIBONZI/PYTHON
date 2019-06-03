# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    typeDict.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/18 08:20:40 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/20 10:43:06 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

progs = {'Yes' : ['Close to the Edge', 'Fragile'], 'Genesis':['Foxtrot', 'The Nursery Crime'],
        'ELP':['Brain Salad Surgery']}

progs ['King Crismon'] = ['red', 'Discipline']

for prog, albums in progs.items():
    print(prog, '=>', albums)

if progs.has_key('ELP'):
    del progs['ELP']
