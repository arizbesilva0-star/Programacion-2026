"""
Created on Febrero, 2019
@author: arizbesilva0-star
"""

from Cuenta import *

class Main:
    pass


print("*** 1. Imprimimos atributos desde el archivo principal ***")

# Creamos un objeto de la clase Cuenta
cuenta1 = Cuenta(300, "debito", "12/02/2019")

# Imprimimos atributos directamente
print(cuenta1.saldo)
print(cuenta1.tipo)
print(cuenta1.fechaCreacion)


print("\n*** 2. Imprimimos atributos con el método ***")

# Usamos el método de la clase
cuenta1.imprimirDetalles()


print("\n*** 3. Probamos operaciones ***")

cuenta1.depositar(200)
cuenta1.retirar(100)

cuenta1.imprimirDetalles()