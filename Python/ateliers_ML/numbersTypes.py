# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    numbersTypes.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/16 09:53:40 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/16 10:15:07 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print('int(3.14) =', int(3.14))
print('float(5) =', float(5))
print('5.0 / 2 +  3 =', 5.0 / 2 + 3) 
print("int('20',8) =", int('20',8))
print("int('20',16) =", int('20', 16))

c = 3 + 4j
print('c='), c
print('Real Part:', c.real)
print('Imaginary Part:', c.imag)
print('Conjugate:', c.conjugate())

