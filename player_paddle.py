# -*- coding: utf-8 -*-

import pygame # Para gráficos
from ai_paddle import AIPaddle # Importar AIPaddle

class PlayerPaddle(AIPaddle):

    # Método de inicialización
    def __init__(self, screensize):
        self.screensize = screensize

        # Definir centro
        self.center_x = screensize[0] - 5
        self.center_y = int(screensize[1] * 0.5)

        # Definir tamaño
        self.height = 70
        self.width = 10
        # TODO: Ajusta el tamaño de la paleta conforme la partida avanza
        # para hacer el juego más difícil

        # Crear rectángulo
        self.rect = pygame.Rect(0, self.center_y - (self.height * 0.5), self.width, self.height)
        self.color = (255, 255, 255)

        # Definir velocidad y dirección
        self.speed = 7
        self.direction = 0

    def update(self):
        # Modificar posición
        self.center_y += self.direction * self.speed

        # Modificar rectángulo
        self.rect.center = (self.center_x, self.center_y)

        # Evaluar si el usuario se ha salido de la pantalla
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screensize[1] - 1:
            self.rect.bottom = self.screensize[1] - 1
