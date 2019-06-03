# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    typeDict_devpointcom.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bkibonzi <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/02/20 10:43:45 by bkibonzi          #+#    #+#              #
#    Updated: 2019/02/20 10:58:06 by bkibonzi         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

d = {"server":"mpilgrim", "database":"master"}

print(d)
print(d["server"])
print(d["database"])


# modification d'un dictionnaire

d["database"] = "pubs"

print(d)

# ajouter une paire cle/valeur 

d["uid"] = "sa"

print(d)

