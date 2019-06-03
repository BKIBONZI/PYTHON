# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    constructor_destructor.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/04 22:10:18 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/04 22:31:42 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Warrior :
    def __init__(self, name='bob'):
        self.name = name
        print("A warrior appeared ! His name is %s." % name)

    def __del__(self):
        print("%s just died." % self.name)

if __name__ == '__main__':
    bob = Warrior()
    tom = Warrior("Tom")
    del tom

