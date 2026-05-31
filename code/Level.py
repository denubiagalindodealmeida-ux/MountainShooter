#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
import os

from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.const import COLOR_WHITE

WIN_HEIGHT = 600


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

        self.timeout = 60000  # 60 segundos em milissegundos

    def run(self):
        # 1. Para e descarrega a música anterior (do menu ou da fase anterior)
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        # 2. Carrega a música de forma AUTOMÁTICA baseada no nome do Level
        try:
            import os
            pasta_projeto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

            # Se self.name for "Level1", nome_da_musica vira "level1.mp3"
            # Se self.name for "Level2", nome_da_musica vira "level2.mp3"
            nome_da_musica = f"{self.name.lower()}.mp3"

            caminho_musica = os.path.join(pasta_projeto, 'asset', 'musicas', nome_da_musica)

            pygame.mixer.music.load(caminho_musica)
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)  # Toca em loop
            print(f"Música {nome_da_musica} iniciada com sucesso para o {self.name}!")
        except pygame.error as e:
            print(f"Erro ao tocar a música automática do level: {e}")

        relogio = pygame.time.Clock()
        rodando = True
        # ... o resto do seu loop (while rodando:) continua igual abaixo
        while rodando:
            relogio.tick(60)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

            # Limpa a tela antes de desenhar
            self.window.fill((0, 0, 0))

            # Movimenta as entidades
            for ent in self.entity_list:
                if hasattr(ent, 'move'):
                    ent.move()

            # Desenha as entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)

            # Desenha os textos por cima de tudo
            self.level_text(text_size=14, text=f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s',
                            text_color=COLOR_WHITE, text_pos=(10, 5))
            self.level_text(text_size=14, text=f'fps: {relogio.get_fps():.0f}', text_color=COLOR_WHITE,
                            text_pos=(10, WIN_HEIGHT - 35))
            self.level_text(text_size=14, text=f'entidades: {len(self.entity_list)}', text_color=COLOR_WHITE,
                            text_pos=(10, WIN_HEIGHT - 20))

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        if not pygame.font.get_init():
            pygame.font.init()

        text_font = pygame.font.SysFont(name='Lucida sans Typewriter', size=text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)