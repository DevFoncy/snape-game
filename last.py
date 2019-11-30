import turtle
import time
#Para crear numeros random para posicionar la comida en otro lado/
import random

posponer = 0.1 

# marcador 
score = 0
hight_score = 0



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


#Comida serpiente 
comida = turtle.Turtle()
comida.speed(0) #Iniciar pantalla el dibujo este ahi
comida.shape("circle") #“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.
comida.penup() #Ppara cuando el snape se mueva no deje rastro
comida.color("red") #Por default viene en negro
comida.goto(0,100) 

# Cuerpo serpiente 
segmentos = [] #lista vacia

texto = turtle.Turtle()
texto.speed(0)
texto.color('white')
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write('Score: 0 		Hight Score: 0', align= 'center', font= ('Courier', 24, 'normal'))



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

# Validar colisiones cuando se toca los extremos
def colisiones():
	if cabeza.xcor() > 290  or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290 :
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = 'stop'
		limpiarSegmentos()	
		
def limpiarSegmentos():
	for segmento in segmentos:
		segmento.hideturtle()

	segmentos.clear()	

	# Resetear marcador
	score = 0
	texto.clear()
	texto.write('Score: {} 		Hight Score: {}'.format(score, hight_score),
							 align= 'center', font= ('Courier', 24, 'normal'))
	


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
				nuevo_segmento = turtle.Turtle()
				nuevo_segmento.speed(0)
				nuevo_segmento.shape("square") 
				nuevo_segmento.penup()
				nuevo_segmento.color("grey")
				segmentos.append(nuevo_segmento)

				# Aumentar Score
				score = score + 10

				if score > hight_score:
					hight_score = score

				texto.clear()	
				texto.write('Score: {} 		Hight Score: {}'.format(score, hight_score),
							 align= 'center', font= ('Courier', 24, 'normal'))
	

					

			# mover el cuerpo de la serpiente	
			totalSeg = len(segmentos) 	
			for index in range(totalSeg -1, 0 , -1):
				x= segmentos[index -1].xcor()
				y= segmentos[index-1].ycor()
				segmentos[index].goto(x,y)	

			if totalSeg > 0:
				x=cabeza.xcor()
				y=cabeza.ycor()
				segmentos[0].goto(x,y)	
				
			mov()
			colisiones()
			# validarLimites()
			time.sleep(posponer)


