"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Menu:

    def __init__(self, mensaje):
        self.mensaje = mensaje

    def bienvenida(self):
        print(self.mensaje)

    def opciones(self):
        print("\nOpciones del sistema:")
        print("1. Aumentar inversion")
        print("2. Disminuir inversion")
        print("3. Calcular monto final")
        print("4. Mostrar datos")
        print("5. Salir")

        opcion = input("Selecciona una opcion: ")
        return opcion
