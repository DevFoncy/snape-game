def printMessage():
	print( "Hola Mundo" )

def functionWithReturn( lado) :
	area = lado*lado
	return area  
	# print("Area",area)

def functionWithoutReturn( a,b,c) : 
	discriminante =   pow(b,2) - 4*a*c 
	print("La discriminante es ", discriminante)


functionWithoutReturn(2,2,1)

# print("el resultado es :",resultado)