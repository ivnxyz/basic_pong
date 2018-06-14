 # -*- coding: utf-8 -*-

import pygame # Para gráficos
import random

DIRECTIONS = [1, -1]

class Pong:

    # Método de inicialización
    def __init__(self, screensize):
        self.screensize = screensize

        # Centrar Pong
        self.center_x = int(screensize[0] * 0.5)
        self.center_y = int(screensize[1] * 0.5)

        # Definir tamaño
        self.radius = 8
        self.rect = pygame.Rect(self.center_x - self.radius,
                                self.center_y - self.radius,
                                self.radius * 2, self.radius * 2)

        self.color = (255, 255, 255)
        self.direction = [random.choice(DIRECTIONS), random.choice(DIRECTIONS)] 

        # Determinar velocidad
        self.speed_x = 4
        self.speed_y = 3
        # TODO: Cambia la velocidad conforme el juego progresa
        # para hacerlo más difícil

        self.hit_edge_left = False
        self.hit_edge_right = False

    # Actualizar Pong
    def update(self, player_paddle=None, ai_paddle=None):
        # Actualizar posición del Pong
        self.center_x += self.direction[0] * self.speed_x
        self.center_y += self.direction[1] * self.speed_y

        # Actualizar centro
        self.rect.center = (self.center_x, self.center_y)

        # Evaluar posición vertical de la bola
        if self.rect.top <= 0:
            self.direction[1] = 1
        elif self.rect.bottom >= self.screensize[1] - 1: #Empezamos en el pixel 0, no 1
            self.direction[1] = -1

        # Evaluar posición horizontal de la bola
        if self.rect.right >= self.screensize[0] - 1:
            self.hit_edge_right = True
        elif self.rect.left <= 0:
            self.hit_edge_left = True

        # Evaluar paleta con la que chocó
        if self.rect.colliderect(player_paddle.rect):
            self.direction[0] = -1
        elif self.rect.colliderect(ai_paddle.rect):
            self.direction[0] = 1

    # Mostrar Pong
    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
