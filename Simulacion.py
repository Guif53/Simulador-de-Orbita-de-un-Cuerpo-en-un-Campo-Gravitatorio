"""Simulador de Órbita de un Cuerpo en un Campo Gravitatorio
Objetivo del Programa: Simular la órbita de un planeta o un satélite alrededor de un cuerpo masivo bajo la influencia de la gravedad.
Descripción: El programa debe calcular la trayectoria de un cuerpo en órbita utilizando las leyes de Kepler y la ley de gravitación de Newton. Puedes incluir visualizaciones de las trayectorias.
Conceptos: Leyes de Kepler, ecuaciones diferenciales, simulación numérica, gráficos 2D con matplotlib."""

import pygame
import math
from Sistema_Solar import dibujar_sistema_solar
from Apha_Centauri import dibujar_sistema_alpha_centauri

while True:
    # Pedirle al usuario a qué sistema solar quiere viajar
    destino = input("¿A qué sistema solar quieres viajar, al Sistema Solar o a Alpha Centauri? ").strip().lower()

    # Verificar el destino
    if destino == "sistema solar":
        dibujar_sistema_solar()
    elif destino == "alpha centauri":
        dibujar_sistema_alpha_centauri()
    else:
        print("Ese sistema solar no está en los datos.")

    # Preguntar si desea hacer otra consulta o terminar
    continuar = input("¿Quieres viajar a otro sistema solar? (si/no): ").strip().lower()
    if continuar != "si":
        print("Gracias por usar nuestros datos espaciales. Sigue Surcando los cielos! ")
        break