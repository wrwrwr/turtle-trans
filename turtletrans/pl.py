from .translate import translate_methods, turtle_subclass

# Translate the class name itself.
Żółw = Żółwik = turtle_subclass("Żółw")

# Original method --> list of aliases (order as in turtle docs).
translate_methods(Żółw, {
    # Turtle motion.
    'forward': ("naprzód", "np", "doprzodu", "dp"),
    'back': ("wstecz", "ws", "dotyłu", "dt"),
    'right': ("naprawo", "prawo", "prawa", "pw"),
    'left': ("nalewo", "lewo", "lewa", "lw"),
    'goto': ("idźdo", "napoz", "zmieńpoz", "zpoz"),
    'setx': ("zmieńx", "zx"),
    'sety': ("zmieńy", "zy"),
    'setheading': ("obróć", "skieruj", "zmieńkierunek", "zk"),
    'home': ("dodomu", "dom", "naśrodek", "środek", "wróć"),
    'circle': ("okrąg", "koło", "kółko"),
    'dot': ("kropka", "punkt"),
    'stamp': ("stempel", "pieczęć", "pieczątka"),
    'clearstamp': ("usuństempel", "usuńpieczęć", "usuńpieczątkę"),
    'clearstamps': ("usuństemple", "usuńpieczęci", "usuńpieczątki"),
    'undo': ("cofnij", "c"),
    'speed': ("szybkość", "prędkość"),

    # Turtle state.
    'position': ("pozycja", "poz"),
    'towards': ("wkierunku", "kierunek"),
    'xcor': ("wspx", "x"),
    'ycor': ("wspy", "y"),
    'heading': ("kierunek",),
    'distance': ("odległość",),

    # Measurement.
    'degrees': ("stopnie",),
    'radians': ("radiany",),

    # Pen control.
    'pendown': ("opuśćpisak", "opuść", "opu"),
    'penup': ("podnieśpisak", "podnieś", "pod"),
    'pensize': ("rozmiarpisaka", "rozmiar", "roz", "ugp"),
    'pen': ("pisak",),
    'isdown': ("czyopuszczony", "opuszczony", "czypisze"),
    'pencolor': ("kolorpisaka", "kolpis", "ukp"),
    'fillcolor': ("kolormalowania", "kolmal", "ukm"),
    'color': ("kolor", "kol", "uk"),
    'filling': ("malowanie", "czymaluje", "wypełnianie", "czywypełnia"),
    'begin_fill': ("rozpocznij_malowanie", "maluj", "wypełniaj"),
    'end_fill': ("zakończ_malowanie", "niemaluj", "niewypełniaj"),
    'reset': ("resetuj", "cs"),
    'clear': ("wyczyść", "czyść"),
    'write': ("pisz", "napisz", "tekst"),

    # Turtle state.
    'hideturtle': ("schowaj", "chowaj", "ukryj", "sż"),
    'showturtle': ("pokaż", "pż"),
    'isvisible': ("czywidoczny", "widoczny"),

    # Appearance.
    'shape': ("kształt",),
    'resizemode': ("trybrozmiaru",),
    'shapesize': ("rozmiarkształtu", "rozmiarżółwia"),
    'shearfactor': ("ścięcie",),
    'tilt': ("odchylenie",),
    'tiltangle': ("kątodchylenia",),
    'shapetransform': ("przekształcenie",),
    'get_shapepoly': ("wielokąt_kształtu",),

    # Events.
    'onclick': ("pokliknięciu",),
    'onrelease': ("popuszczeniu",),
    'ondrag': ("poprzeciągnięciu",),

    # Special.
    'begin_poly': ("rozpocznijwielokąt",),
    'end_poly': ("zakończwielokąt",),
    'get_poly': ("nagranywielokąt",),
    'clone': ("klonuj",),
    'getturtle': ("zółw",),
    'getscreen': ("obraz",),
    'setundobuffer': ("buforcofania",),
    'undobufferentries': ("wpisybuforacofania", "wpisybuforucofania"),
})
