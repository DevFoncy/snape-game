import turtle
import time
#Para crear numeros random para posicionar la comida en otro lado/
import random

posponer = 0.1 


# Instanciamos un objeto de tipo Screen y ejecutamos el metodo Screen para generar una ventana en blanco
wn = turtle.Screen()

# Accedemos a sus metodos y le pasamos parametros
wn.title("Juego")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)  #Redimensionar la pantalla
wn.tracer(0)  #Mejores efectos de animaciones


#Cabeza serpiente 
cabeza = turtle.Turtle()
cabeza.speed(0) #Iniciar pantalla el dibujo este ahi
cabeza.shape("square") #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
cabeza.penup() #Ppara cuando el snape se mueva no deje rastro
cabeza.color("white") #Por default viene en negro
cabeza.goto(0,0)
# cabeza.direction = "stop"  #el programa espere a que yo introduzce alguna direccion 
cabeza.direction = "stop"  #Setemoas en up


#Cabeza

#Cabeza serpiente 
comida = turtle.Turtle()
comida.speed(0) #Iniciar pantalla el dibujo este ahi
comida.shape("square") #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
comida.penup() #Ppara cuando el snape se mueva no deje rastro
comida.color("red") #Por default viene en negro
comida.goto(0,100)


# Funciones 
# los nombres arriba, abajo, izquierda, derecha puede variar son string de comparacion
def arriba():
	cabeza.direction = "arriba"
def abajo():
	cabeza.direction = "abajo"
def izquierda():
	cabeza.direction = "izquierda"
def derecha():
	cabeza.direction = "derecha"

# Esta funcion va validar cuando se llega al extremo de la pantalla , eje X y eje Y
def validarLimites():
	# Validamos cuando el eje X llega al extremo derecho , en mi caso seria 300px 
		if cabeza.xcor() == 300:
								y = cabeza.ycor()
								cabeza.goto(-280, y)

	# Validamos cuando el eje X llega al extremo izquierda , en mi caso seria -300px 
		if cabeza.xcor() == -300:
								y = cabeza.ycor()
								cabeza.goto(280, y)

	# Validamos cuando el eje Y llega al extremo inferior , en mi caso seria -300px
		if cabeza.ycor() == -300:
								x = cabeza.xcor()
								cabeza.goto(x,280)
														
 # Validamos cuando el eje Y llega al extremo superior , en mi caso seria 300px
		if cabeza.ycor() == 300:
								x = cabeza.xcor()
								cabeza.goto(x,-280)

		

# los nombres arriba, abajo, izquierda, derecha puede variar son string de comparacion
def mov():
	if cabeza.direction == 'arriba' :
		y= cabeza.ycor() #Obtener coordenadas de la coordenada y
		cabeza.sety( y + 20) #Aumentmaos 20px en el eje Y

	if cabeza.direction == 'abajo' :
		y= cabeza.ycor() #Obtener coordenadas de la coordenada y
		cabeza.sety( y - 20) #Reducimos 20px en el eje Y

	if cabeza.direction == 'izquierda' :
		x= cabeza.xcor() #Obtener coordenadas de la coordenada X
		cabeza.setx( x - 20) #Aumentamos 20px en el eje X 

	if cabeza.direction == 'derecha' :
		x= cabeza.xcor() #Obtener coordenadas de la coordenada X
		cabeza.setx( x + 20) #Reducimos 20px en el eje X 




# Teclado
#Recordar que Up , Down , Left , Right son palabras reservadas de los eventos leidos por el teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")


# Estructura de los juegos corriendo en un bucle infinito
while True:
			wn.update()

				# Esto es el efecto de comer la comida cuando haya una distancia de 20 y posicionar en un lugar aleatorio en el mapa
			if cabeza.distance(comida) < 20:
				x=random.randint(-280,280)
				y=random.randint(-280,280)
				comida.goto(x,y)

			mov()
			validarLimites()
			time.sleep(posponer)


