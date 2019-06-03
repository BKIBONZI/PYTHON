# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fibonacci_non_recursif.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/19 08:53:03 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/20 01:04:51 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def fib(n) :
    """Fibonacci :
    fib(n) = fib(n-1) + fib(n-2) se n > 1
    fib(n) = 1 se n <= 1
    """

    l = [1,1]

    for i in range(2, n + 1):
        l.append(l[i -1] + l[i -2])
    
    return l[n]

#Show Fibonacci from 1 to 5
for i in [1,2,3,4,5]:
    print(i, '=>', fib(i))


