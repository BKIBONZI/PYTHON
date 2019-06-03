# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_iterateur+devpointcom.py                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/21 05:38:07 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/21 06:12:27 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class MonIterateur(object):
    def __init__(self, obj):
        self.obj = obj
        self.length = len(obj)
        self.count = 0

    def __iter__(self) :
        return self

    def next(self) :
        if self.count > self.length:
            raise StopIteration 

        else:
            result = self.obj[self.count]

        self.count += 2
        return result

if __name__ == "__main__":
    chaine = "hello_world"
    ma_classe_iterateur = MonIterateur(chaine)
    try:
        for lettre in ma_classe_iterateur :
            print(lettre)
    except  StopIteration:
        print("fin d'iteration")
