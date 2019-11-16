class Alumno: 
  def __init__(object, name, age):
  	object.name = name
  	object.age = age

  def printName(abc):
  	print("Hola mi nombre es" + abc.name)
  	print("Mi edad es ", abc.age)

p1 = Alumno("John", 36)
p1.name = "Tito"
p1.age = 12
p1.printName()
