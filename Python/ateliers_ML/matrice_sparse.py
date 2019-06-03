# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrice_sparse.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/18 18:58:57 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/18 20:17:51 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

matrix = '''0 0 0 0 0 0 0 0 0 0 0 0
9 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 4 0 0
0 0 0 0 0 0 0 3 0 0 0 0
0 0 0 0 0 0 5 0 0 0 0 0
0 0 0 0 6 0 0 0 0 0 0 0'''

mat = {}

for row, line in enumerate(matrix.splitlines()):

    for col, column in enumerate(line.split()):

        column = int(column)

        if column:
            mat[row, col] = column
print(mat) 

print('Complete matrix size:', (row + 1) * (col +1))
print('Sparse matrix size :', len(mat))
