"""
Created on March, 2026
@author: lunysska
"""

from Cuenta import *

class Menu:

    # Constructor
    # Inicializa el mensaje de bienvenida
    def __init__(self, valor):
        self.mensajeDeBienvenida = valor

    # Método que muestra el mensaje de bienvenida
    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    # Método que muestra las opciones del menú
    def despliegaMenu(self):
        print("\nLas opciones son:")
        print("1. Depositar")
        print("2. Retirar")

        opcion = input("Teclea la opcion: ")

        return opcion