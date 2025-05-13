'''
helpull resources:
    svg: https://pypi.org/project/svgpathtools/ https://www.w3.org/TR/SVG/paths.html#PathLengthAttribute
'''

import pygame  # Bibliothèque principale pour la création de la fenêtre, la gestion des événements et des dessins.
import math    # Fournit des fonctions mathématiques comme hypot pour calculer des distances.
import random  # Permet d'introduire des comportements aléatoires dans le jeu si besoin.
from svgpathtools import Path, Line, Arc, CubicBezier, QuadraticBezier
from settings import SCREEN_SIZE, display_path, path_points, tup_to_comp



class MapMaker:

    def __init__(self):
        # temporary
        self.precision = 5
        self.path = Path()
        vertecies = [(0, 150), (500, 150), (500, 300), (800, 300), (800, 450)]
        for i in range(len(vertecies) - 1):
            self.path += Path(Line(tup_to_comp(vertecies[i]), tup_to_comp(vertecies[i+1])))
        self.path += Path(CubicBezier(800 + 450j, 500 - 200j, 800 + 800j, 450j))
        '''
        self.path = Path()
        self.path += Path(QuadraticBezier(200 + 100j, 200j, 200 + 400j))
        self.path += Path(CubicBezier(200 + 400j, 600j, 800 + 500j, 300 + 600j))
        '''
        self.points = path_points(self.path, self.precision)
        self.exit = False  # if true means you want to close the program => no need to run the game in the main file

    def run(self):
        
        temporairy_precision = 50

        pygame.init()

        SCREEN = pygame.display.set_mode(SCREEN_SIZE)  # Crée une fenêtre pygame de dimensions spécifiées.
        pygame.display.set_caption("Tower Defense - MapMaker")  # Donne un titre à la fenêtre.

        FPS = 60  # Permet de contrôler la fluidité de l'animation (60 images par seconde).

        clock = pygame.time.Clock()  # Objet permettant de contrôler le framerate
        run = True  # Contrôle principal de la boucle de jeu
        
        finished = False
        drawing = True

        '''path info'''
        # TODO for now only lines work
        start_pos: None|tuple = None
        end_pos = None
        # (if line just start_point and end_point needed)
        # if Arc

        type: None|Line|Arc|QuadraticBezier|CubicBezier = None
        
        while not finished:

            clock.tick(FPS)
            SCREEN.fill('white')

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()

            

            
            '''
            if drawing:

                # type of path selected
                if keys[pygame.K_1]:
                    type = Line
                if keys[pygame.K_2]:
                    type = Arc
                if keys[pygame.K_3]:
                    type = QuadraticBezier
                if keys[pygame.K_4]:
                    type = CubicBezier

                if type == None:
                    pass
                        
                elif type == Line:
                    pass
                elif type == Arc:
                    raise ValueError('not yet implemented')
                    pass
                elif type == QuadraticBezier:
                    raise ValueError('not yet implemented')
                    pass
                elif type == CubicBezier:
                    raise ValueError('not yet implemented')
                    pass
            '''

            
            # displays
            display_path(path_points(self.path, temporairy_precision), SCREEN, color = 'black', thikness = temporairy_precision)
            # Met à jour l'écran après tous les dessins
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                    self.exit = True
            
            if keys[pygame.K_q]:
                finished = True

        pygame.quit()

        self.points = path_points(self.path, self.precision)