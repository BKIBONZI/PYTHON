# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_factoriel_recursif.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/18 20:18:57 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/18 20:27:28 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_factoriel_recursif(num) :
    if (num <= 1):
        return 1
    else :
        return(num * ft_factoriel_recursif(num -1))

print(ft_factoriel_recursif(5))
