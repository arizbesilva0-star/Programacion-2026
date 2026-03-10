"""
Created on Febrero, 2019
@author: arizbesilva0-star
"""

from Inversion import *
from Menu import *

menu = Menu("Bienvenido al Sistema de Inversiones")

inversion1 = Inversion(1000, 0.05, 12, "Inversion Banco BBVA")

menu.bienvenida()

while True:

    opcion = menu.opciones()

    if opcion == "1":
        cantidad = float(input("Cantidad a aumentar: "))
        inversion1.aumentar(cantidad)
        print("Capital actualizado:", inversion1.capital)

    elif opcion == "2":
        cantidad = float(input("Cantidad a disminuir: "))
        inversion1.disminuir(cantidad)
        print("Capital actualizado:", inversion1.capital)

    elif opcion == "3":
        resultado = inversion1.calcular()
        print("Monto final de la inversion:", resultado)

    elif opcion == "4":
        inversion1.mostrar()

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion no valida")