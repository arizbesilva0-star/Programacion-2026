"""
Created on Febrero, 2019
@author: arizbesilva0-star
"""

from Cuenta import *
from Menu import *

class Main:
    pass


menu = Menu("Bienvenidos al Banco Pato")

menu.darBienvenida()
opcion = menu.despliegaMenu()


cuenta1 = Cuenta(300, "debito", "12/02/2019")

print("\nDatos de la cuenta:")
cuenta1.imprimirDetalles()


if opcion == "1":
    cuenta1.depositar(800)
    print("\nDepósito realizado")
    cuenta1.imprimirDetalles()

elif opcion == "2":
    cuenta1.retirar(100)
    print("\nRetiro realizado")
    cuenta1.imprimirDetalles()