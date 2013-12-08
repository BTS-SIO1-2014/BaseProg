def drapeau(n):
    for i in range(0,n):
        print i*'*'

def drapeauInverse(n):
    for i in range(n,0,-1):
        print i*'*'


drapeau(10)
drapeauInverse(10)

def astTri(i,n):
    ast=''
    for j in range(0,n+4-(i*2)):
        ast+=" "
    for k in range(0,i*2+1):
        ast+="* "
    return ast

def drapeauIso(n):
    for i in range (0,n):
        print astTri(i,n)

drapeauIso(5)


def fizzBuzz():
    for i in range(0,100):
        if (i%3 == 0 and i%5 == 0):
            print "FizzBuzz"
        elif (i%5 == 0):
            print "Buzz"
        elif (i%3 ==0):
            print "Fizz"
        else:
            print i

fizzBuzz()


def afficherMatrice(matrice):
    print "|"+str(matrice[0][0]) +" "+str(matrice[0][1])+"|"
    print "|"+str(matrice[1][0]) +" "+str(matrice[1][1])+"|"

MATRICE = [[4,5],[6,7]]
afficherMatrice(MATRICE)

def is_premier(n):
    diviseur = 2
    while (n % diviseur !=0):
        diviseur +=1

    if diviseur == n:
        return True
    else:
        return False

n = input ("Premier?")
print is_premier(n)
