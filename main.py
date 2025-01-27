"""
# [M4.L1] Carrera de tortugas - Actividad # 4 "Dos Jugadores"

# Objetivo: Crear una tortuga y programar el dibujo de la pista de carreras

Parche: ¿¡ El profe se equivocó copiando y pegando código ?! Sipi

> Cambiamos el nombre de la segunda tortuga de "primera" a "segunda"
> Revisamos su posición inicial
"""

import turtle

"""   ##########################
     # > VARIABLES GLOBALES < #
    ##########################    """

velocidad_corredores = 5 # Controla la velocidad de la animación (no a la que "corren", sino a la que las dibujamos)
cant_tortugas = 0 #contador con la cantidad de corredores
distancia_entre_tortugas = 40
y_inicial_tortugas = 80
x_inicial_tortugas = -230

"""   #########################
     # > PISTA DE CARRERAS < #
    #########################    """

# Tortuga que dibuja el tablero 🐢 (t)
t = turtle.Turtle() # Creamos la tortuga
t.penup()           # Levantamos el trazo
t.goto(-200, 100)   # Buscamos más espacio para la pista
t.pendown()         # Volvemos a dibujar
t.speed(0)          # Aceleramos la animiación de la tortuga
t.color(0,0,0)      # Seteo el color de dibujo a negro

# Pista de carreras
cant_secciones_pista = 15
ancho_secciones_pista = 20
# ¿Cuántos píxeles tiene que recorrer la tortuga hasta curzar la meta?
# Distancia de carrera = cant_secciones_pista * ancho_secciones_pista

long_secciones_pista = 150

# Bucle que dibuja la pista:
for pista in range(1, (1 + cant_secciones_pista)):
    t.write(str(pista))         # Escribe el Nº de la sección (1~15)
    t.right(90)                 # Gira 90º (mirando hacia abajo)
    t.fd(long_secciones_pista)  # Dibuja la línea de la sección
    t.bk(long_secciones_pista)  # Retrocede y "vuelve" arriba
    t.left(90)                  # Reposiciona la tortuga para que mire a la dcha
    t.fd(ancho_secciones_pista) # Avanza el ancho hasta la próxima sección

# -> Inserte aquí código bandera meta
t.color(255, 0, 0)
t.right(90)
t.fd(long_secciones_pista)
t.bk(long_secciones_pista)
t.left(90)
t.color("black")
######################################

"""   #############################
     # > CORREDORAS (TORTUGAS) < #
    #############################    """

# PRIMERA
primera = turtle.Turtle()              # Creamos una nueva tortuga
cant_tortugas += 1                     # La registramos como corredora
primera.shape("turtle")                # Le damos forma de tortuga
primera.color("crimson")               # Le asignamos otro color (ROJO)
primera.speed(0)                       # Aceleramos su animación
primera.penup()                        # Levantamos el trazo para reubicarla

# La posicionamos DETRÁS de la línea de partida
#primera.goto(-230, 80)
primera.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
primera.speed(velocidad_corredores)    # Cambiamos su velocidad de animación para la carrera

########################################

# SEGUNDA
segunda = turtle.Turtle()              # Creamos una nueva tortuga
cant_tortugas += 1                     # La registramos como corredora
segunda.shape("turtle")                # Le damos forma de tortuga
segunda.color("navy")                  # Le asignamos otro color (AZUL)
segunda.speed(0)                       # Aceleramos su animación
segunda.penup()                        # Levantamos el trazo para reubicarla

# La posicionamos DETRÁS de la línea de partida
#segunda.goto(-230, 40)
segunda.goto(x_inicial_tortugas, (y_inicial_tortugas - (distancia_entre_tortugas * (cant_tortugas - 1))))
segunda.speed(velocidad_corredores)    # Cambiamos su velocidad de animación para la carrera

########################################

# Colorín colorado el código ha terminado :D