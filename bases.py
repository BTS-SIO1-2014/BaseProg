#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Un programme s'éxécute de façon séquentiel en effectuant les instructions
#Dans l'ordre du programme de haut en bas:

#L'opération d'affectation d'une valeur à une variable s'écrit en pseudo-code
# variable <- valeur (on lit : la variable est affecté de la valeur)
# Dans de nombreux langages on utilise = au lieu de <-

variable = 1
variable = 2
print variable

#Affiche 2 uniquement (print est la procédure d'affichage)

#Une procédure est un ensemble d'instructions
#La différence entre une procédure et une fonction vient du fait qu'une procédure ne renvoie pas de valeurs au contraire d'une fonction.

#En pseudo-code on définie le début et la fin de la procédure et on la nomme!

# DébutProcédure MA_PROCEDURE
# | Bloc d'instructions
# FinProcédure MA_PROCEDURE

# En python

def ma_procedure():
    pass

# En java
# function ma_procedure(){
#    // rien
# }

#Les conditions / tests

#Les conditions sont des fonctions ou une suite d'opérations renvoyant un type booléen True ou False

var1 = True;
var2 = False;

var1 or var2 #Ceci est une condition

def condition():
    return False #Cette fonction est une fonction condition car son type de retour est un booléen

#Les branches / choix / Séquences conditionnelles:

#Une branche permet de selectionner un bloc d'instruction en fonction d'une condition:

#En pseudo-Code la branche s'écrit:
# Si Condition, Alors
# | Bloc d'instructions
# Sinon
# | Bloc d'instructions autre
# FinSi

#En python

if (condition()): 
   pass 
else:
   pass # Dans notre cas la fonction condition renvoie False, donc on passe dans 
        # le bloc else


#En java, C#
# if (condition){
#    //rien
# }else{
#    //rien
# }


#Les Boucles

#Dans un programme il est courrant de vouloir effectuer plusieurs fois les
#mêmes instructions.
#Dans ce cas on utilise une structure de flux d'instructions nommée boucle

#Il existe trois grand type de boucle:
# - Les boucles POUR
# - Les boucles POURCHAQUE
# - Les boucles TANTQUE
# - Il existe une boucle FAIRE - TANTQUE (do-while) mais son usage est déprécié regarder cette page pour comprendre pourquoi cette boucle n'as pas été implémenté en python: http://www.python.org/dev/peps/pep-0315/

#Une boucle à un début et une fin:
#En peusdo code on doit donc préciser
# - POUR
#   |
#   | Bloc d'instruction
#   | 
#   FinPOUR

#Les boucles doivent avoir une condition de sortie
#Cette condition est un fonction qui doit retourner un type boolein.

# La boucle POUR:
# Une boucle POUR comporte :
#  - une variable 'i' qui est un compteur (ou plus élégamment une variable d'itération, on utilise i comme index ou indice)
#  - une condition de sortie
#  - une fonction incrémentale (qui va modifier à chaque tour de la boucle la variable compteur), également nommé 'Pas', par défaut le 'Pas' est de 1 (i est incrémenté de 1)

# En peusdo code on peut écrire
# - POUR compteur allant de 0 à 10 (par pas de 1)
# cela se traduit:
# En python for i in range(0,11) (le pas de 1 est implicite par contre la condition de sortie par défaut est  i < deuxième_paramètre de la fonction range (ici 11))
# En java,C#   for (int i=0;i<=10;i=i+1) (ou plus classiquement i=i+1 == i++)

# La boucle TANTQUE

# On écrit en pseudo-code:
# TANTQUE condition
# | Bloc d'instructions
# FinTANTQUE

# En python:
while(condition()):
    pass #Ici on ne passera JAMAIS dans le bloc d'instruction car la condition() est fausse

# La boucle POURCHAQUE

# En pseudo-code
# POURCHAQUE élément DANS collection
# | Bloc d'instructions
# FinPOURCHAQUE

