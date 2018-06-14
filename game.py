# -*- coding: utf-8 -*-

import pygame # Para gráficos
from pygame.locals import * # Variables para eventos
from pong import Pong # Para nuestro Pong <3

# Importar paletas
from ai_paddle import AIPaddle
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
    ai_paddle = AIPaddle(SCREENSIZE)
    player_paddle = PlayerPaddle(SCREENSIZE)

    running = True

    while running:
        clock.tick(64) # Limitar FPS's

        #Obtener eventos de pygame
        for event in pygame.event.get():
            # Evaluar evento QUIT
            if event.type == QUIT:
                # Salir del juego
                pygame.quit()
                running = False
            # Evaluar eventos del teclado
            if event.type == KEYDOWN:
                # Evaluar posición e la paleta
                if event.key == K_UP:
                    player_paddle.direction = -1
                elif event.key == K_DOWN:
                    player_paddle.direction = 1
            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    player_paddle.direction = 0

        # Actualizar pong
        ai_paddle.update(pong)
        player_paddle.update()
        pong.update(player_paddle, ai_paddle)

        # TODO: Mostrar mensaje en la pantalla
        if pong.hit_edge_left:
            print('GANASTE!')
            running = False
        elif pong.hit_edge_right:
            print('PERDISTE!')
            running = False

        # Mostrar un cuadro negro en la pantalla
        screen.fill((0, 0, 0))

        # Mostrar Paddle
        ai_paddle.render(screen)
        player_paddle.render(screen)
        # Mostrar Pong
        pong.render(screen)

        pygame.display.flip() # Mostrar pantalla

    pygame.quit()

main()
