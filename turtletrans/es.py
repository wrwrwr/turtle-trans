from turtle import Turtle

from .translate import translate_methods

# Translate the class name itself.
Tortuga = Turtle

# Original method --> list of aliases (order as in turtle docs).
# TODO: Please correct and fill in :-)
translate_methods(Turtle, {
    # Turtle motion.
    'forward': ("adelante", "ad"),
    'back': ("haciaatrás", "ha"),
    'right': ("derecho", "dr"),
    'left': ("izquierda", "iz"),
    'goto': ("ir"),
    'setx': (),
    'sety': (),
    'setheading': (),
    'home': (),
    'circle': ("circulo",),
    'dot': (),
    'stamp': (),
    'clearstamp': (),
    'clearstamps': (),
    'undo': ("deshacer", "d"),
    'speed': ("velocidad", "rapidez"),

    # Turtle state.
    'position': ("posición",),
    'towards': (),
    'xcor': (),
    'ycor': (),
    'heading': (),
    'distance': ("distancia",),

    # Measurement.
    'degrees': ("grados",),
    'radians': ("radianes",),

    # Pen control.
    'pendown': (),
    'penup': (),
    'pensize': (),
    'pen': (),
    'isdown': (),
    'pencolor': (),
    'fillcolor': (),
    'color': (),
    'filling': (),
    'begin_fill': (),
    'end_fill': (),
    'reset': (),
    'clear': (),
    'write': (),

    # Turtle state.
    'hideturtle': (),
    'showturtle': (),
    'isvisible': (),

    # Appearance.
    'shape': (),
    'resizemode': (),
    'shapesize': (),
    'shearfactor': (),
    'tilt': (),
    'tiltangle': (),
    'shapetransform': (),
    'get_shapepoly': (),

    # Events.
    'onclick': (),
    'onrelease': (),
    'ondrag': (),

    # Special.
    'begin_poly': (),
    'end_poly': (),
    'get_poly': (),
    'clone': (),
    'getturtle': (),
    'getscreen': (),
    'setundobuffer': (),
    'undobufferentries': (),
})
