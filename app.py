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

# Segmentos  / cuerpo serpiente
segmentos=[]

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

   	if cabeza.distance(comida) < 20:
   		x=random.randint(-280,280)
   		y=random.randint(-280,280)
   		comida.goto(x,y)

   		nuevo_segmento = turtle.Turtle()
   		nuevo_segmento.speed(0) #Iniciar pantalla el dibujo este ahi
   		nuevo_segmento.shape("square") #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
   		nuevo_segmento.penup() #Ppara cuando el snape se mueva no deje rastro
   		nuevo_segmento.color("gray") #Por default viene en negro
   		nuevo_segmento.goto(0,100)

   	mov()
   	time.sleep(posponer)