# L'éléments est un objet de la collection (liste,dictionnaires,map,set...)
# En python pour et pourchaque sont similaire:

for i in {0,1,2}:
    print i # affiche 0
            #         1
            #         2

# En java
# for (Integer i : liste){
#     // rien
# }

# En C#
#foreach (int i in tableau)
#{
#        //rien
#}


# Exercices:


#Définition Procédure "Triangle"
#   Paramètres:
#       nombre_de_lignes : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       chaine : type chaine de caractères
#
#   DébutProcédure
#       Pour i allant de 1 à nombre_de_lignes
#       |   chaine <- chaine vide
#       |   Pour j allant de 1 à i
#       |   |   chaine <- chaine + "+"
#       |   FinPour
#       |   afficher chaine
#       FinPour
#   FinProcédure
#Fin Définition Procédure "Triangle"

def triangle(nombre_de_lignes):
    for i in range (1, nombre_de_lignes + 1):
        chaine = ""
        for j in range(1,i+1):
            chaine = chaine + "+"
        print chaine


# Avoir définie une procédure ne l'appel pas! 
# En python (et dans les autres languages) on appel une procédure en utilisant son nom et en lui passant des paramètres!

print "Triangle"
triangle(10) # Ici j'appel la procédure triangle définie plus haut avec le paramètre 10

#Attention pour pouvoir appeler une fonction il faut d'abbord la définir. Cela est du à la lecture séquentiel du code.


#Définition Procédure "Rectangle Plein"
#   Paramètres:
#       largeur : type entier
#       hauteur : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       chaine : type chaine de caractères
#
#   DébutProcédure
#       Pour i allant de 1 à hauteur
#       |   chaine <- chaine vide
#       |   Pour j allant de 1 à largeur
#       |   |   chaine <- chaine + "+"
#       |   FinPour
#       |   afficher chaine
#       FinPour
#   FinProcédure
#
#FinDéfinition Procédure "Rectangle Plein"
def rectangle_plein(largeur,hauteur):
    for i in range (1, hauteur + 1):
        chaine = ""
        for j in range(1, largeur +1):
            chaine = chaine + "+"
        print chaine

print "Rectangle plein"
rectangle_plein(4,2)


#Définition Procédure "Rectangle Creux"
#   Paramètres:
#       largeur : type entier
#       hauteur : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       k : type entier
#       chaine : type chaine de caractères
#
#   DébutProcédure:
#       Si hauteur ou largeur est inférieur à 3
#       |   Lancer une exception "Paramètre invalide"
#       FinSi
#       chaine <- chaine vide
#       Pour k allant de 1 à largeur
#       |    chaine <- chaine + "+"
#       FinPour
#       afficher chaine
#       Pour i allant de 2 à hauteur -1
#       |   chaine <- "+"
#       |   Pour j allant de 1 à largeur-2
#       |   |   chaine <- chaine + " "
#       |   FinPour
#       |   chaine <- chaine + "+"
#       |   afficher chaine
#       FinPour
#       chaine <- chaine vide
#       Pour k allant de 1 à largeur:
#       |    chaine <- chaine + "+"
#       FinPour
#       afficher chaine
#   FinProcédure
#FinDéfinition Procédure "Rectangle Creux"
def rectangle_creux(largeur,hauteur):
    if hauteur <3 or largeur < 3:
        raise Exception("Paramètre non valide")
    chaine = ""
    for k in range (1,largeur+1):
        chaine = chaine + "+"
    print chaine
    for i in range (2, hauteur):
        chaine = "+"
        for j in range (1,largeur-1):
            chaine = chaine + " "
        chaine = chaine + "+"
        print chaine
    chaine = ""
    for k in range (1,largeur+1):
        chaine = chaine + "+"
    print chaine

print "Rectangle creux 1"
rectangle_creux(3,3)
rectangle_creux(4,3)
rectangle_creux(5,5)


