"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.

"""
# A01701879 María José Díaz Sánchez 
# A00829556 Santiago Gonzalez Irigoyen
# Este código funciona permite dibujar líneas, cuadrados, círculos y triángulos de diferentes colores

from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    #Esta parte hace las líneas rectas
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    #Aquí se hacen los rectángulos usando vueltas por grados
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    #Aquí está el código del círculo, con un speed para hacerlo más rápido
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(130):
        speed(10)
        forward((end.x - start.x)/4)
        speed(10)
        left(2.86)
    
    end_fill()
     

def rectangle(start, end):
    "Draw rectangle from start to end."
    #Similar al cuadrado el código del rectángulo hace vueltas por ángulos
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward(end.y - start.y)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    #El código del triángulo también usa vueltas por ángulos
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    #funcion para iniciar
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')#comando para deshacer dibujo
#lista de colores y sus teclas 
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('orange'), 'O')#color añadido naranja
onkey(lambda: color('purple'), 'P')#color añadido morado
onkey(lambda: color('yellow'), 'Y')#color añadido amarillo
onkey(lambda: color('pink'), 'N')#color añadido rosa
#lista de las figuras y sus teclas
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
