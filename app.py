import turtle
import time

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


# Funciones 
def arriba():
	cabeza.direction = "up"
def abajo():
	cabeza.direction = "down"
def izquierda():
	cabeza.direction = "left"
def derecha():
	cabeza.direction = "right"


def mov():
	if cabeza.direction == 'up' :
		y= cabeza.ycor() #Obtener coordenadas de la coordenada y
		cabeza.sety( y + 20) #Aumentmaos 20px en el eje Y

	if cabeza.direction == 'down' :
		y= cabeza.ycor() #Obtener coordenadas de la coordenada y
		cabeza.sety( y - 20) #Aumentmaos 20px en el eje Y

	if cabeza.direction == 'left' :
		x= cabeza.xcor() #Obtener coordenadas de la coordenada y
		cabeza.setx( x - 20) #Aumentmaos 20px en el eje Y	

	if cabeza.direction == 'right' :
		x= cabeza.xcor() #Obtener coordenadas de la coordenada y
		cabeza.setx( x + 20) #Aumentmaos 20px en el eje Y	

# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")



# Estructura de los juegos corriendo en un bucle infinito
while True:
	wn.update()

	mov()

	time.sleep(posponer)