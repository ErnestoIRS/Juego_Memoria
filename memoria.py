#A00827434 Ernesto García González
#A00827107 Regina González Quijano

from random import *
from turtle import *
from freegames import path

#Imágen de fondo.
car = path('car.gif')

#Número de cuadros en la ventana. 32*2 para cumplir los 64 cuadros en parejas. 
tiles = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E']*2

#Variable que indica el estado de cada cuadro.
state = {'mark': None}

#Variable que indica el número de clicks que se han hecho.
global tapCount
tapCount = 0

#Variable que indica que al inicio todos los cuadros estan 'escondidos'.
hide = [True] * 64

#Variable que indica el marcador.
stateScore = {'score': 0}
writer = Turtle(visible=False)

#Función que dibuja los cuadros que el usuario podrá seleccionar.
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    
    #Medidas del cuadrado.
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#Convierte las coordenadas de la ventana a coordenadas que indican la posición del cuadro en la ventana.
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#Convierte las coordenadas del cuadro a coordenadas en la ventana.
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#Función que controla lo que sucede al dar click en un cuadro.
def tap(x, y):
    "Update mark and hidden tiles based on tap."
    
    #Se llama el contador de clicks y se suma cada click.
    global tapCount
    tapCount = tapCount + 1
    spot = index(x, y)
    mark = state['mark']
    print('El número de clicks que llevas son:', tapCount)

    #Condiciones para determinar que los numeros NO COINCIDEN y los cuadros regresan a su estado original.
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        print("aqui if")
        state['mark'] = spot
        
    #Si no es asi, los números son iguales y ambos cuadros (mark y spot) se revelan.    
    else:
        print("aqui else")
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        stateScore['score'] += 1
    
#Función que muestra el tablero dependiendo del estado de cada cuadro (hide = None o False).
def draw():
    
    #Se dibuja la imágen de fondo.
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    #Si el estado del cuadro es 'escondido', se dibuja el cuadro blanco.
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)
   
    #Se evalua si mark esta descubierto o no.
    mark = state['mark']

    #Si el cuadro esta seleccionado y su estado es 'escondido' se muestra el número.
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 14, y + 3)
        color('black')
        write(tiles[mark], font=('Arial', 25, 'normal'))
    
    #Se escribe el puntaje actual.
    writer.color('orange')
    writer.write(stateScore['score'], font=('Arial', 15, 'bold'))

#Si todos los cuadros se encuentran volteados, se termina el juego.
    if (hide == [False] * 64):
        print ("Juego terminado")
        return

    update()
    ontimer(draw, 10)

#Se hace el acomodo de tiles.
shuffle(tiles)
setup(420, 420, 370, 0)

addshape(car)
hideturtle()

#Se indica la posición del marcador.
writer.goto(185, 170)
tracer(False)

onscreenclick(tap)
draw()
done()