# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fcnFormat.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/17 23:31:08 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/18 00:23:59 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

musicians = [('Page', 'guitarist','Led Zeppelin'),
('fripp','guitarist','king Crimson')]

msg = '{0} is {1} of {2}'

for name, function, band in musicians:
    print(msg.format(name, function, band))


msg = '{greeting}, it is {hour:02d}:{minute:02d}'
print(msg.format(greeting='Good morning', hour=7, minute=30))

print('Pi =', format(3.14159, '.3e'))

