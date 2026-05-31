#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame
from abc import ABC, abstractmethod
import pygame.image



class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        # Carrega a imagem dinâmica conforme o nome da entidade
        # Mude a linha 16 para usar o caminho absoluto:
        self.surf = pygame.image.load(
            '/home/denubiagalindodealmeida/PycharmProjects/MountainShooter/asset/' + name + '.png').convert_alpha()

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass