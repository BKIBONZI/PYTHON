# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_enumerate.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/03/01 12:49:44 by bkibonzi          #+#    #+#              #
#    Updated: 2019/03/01 12:55:07 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def enumerate(liste):
    for i in range(len(liste)):
        yield i, liste[i]

for i, j in enumerate(["a", "b", "c"]):
    print(i, j)
