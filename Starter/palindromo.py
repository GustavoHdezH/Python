"""
Purpose
    Demostrar si una palabra es un palindromo o no es lo es

Running the code
    py palindrome.py

Additional information
    Python 3.9.7

"""

print("===============================================================")
print("                     PALINDORME TESTING                        ")
print("===============================================================")

word= str(input("Enter your word ~> "))
word = word.replace("á","a").replace("é","e").replace("í", "i")\
    .replace("ó","o").replace("ú","u")

lower = word.casefold()
split = lower.split(' ')
join = ''.join(split)

reversion = join[::-1]

if (join == reversion):
    print("$ La palabra '{}', si es in palindromo".format(word))
else:
    print("$ La palabra '{}', no es un palindromo".format(word))

"""Se define los parametros
:param word: Palabra que ingresa el usuario
:param reversion:  Palabra que se voltea para comprobar
"""
