# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    fibonacci_recursif.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/19 08:40:53 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/19 08:46:36 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def fib(n) :
    """ Fibonacci :
    fib(n) = fib(n-1) +  (fib n-2) se n > 1
    fib(n) = 1 se n <= 1
    """
    if n > 1:
        return fib(n-1) + fib(n-2)
    else :
        return(1)
#show Fibonacci from 1 to 5
for i in [1,2,3,4,5]:
    print(i, '=>', fib(i))

