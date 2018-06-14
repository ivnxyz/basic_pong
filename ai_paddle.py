# -*- coding: utf-8 -*-

import pygame # Para gráficos

class AIPaddle:

    # Método de inicialización
    def __init__(self, screensize):
        self.screensize = screensize

        # Definir centro
        self.center_x = 5
        self.center_y = int(screensize[1] * 0.5)

        # Definir tamaño
        self.height = 70
        self.width = 10
        # TODO: Ajusta el tamaño de la paleta conforme la partida avanza
        # para hacer el juego más difícil

        # Crear rectángulo
        self.rect = pygame.Rect(0, self.center_y - (self.height * 0.5), self.width, self.height)
        self.color = (255, 255, 255)

        # Definir velocidad
        self.speed = 2.7

    # Actualizar Paddle
    def update(self, pong):
        # Determinar si Pong está arriba
        if pong.rect.top < self.rect.top:
            self.center_y -= self.speed
        elif pong.rect.bottom > self.rect.bottom:
            self.center_y += self.speed

        # Actualizar centro
        self.rect.center = (self.center_x, self.center_y)

    # Renderizar Paddle
    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
