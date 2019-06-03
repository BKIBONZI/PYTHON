# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    textTypes.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/17 10:46:31 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/17 22:23:45 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

s = 'Camel'

print('The ' + s + ' ran away !')

print('Size of %s => %d' %(s, len(s)))

for ch in s :
    print(ch)

if s.startswith('C'):
    print(s.upper())

print(3*s)

print('Now is %02d:%02d.' % (16,30))

print('Percent: %.1f%%, Exponencial:%.2e' % (5.333, 0.00314))

print('Decimal : %d, Octal : %o, Hexadecimal : %x' % (10,10,10))
