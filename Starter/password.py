"""
Purpose
    Crear un script que permita generar una contraseña aleatoria con datos 
    ingresados por el usuario.

Running the code
    py password.py

Additional information
    Python 3.9.7

"""
import string
import random

def generate_password():
    """Funcion que permite generar un password aleatorio
    :param length: Longitud asignada de la contraseña
    :param alphabets_length: Numero de letras insertadas en la contraseña
    :param digits_length: Numero de digitos insertados en la contraseña
    :param pecial_characters_length: Numero de caracteres insertados en la 
                                        contraseña
    :param count: suma de las letras, digito y caracteres especiales que
                    seran insertados en la contraseña
    """
    print("===============================================================")
    print("                     PASSWORD GENERATOR                        ")
    print("===============================================================")
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list("!@#$%^&*()")
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    #Logintud de los datos para generar la contraseña
    length = int(input("Enter your password length ~>"))
    alphabets_length = int(input("Enter alphabets count in password ~>"))
    digits_length = int(input("Enter digits count in password ~>"))
    special_characters_length = int(input("Enter special characters in \
                                            password~> "))
    count = alphabets_length + digits_length + special_characters_length
    
    #Validacion de longitud suma de datos vs longitud de password
    if count > length:
        print("==============================================================")
        print("$ Character total count is {} and the password length is {}\
                try again ".format(count, length))
        return
    # Se inicializa la contraseña
    password = []
    #Seleccion aleratoria de letras
    for x in range(alphabets_length):
        password.append(random.choice(alphabets))
    #Seleccion aleatoria de numeros
    for x in range(digits_length):
        password.append(random.choice(digits))
    #Seleccion aleatoria de caracteres especiales
    for x in range(special_characters_length):
        password.append(random.choice(special_characters))
    # Si la suma de los datos es menos que la longitud agrega caracteres 
    # aleatorios igual a la longitud
    if count < length:
        random.shuffle(characters)
        for x in range(length - count):
            password.append(random.choice(characters))
    # convinando la contraseña resultante
    random.shuffle(password)
    print("===============================================================")
    print("$ You password is ~> "+"".join(password))

generate_password()
