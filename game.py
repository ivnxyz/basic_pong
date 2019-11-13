# -*- coding: utf-8 -*-

import pygame # Para gráficos
from pygame.locals import * # Variables para eventos
from pong import Pong # Para nuestro Pong <3

# Importar paletas
from player_paddle import PlayerPaddle

# Valores constantes
SCREENSIZE = (650, 380)

# Punto de entrada al programa
def main():
    pygame.init() # Interfaz básica
    pygame.font.init() # Texto

    screen = pygame.display.set_mode(SCREENSIZE) # Definir tamaño de la pantalla (width, height)
    clock = pygame.time.Clock() # Objeto Clock para limitar nuestros FPS

    # Crear Pong
    pong = Pong(SCREENSIZE)
    # Crear AI Paddle
    player1_paddle = PlayerPaddle(SCREENSIZE, "left")
    player2_paddle = PlayerPaddle(SCREENSIZE, "right")

    while True:
        clock.tick(64) # Limitar FPS's

        #Obtener eventos de pygame
        for event in pygame.event.get():
            # Evaluar evento QUIT
            if event.type == QUIT:
                # Salir del juego
                pygame.quit()
                quit()
            # Evaluar eventos del teclado
            if event.type == KEYDOWN:
                # Cambiar dirección de la paleta
                if event.key == K_UP:
                    player2_paddle.direction = -1
                if event.key == K_DOWN:
                    player2_paddle.direction = 1

                # Cambiar dirección de la paleta
                if event.key == 119:
                    player1_paddle.direction = -1
                if event.key == 115:
                    player1_paddle.direction = 1
            if event.type == KEYUP:
                # Deneter la paleta
                if event.key == K_UP or event.key == K_DOWN:
                    player2_paddle.direction = 0

                # Detener la paleta
                if event.key == 119 or event.key == 115:
                    player1_paddle.direction = 0

        # Actualizar pong
        player1_paddle.update()
        player2_paddle.update()

        pong.update(player2_paddle, player1_paddle)

        # TODO: Mostrar mensaje en la pantalla
        if pong.hit_edge_left:
            print("Ganó el jugador 2 (derecha)")
            pygame.quit()
            quit()
        elif pong.hit_edge_right:
            print("Ganó el jugador 1 (izquierda)")
            pygame.quit()
            quit()

        # Mostrar un cuadro negro en la pantalla
        screen.fill((0, 0, 0))

        # Mostrar Paddle
        player1_paddle.render(screen)
        player2_paddle.render(screen)
        # Mostrar Pong
        pong.render(screen)

        pygame.display.flip() # Mostrar pantalla

main()
