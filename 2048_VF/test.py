import random

# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400, 300))

# Initialing Color
color = (255, 0, 0)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(30, 30, 90, 90), border_radius=4)
print(pygame.draw)
pygame.display.flip()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print('coucou')
'''''
mot ='sloggy'

def melange_mot(mot):
    nouveau_mot = ''
    index = []
    i = 0
    while i < len(mot):
        n = random.randint(0, len(mot) - 1)
        if not index.__contains__(n):
            nouveau_mot += mot[n]
            index.append(n)
            i += 1
    return nouveau_mot

print(mot)
nouveau_mot = melange_mot(mot)
print(nouveau_mot)
'''''

