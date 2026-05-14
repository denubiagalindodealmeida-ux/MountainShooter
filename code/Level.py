#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import name

import pygame

import pygame  # Não esqueça de importar o pygame no topo
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):  # Adicionado 'name' aqui
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)

            pygame.display.flip()