"""Module for sounds in the game"""
import pygame.mixer


class Sounds:

    def __init__(self):
        pygame.mixer.init()
        self.explosion = pygame.mixer.Sound( "..\sounds\explosion.wav" )
