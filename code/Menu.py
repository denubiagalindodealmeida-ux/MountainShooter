#!/usr/bin/python
# -*- coding: utf-8 -*-
from cmath import rect

import pygame.image
from pygame import font, Surface, Rect  # Importado Rect e Surface corretamente

from code.const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW
from code.const import MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = 0  # <--- Criado aqui para evitar o NameError

    def run(self):
        # Carregar e dar play na música FORA do while para não travar o som
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                # Adicionado o 'self.' antes de menu_option
                if i == self.menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 150 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 150 + 30 * i))

            pygame.display.flip()

            # Verificação de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()



    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Corrigido o nome de 'text_center_pas' para 'pos' e tipos de fonte
        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)