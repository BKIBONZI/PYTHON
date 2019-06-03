
class Point :
    "Definition de la classe Point"

    def affiche_point(self, param):
        print("coord. horizontale =", param.x, "coord. verticale =", param.y)

if __name__ == '__main__':
    p9 = Point()
    print(type(p9))
    print (p9.__doc__)
    print (p9)
    p9.x = 3.0
    p9.y = 4.0
    print (p9.x)
    print (p9.y)
    print (p9.x**2 + p9.y**2)
    x = p9.x 
    print(x)
    p9.affiche_point(p9)


