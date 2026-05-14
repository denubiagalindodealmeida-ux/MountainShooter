#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):  # Corrigido: entity_name

        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                return list_bg

            case _:  # Caso padrão se não encontrar o nome
                return None


