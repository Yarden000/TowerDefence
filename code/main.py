import pygame  # Bibliothèque principale pour la création de la fenêtre, la gestion des événements et des dessins.
import math    # Fournit des fonctions mathématiques comme hypot pour calculer des distances.
import random  # Permet d'introduire des comportements aléatoires dans le jeu si besoin.
from settings import SCREEN_SIZE
from mapmaker import MapMaker

class Game:
    
    def __init__(self):
        pass

    def run(self):
        pygame.init()

        SURFACE = pygame.display.set_mode(SCREEN_SIZE)  # Crée une fenêtre pygame de dimensions spécifiées.
        pygame.display.set_caption("Tower Defense - Semaine 1 - Enemies")  # Donne un titre à la fenêtre.

        FPS = 60  # Permet de contrôler la fluidité de l'animation (60 images par seconde).

        clock = pygame.time.Clock()  # Objet permettant de contrôler le framerate
        run = True  # Contrôle principal de la boucle de jeu
        

        while run:
            clock.tick(FPS)
            SURFACE.fill('white')

            # TODO: Dessiner le chemin

            # TODO: Dessiner et déplacer les ennemis

            # Met à jour l'écran après tous les dessins
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()






if __name__ == "__main__":
    map_maker = MapMaker()
    exit, map = map_maker.run()
    game = Game()
    if not exit:
        game.run()