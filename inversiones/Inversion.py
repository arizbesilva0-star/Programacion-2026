"""
Created on Febrero, 2026
@author: arizbesilva0-star
"""

class Inversion:

    # Constructor
    # Inicializa los atributos de la inversión
    def __init__(self, capital, interes, tiempo, nombre):
        self.capital = capital
        self.interes = interes
        self.tiempo = tiempo
        self.nombre = nombre

    # Aumentar capital
    def aumentar(self, cantidad):
        self.capital = self.capital + cantidad

    # Disminuir capital
    def disminuir(self, cantidad):
        self.capital = self.capital - cantidad

    # Calcular monto final con interés simple
    def calcular(self):
        monto = self.capital * (1 + self.interes * self.tiempo)
        return monto

    # Mostrar datos
    def mostrar(self):
        print("Nombre de inversion:", self.nombre)
        print("Capital actual:", self.capital)
        print("Interes:", self.interes)
        print("Tiempo:", self.tiempo, "meses")