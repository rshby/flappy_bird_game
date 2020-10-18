# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:15:10 2020

@author: ROG
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((576, 1024))

while True:
    for event in pygame.event.get():
        if event.type = pygame.QUIT:
            pygame.quit
        
    pygame.display.update()