# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    attributes_methods.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/03 22:19:52 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/04 15:21:37 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/local/bin/python3

class Car:
    def drive(self):
        print("Vroom !")

    def paint(self, color):
        self.color = color
        print("%s is now the new color" % str(color))

    def get_color(self):
        return self.color

if __name__ == '__main__':
    x = Car()
    print("Drive method called:")
    x.drive()

    print("\nChanging attribute value with a setter :")
    x.paint("red")
    print("\nPrint getter return :")
    print(x.get_color())

    print("\n Direct access to attribute :")
    x.color = "blue"
    print(x.color)

