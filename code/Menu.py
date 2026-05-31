#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame.image
from pygame import font, Surface, Rect

from code.const import WIN_WIDTH, COLOR_ORANGE, COLOR_WHITE, COLOR_YELLOW
from code.const import MENU_OPTION


class Menu:
    def __init__(self, window):
        self.window = window
        # Mude esta linha:
        self.surf = pygame.image.load('/home/denubiagalindodealmeida/PycharmProjects/MountainShooter/asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)
        self.menu_option = 0  # Controla qual opção está selecionada

    def run(self):
        # --- REATIVADO E COM O CAMINHO CORRETO ---
        pygame.mixer_music.load('/home/denubiagalindodealmeida/PycharmProjects/MountainShooter/asset/Menu.mp3')
        pygame.mixer_music.play(-1)  # O -1 faz a música tocar em loop infinito

        relogio = pygame.time.Clock()
        while True:
            # ... resto do código do menu continua igual ...
            relogio.tick(60)  # Limita o menu a 60 FPS (Evita consumo de 100% da CPU)

            # 1. DESENHAR IMAGENS E TEXTOS
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Mountain", COLOR_ORANGE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == self.menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, ((WIN_WIDTH / 2), 150 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 150 + 30 * i))

            # 2. CAPTURAR EVENTOS DO USUÁRIO
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()  # Fechamento limpo para o Linux

                if event.type == pygame.KEYDOWN:
                    # TRATA A SETA PARA BAIXO
                    if event.key == pygame.K_DOWN:
                        if self.menu_option < len(MENU_OPTION) - 1:
                            self.menu_option += 1
                        else:
                            self.menu_option = 0

                    # TRATA A SETA PARA CIMA
                    elif event.key == pygame.K_UP:
                        if self.menu_option > 0:
                            self.menu_option -= 1
                        else:
                            self.menu_option = len(MENU_OPTION) - 1

                    # TRATA O ENTER (Seleciona a opção e fecha o menu)
                    elif event.key == pygame.K_RETURN:
                        return MENU_OPTION[self.menu_option]

            # 3. ATUALIZAR A TELA (Apenas um flip por ciclo do while é necessário)
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        # Correção automática de inicialização do módulo de fontes se necessário
        if not pygame.font.get_init():
            pygame.font.init()

        text_font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)