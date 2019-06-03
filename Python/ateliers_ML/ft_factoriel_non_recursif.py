# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_factoriel_non_recursif.py                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/18 20:48:24 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/18 23:55:14 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_factoriel_non_recursif(num):
    num = num if num > 1 else 1
    j = 1
    for i in range(1, num +1):
        j = j * i
    return j


for i in range(1,6):
    print(i, '->', ft_factoriel_non_recursif(i))
