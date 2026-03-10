'''
Created on Feb, 2019
@author: arizbesilva0-star

'''
class Cuenta :
  #este es el metodo constructor, que
  #inicializa a los atributos de una clase
  # La clase ya tiene más de un atributo.
	# En este caso, cambia la cantidad de argumentos que el
	# constructor recibe
  def __init__(self, valor1, valor2, valor3) :
    self.saldo=valor1
    self.tipo=valor2
    self.fechaCreacion=valor3
  def depositar(self, cantidad) :
    self.saldo=self.saldo+cantidad
  def retirar(self, cantidad2) :
    self.saldo=self.saldo-cantidad2
  def informacion(self):
    print("saldo::",self.saldo)
    print("tipo::",self.tipo)
    print("fechaCreacion::",self.fechaCreacion)
