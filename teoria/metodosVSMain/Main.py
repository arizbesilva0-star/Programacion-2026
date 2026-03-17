"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

from Cuenta import *
from Cliente import *
from Menu import *

menu = Menu("Bienvenido al Banco")

cuenta1 = Cuenta(300, "debito", "12/02/2019")
cliente1 = Cliente("Arizbe", cuenta1)

menu.bienvenida()

while True:

    op = menu.opciones()

    if op == "1":
        cant = float(input("Cantidad: "))
        if cuenta1.depositar(cant):
            print("Deposito correcto")
        else:
            print("Error")

    elif op == "2":
        cant = float(input("Cantidad: "))
        if cuenta1.retirar(cant):
            print("Retiro correcto")
        else:
            print("No hay saldo")

    elif op == "3":
        print(cliente1)

    elif op == "4":
        break

    else:
        print("Opcion invalida")