#Définition Procédure "Afficher Ligne"
#   Paramètres:
#       largeur : type entier
#   Variables:
#       k : type entier
#       chaine : type chaine de caractères
#
#   DébutProcédure
#       chaine <- chaine vide
#       Pour k allant de 1 à largeur
#       |    chaine <- chaine + "+"
#       FinPour
#       afficher chaine
#   FinProcédure
#
#FinDéfinition Procédure "Afficher Ligne"
def afficher_ligne(largeur):
    chaine = ""
    for k in range (1,largeur+1):
        chaine = chaine + "+"
    print chaine



#Procédure "Rectangle Creux 2"
#   Paramètres:
#       largeur : type entier
#       hauteur : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       chaine : type chaine de caractères
#   Utilise:
#       AFFICHER_LIGNE : type Procedure "Afficher Ligne"
#
#   DébutProcédure:
#       Si hauteur ou largeur est inférieur à 3
#           Lancer une Exception "Paramètre invalide"
#       FinSi
#       AFFICHER_LIGNE
#       Pour i allant de 2 à hauteur -1
#       |   chaine <- "+"
#       |   Pour j allant de 1 à largeur-2
#       |   |   chaine <- chaine + " "
#       |   FinPour
#       |   chaine <- chaine + "+"
#       |   afficher chaine
#       FinPour
#       AFFICHER_LIGNE
#   FinProcédure
#FinDéfinition Procédure "Rectangle Creux 2"
def rectangle_creux2(largeur,hauteur):
    if hauteur <3 or largeur < 3:
        raise Exception("Paramètre non valide")
    afficher_ligne(largeur)
    for i in range (2, hauteur):
        chaine = "+"
        for j in range (1,largeur-1):
            chaine = chaine + " "
        chaine = chaine + "+"
        print chaine
    afficher_ligne(largeur)

print "Rectangle Creux 2"
rectangle_creux2(6,3)


#Définition Procédure "Carrer Plein"
#   Paramètres:
#       cote : type entier
#   Utilise:
#       RECTANGLE : type Procedure "Rectangle Plein"
#
#   DébutProcédure
#       RECTANGLE(cote,cote)
#   FinProcédure
#
#FinDéfinition Procédure "Carrer Plein"
def carre_plein(cote):
    rectangle_plein(cote,cote)

print "Carré plein"
carre_plein(4)
    
#Définition Procédure "Carrer Creux"
#   Paramètres:
#       cote : type entier
#   Utilise:
#       RECTANGLE : type Procedure "Rectangle Creux2"
#
#   DébutProcédure
#       RECTANGLE(cote,cote)
#   FinProcédure
#
#FinDéfinition Procédure "Carrer Plein"
def carre_creux(cote): # minimum cote 3
    rectangle_creux2(cote,cote)

print "Carré Creux"
carre_creux(4)

#Définition Procédure "Triangle Inverse"
#   Paramètres:
#       nombre_de_lignes : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       chaine : type chaine de caractères
#
#   DébutProcédure
#       Pour i allant de 1 à nombre_de_lignes
#       |   chaine <- chaine vide
#       |   Pour j allant de nombre_de_lignes - i  à 1 par pas de -1
#       |   |   chaine <- chaine + "+"
#       |   FinPour11
#       |   afficher chaine
#       FinPour
#   FinProcédure
#Fin Définition Procédure "Triangle"
def triangle_inverse(nombre_de_lignes):
    for i in range (1, nombre_de_lignes + 1):
        chaine = ""
        for j in range(nombre_de_lignes+1-i,0,-1):
            chaine = chaine + "+"
        print chaine

print "Triangle Inverse"
triangle_inverse(4)
# ++++
# +++
# ++
# +

