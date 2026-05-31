##!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level  # ATIVADO: Agora o Game sabe o que é o Level!


class Game:
    def __init__(self):
        pygame.init()
        # Procure essa linha no seu Game.py e mude para:
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT), flags=pygame.DOUBLEBUF | pygame.HWSURFACE)

    def run(self):
        menu = Menu(self.window)

        while True:
            menu_return = menu.run()

            # Se o jogador escolher alguma das opções de jogo (1P, 2P Coop ou 2P Comp)
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                # Passando a janela, o nome da fase e o modo de jogo selecionado no menu
                current_level = Level(self.window, 'Level1', menu_return)
                level_return = current_level.run()

            elif menu_return == MENU_OPTION[4]:  # EXIT
                pygame.quit()
                sys.exit()  # Garante o fechamento limpo no Linux