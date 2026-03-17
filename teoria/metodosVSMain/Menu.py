"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

from Cuenta import *

class Menu:

    def __init__(self, mensaje):
        self.mensaje = mensaje

    def bienvenida(self):
        print(self.mensaje)

    def opciones(self):
        print("\n1. Depositar")
        print("2. Retirar")
        print("3. Mostrar cuenta")
        print("4. Salir")
        return input("Opcion: ")