#Définition Procédure "Triangle Mirroir"
#   Paramètres:
#       nombre_de_lignes : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       chaine : type chaine de caractères
#
#   DébutProcédure
#       Pour i allant de 1 à nombre_de_lignes
#       |   chaine <- chaine vide
#       |   Pour j allant de 1 à nombre_de_lignes - i
#       |   |   chaine <- chaine + " "
#       |   FinPour
#       |   Pour k allant de 1 à i
#       |   |   chaine <- chaine + "+"
#       |   FinPour
#       |   afficher chaine
#       FinPour
#   FinProcédure
#Fin Définition Procédure "Triangle Mirroir"
def triangle_mirroir(nombre_de_lignes):
     for i in range (1, nombre_de_lignes + 1):
        chaine = ""
        for j in range(1,nombre_de_lignes+1-i):
            chaine = chaine + " "
        for k in range(1,i+1):
            chaine = chaine + "+"
        print chaine

print "Triangle Mirroir"
triangle_mirroir(4)
#    +
#   ++
#  +++
# ++++


#Définition Procédure "Triangle Mirroir Inverse"
#   Paramètres:
#       nombre_de_lignes : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       chaine : type chaine de caractères
#
#   DébutProcédure
#       Pour i allant de 0 à nombre_de_lignes
#       |   chaine <- chaine vide
#       |   Pour j allant de 0 à i
#       |   |   chaine <- chaine + " "
#       |   FinPour
#       |   Pour k allant de 0 à nombre_de_lignes - i
#       |   |   chaine <- chaine + "+"
#       |   FinPour
#       |   afficher chaine
#       FinPour
#   FinProcédure
#Fin Définition Procédure "Triangle Mirroir Inverse"
def triangle_mirroir_inverse(nombre_de_lignes):
    for i in range (0, nombre_de_lignes):
        chaine = ""
        for j in range(0,i):
            chaine = chaine + " "
        for k in range(0,nombre_de_lignes-i):
            chaine = chaine + "+"
        print chaine

print "Triangle Mirroir Inverse"
triangle_mirroir_inverse(4)
# ++++
#  +++
#   ++
#    +


#Définition Procédure "Triangle Iso"
#   Paramètres:
#       nombre_de_lignes : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       chaine : type chaine de caractères
#
#   DébutProcédure
#       Pour i allant de 0 à nombre_de_lignes
#       |   chaine <- chaine vide
#       |   Pour j allant de nombre_de_lignes - i -1 à 0 par pas de -1
#       |   |   chaine <- chaine + " "
#       |   FinPour
#       |   Pour k allant de 0 à i*2 + 1
#       |   |   chaine <- chaine + "+"
#       |   FinPour
#       |   afficher chaine
#       FinPour
#   FinProcédure
#Fin Définition Procédure "Triangle Iso"
def triangle_iso(nombre_de_lignes):
     for i in range (0, nombre_de_lignes):
        chaine = ""
        for j in range(nombre_de_lignes-i-1,0,-1):
            chaine = chaine + " "
        for k in range(0,i*2 + 1):
            chaine = chaine + "+"
        print chaine

#   +
#  +++
# +++++
print "Triangle ISO" 
triangle_iso(3)

#Définition Procédure "Triangle Iso Inverse"
#   Paramètres:
#       nombre_de_lignes : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       chaine : type chaine de caractères
#
#   DébutProcédure
#       Pour i allant de 0 à nombre_de_lignes
#       |   chaine <- chaine vide
#       |   Pour j allant de 0 à i
#       |   |   chaine <- chaine + " "
#       |   FinPour
#       |   Pour k allant de 0 à (nombre_de_lignes -i)*2 -1
#       |   |   chaine <- chaine + "+"
#       |   FinPour
#       |   afficher chaine
#       FinPour
#   FinProcédure
#Fin Définition Procédure "Triangle Iso Inverse"
def triangle_iso_inverse(nombre_de_lignes):
      for i in range (0, nombre_de_lignes):
        chaine = ""
        for j in range(0,i):
            chaine = chaine + " "
        for k in range((nombre_de_lignes -i)*2 - 1):
            chaine = chaine + "+"
        print chaine

# +++++
#  +++
#   +
print "Triangle ISO Inverse"
triangle_iso_inverse(3)

