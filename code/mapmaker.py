import pygame  # Bibliothèque principale pour la création de la fenêtre, la gestion des événements et des dessins.
import math    # Fournit des fonctions mathématiques comme hypot pour calculer des distances.
import random  # Permet d'introduire des comportements aléatoires dans le jeu si besoin.
import svgelements
from svgelements import Path, Line, Arc, CubicBezier, QuadraticBezier, Close, Move
# Path = 1, Line = 2, Arc = 3, CubicBezier = 4, QuadraticBezier = 5, Close = 6, Move = 7
# 



class MapMaker:

    def __init__(self):
        self.path = Path

    def run(self):
        pygame.init()

        WIDTH, HEIGHT = 800, 600  # Modélise l'espace de jeu où se déplaceront ennemis et tours.
        SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))  # Crée une fenêtre pygame de dimensions spécifiées.
        pygame.display.set_caption("Tower Defense - MapMaker")  # Donne un titre à la fenêtre.

        FPS = 60  # Permet de contrôler la fluidité de l'animation (60 images par seconde).

        clock = pygame.time.Clock()  # Objet permettant de contrôler le framerate
        run = True  # Contrôle principal de la boucle de jeu
        
        finished = False
        drawing = False
        type = None
        while not finished:

            clock.tick(FPS)
            SURFACE.fill('white')

            mouse_pos = pygame.mouse.get_pos()
            keys = pygame.key.get_pressed()
            

            if drawing:

                # select type
                if type == None:
                

            

            # Met à jour l'écran après tous les dessins
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()