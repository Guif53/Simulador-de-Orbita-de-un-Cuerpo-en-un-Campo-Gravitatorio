import pygame
import math

# Inicializar Pygame
pygame.init()

# Función para dibujar el sistema solar
def dibujar_sistema_solar():
    # Configurar la pantalla
    ancho, alto = 1200, 800
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Sistema Solar")

    # Configurar la fuente para los nombres de los planetas
    pygame.font.init()
    fuente = pygame.font.Font(None, 24)  # Usar una fuente predeterminada

    # Colores
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    AMARILLO = (255, 255, 0)
    CYAN_CLARO = (0, 255, 255)  # Color claro para la órbita de Neptuno
    COLORES_PLANETAS = {
        "Mercurio": (169, 169, 169),
        "Venus": (238, 130, 238),
        "Tierra": (0, 0, 255),
        "Marte": (255, 0, 0),
        "Júpiter": (165, 42, 42),
        "Saturno": (210, 180, 140),
        "Urano": (173, 216, 230),
        "Neptuno": (0, 0, 139)
    }

    # Posición del Sol
    sol_x, sol_y = ancho // 2, alto // 2

    # Propiedades de los planetas y la Luna
    planetas = {
        "Mercurio": {"a": 60, "b": 50, "velocidad": 0.024, "radio": 5, "angulo": 0},
        "Venus": {"a": 90, "b": 80, "velocidad": 0.016, "radio": 8, "angulo": 0},
        "Tierra": {"a": 120, "b": 100, "velocidad": 0.01, "radio": 10, "angulo": 0},
        "Marte": {"a": 150, "b": 130, "velocidad": 0.008, "radio": 7, "angulo": 0},
        "Júpiter": {"a": 200, "b": 180, "velocidad": 0.004, "radio": 15, "angulo": 0},
        "Saturno": {"a": 250, "b": 220, "velocidad": 0.003, "radio": 13, "angulo": 0},
        "Urano": {"a": 300, "b": 270, "velocidad": 0.002, "radio": 10, "angulo": 0},
        "Neptuno": {"a": 350, "b": 320, "velocidad": 0.001, "radio": 10, "angulo": 0, "color_orbita": CYAN_CLARO}
    }

    # Propiedades de la Luna
    luna = {
        "color": (169, 169, 169), "radio_orbita": 20, "velocidad": 0.05, "radio": 3, "angulo": 0
    }

    # Iniciar el bucle de animación
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pantalla.fill(NEGRO)

        # Dibujar el Sol
        pygame.draw.circle(pantalla, AMARILLO, (sol_x, sol_y), 30)

        # Dibujar las órbitas y los planetas
        for nombre, propiedades in planetas.items():
            a = propiedades["a"]
            b = propiedades["b"]
            velocidad = propiedades["velocidad"]
            color = COLORES_PLANETAS[nombre]
            radio = propiedades["radio"]
            color_orbita = propiedades.get("color_orbita", color)  # Usar color especial si está definido

            # Calcular la posición del planeta en una órbita elíptica
            planeta_x = sol_x + int(a * math.cos(propiedades["angulo"]))
            planeta_y = sol_y + int(b * math.sin(propiedades["angulo"]))

            if nombre == "Tierra":
                # Dibujar la órbita de la Luna
                pygame.draw.circle(pantalla, luna["color"], (planeta_x, planeta_y), luna["radio_orbita"], 1)

                # Calcular la posición de la Luna
                luna_x = planeta_x + int(luna["radio_orbita"] * math.cos(luna["angulo"]))
                luna_y = planeta_y + int(luna["radio_orbita"] * math.sin(luna["angulo"]))

                # Dibujar la Luna
                pygame.draw.circle(pantalla, luna["color"], (luna_x, luna_y), luna["radio"])

                # Incrementar el ángulo de la Luna
                luna["angulo"] += luna["velocidad"]

            # Dibujar la órbita del planeta (elipse)
            for i in range(361):
                x = sol_x + int(a * math.cos(math.radians(i)))
                y = sol_y + int(b * math.sin(math.radians(i)))
                pantalla.set_at((int(x), int(y)), color_orbita)
            
            # Dibujar el planeta
            pygame.draw.circle(pantalla, color, (planeta_x, planeta_y), radio)

            # Dibujar el nombre del planeta
            texto = fuente.render(nombre, True, BLANCO)
            pantalla.blit(texto, (planeta_x + radio + 5, planeta_y - radio // 2))

            # Incrementar el ángulo del planeta
            propiedades["angulo"] += velocidad

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar la velocidad de la animación
        pygame.time.delay(10)

    pygame.quit()