#Définition Procédure "Losange"
#   Paramètres:
#       cote : type entier
#   Variables:
#       i : type entier
#       j : type entier
#       chaine : type chaine de caractères
#   Utilise:
#       TRIANGLE_ISO : type Procedure "Triangle Iso"
#
#   DébutProcédure
#       TRIANGLE_ISO
#       Pour i allant de 1 à cote
#       |   chaine <- chaine vide
#       |   Pour j allant de 0 à i
#       |   |   chaine <- chaine + " "
#       |   FinPour
#       |   Pour k allant de 0 à (cote -i)*2 -1
#       |   |   chaine <- chaine + "+"
#       |   FinPour
#       |   afficher chaine
#       FinPour
#   FinProcédure
#Fin Définition Procédure "Losange"
def losange(cote):
    triangle_iso(cote)
    for i in range (1, cote):
        chaine = ""
        for j in range(0,i):
            chaine = chaine + " "
        for k in range((cote -i)*2 - 1):
            chaine = chaine + "+"
        print chaine

print "Losange"
losange(3)
#   +
#  +++
# +++++
#  +++
#   +
losange(6)


#Définition Procédure "Tables de multiplications"
#   Paramètres:
#       entier : type entier
#   Variables:
#       tables : type entier
#       multiplicateur : type entier
#       resultat : type string
#
#   DébutProcédure:
#       POURCHAQUE tables compris entre  O et entier
#       |   POURCHAQUE multiplicateur compris entre 0 et entier
#       |   |   résultat <- tables * multiplicateur
#       |   |   afficher tables * multiplicateur = résultat
#       |   FinPOURCHAQUE
#       FinPOURCHAQUE
#   FinProcédure
#Fin Définition Procédure "Tables de Multiplications"
def tables_multiplications(entier):
    for tables in range(0,entier+1):
        for multiplicateur in range(0,entier+1):
            resultat= tables * multiplicateur
            print str(tables)+"*"+str(multiplicateur) +"=" + str(resultat)

print "Tables de multiplications"
tables_multiplications(10)


#Début Définition Procédure "Fizz Buzz"
#   Paramètres:
#       nombre : type entier
#   
#   DébutProcédure
#   |   SI nombre divisible par 3 et nombre disivible par 5
#   |   |   afficher "FizzBuzz"
#   |   |   retour
#   |   FinSI
#   |   SI nombre divisible par 5
#   |   |   afficher "Buzz"
#   |   |   retour
#   |   FinSI
#   |   SI nombre divisible par 3
#   |   |   afficher "Fizz"
#   |   |   retour
#   |   FinSI
#   FinProcédure
#Fin Définition Procédure "Fizz Buzz"
def fizz_buzz(nombre):
    if nombre % 3 == 0 and nombre % 5 == 0:
        print "FizzBuzz"
        return
    if nombre % 5 == 0:
        print "Buzz"
        return
    if nombre % 3 == 0:
        print "Fizz"
        return

fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)

#Définition Procédure "Code de caesar"
#   Paramètres:
#       mot : type chaine de charactère
#       char : type charactère
#   Variables:
#       retour : type chaine de charactère
#       c : type charactère
#       cprime : type entier
#   Fonctions:
#       Ordinal : renvoie un entier correspondant au charactère paramètre
#       Character : Convertie un entier paramètre en charactère
#
#   DébutProcédure
#   |   retour <- chaine vide
#   |   POURCHAQUE c dans mot
#   |   |   cprime <- (Ordinal(c) - Ordinal(char)) % 26 + Ordinal(char)
#   |   |   retour <- retour + Character(cprime)
#   |   FinPOURCHAQUE
#   |   afficher retour
#   FinProcédure
#Fin Définition Procédure "Code de Caésar"
def code_de_caesar(mot,char):
    retour = ""
    for c in mot:
        cprime = (ord(c)- ord(char)) % 26 + ord('a')
        retour += chr(cprime)
    print retour

code_de_caesar("caesar",'c')
