import pygame
import math

# Inicializar Pygame
pygame.init()

# Función para dibujar el sistema de Alpha Centauri
def dibujar_sistema_alpha_centauri():
    # Configurar la pantalla
    ancho, alto = 1200, 800
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Sistema Alpha Centauri")

    # Configurar la fuente para los nombres de los planetas
    pygame.font.init()
    fuente = pygame.font.Font(None, 24)  # Usar una fuente predeterminada

    # Colores
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)
    AMARILLO = (255, 255, 0)
    NARANJA = (255, 165, 0)
    AZUL = (0, 0, 255)
    ROJO = (255, 0, 0)

    # Posiciones de Alpha Centauri A y B
    alpha_centauri_a_x, alpha_centauri_a_y = ancho // 3, alto // 2
    alpha_centauri_b_x, alpha_centauri_b_y = 2 * ancho // 3, alto // 2

    # Propiedades de los planetas
    planetas_a = {
        "Planeta A1": {"a": 80, "b": 70, "velocidad": 0.015, "color": AZUL, "radio": 8, "angulo": 0},
        "Planeta A2": {"a": 120, "b": 110, "velocidad": 0.01, "color": ROJO, "radio": 10, "angulo": 0}
    }

    planetas_b = {
        "Planeta B1": {"a": 90, "b": 80, "velocidad": 0.02, "color": AZUL, "radio": 8, "angulo": 0},
        "Planeta B2": {"a": 130, "b": 120, "velocidad": 0.012, "color": ROJO, "radio": 10, "angulo": 0}
    }

    # Iniciar el bucle de animación
    corriendo = True

    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        pantalla.fill(NEGRO)

        # Dibujar Alpha Centauri A y B
        pygame.draw.circle(pantalla, AMARILLO, (alpha_centauri_a_x, alpha_centauri_a_y), 30)
        pygame.draw.circle(pantalla, NARANJA, (alpha_centauri_b_x, alpha_centauri_b_y), 25)

        # Dibujar las órbitas y los planetas alrededor de Alpha Centauri A
        for nombre, propiedades in planetas_a.items():
            a = propiedades["a"]
            b = propiedades["b"]
            velocidad = propiedades["velocidad"]
            color = propiedades["color"]
            radio = propiedades["radio"]

            # Calcular la posición del planeta en una órbita elíptica
            planeta_x = alpha_centauri_a_x + int(a * math.cos(propiedades["angulo"]))
            planeta_y = alpha_centauri_a_y + int(b * math.sin(propiedades["angulo"]))

            # Dibujar la órbita del planeta (elipse)
            for i in range(361):
                x = alpha_centauri_a_x + int(a * math.cos(math.radians(i)))
                y = alpha_centauri_a_y + int(b * math.sin(math.radians(i)))
                pantalla.set_at((int(x), int(y)), color)
            
            # Dibujar el planeta
            pygame.draw.circle(pantalla, color, (planeta_x, planeta_y), radio)

            # Dibujar el nombre del planeta
            texto = fuente.render(nombre, True, BLANCO)
            pantalla.blit(texto, (planeta_x + radio + 5, planeta_y - radio // 2))

            # Incrementar el ángulo del planeta
            propiedades["angulo"] += velocidad

        # Dibujar las órbitas y los planetas alrededor de Alpha Centauri B
        for nombre, propiedades in planetas_b.items():
            a = propiedades["a"]
            b = propiedades["b"]
            velocidad = propiedades["velocidad"]
            color = propiedades["color"]
            radio = propiedades["radio"]

            # Calcular la posición del planeta en una órbita elíptica
            planeta_x = alpha_centauri_b_x + int(a * math.cos(propiedades["angulo"]))
            planeta_y = alpha_centauri_b_y + int(b * math.sin(propiedades["angulo"]))

            # Dibujar la órbita del planeta (elipse)
            for i in range(361):
                x = alpha_centauri_b_x + int(a * math.cos(math.radians(i)))
                y = alpha_centauri_b_y + int(b * math.sin(math.radians(i)))
                pantalla.set_at((int(x), int(y)), color)
            
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