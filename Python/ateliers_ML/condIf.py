# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    exemplesIf.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/16 02:30:13 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/16 02:38:19 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

temp = 23 

if temp < 0:
    print('Freezing ...')
elif 0 <= temp <= 20:
    print(Cold)
elif 21 <= temp <= 25:
    print('Normal')
elif 26 <= temp <= 35:
    print('Hot')
else :
    print('Very Hot')


