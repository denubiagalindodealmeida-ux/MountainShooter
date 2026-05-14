#!/usr/bin/python
# -*- coding: utf-8 -*-
from idlelib import window

import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu
from code.const import MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        # Primeiro, criamos o objeto menu usando a janela do jogo
        menu = Menu(self.window)

        while True:
            # Tudo dentro do while deve ter o mesmo alinhamento inicial
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:

                level = level(self.window, 'level1', menu_return)
                level_return = level.run()

            if menu_return == MENU_OPTION[4]:
                pygame.quit()  # Fecha o Pygame
                quit()  # Encerra o programa

            else:
                pass
