import sys

try : 
    if len(sys.argv) > 2 :
        raise ValueError("bad number of arguments")

    if len(sys.argv) == 2 :
    
        nombre = int(sys.argv[1])

        if int(sys.argv[1]) == 0 :
            print("I'm Zero.")
        elif int(sys.argv[1]) % 2 == 0 :
            print("I'm Even.")
        else :
            print("I'm Odd.")

except ValueError :
    print("ERROR")
