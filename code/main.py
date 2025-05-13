import pygame  # Bibliothèque principale pour la création de la fenêtre, la gestion des événements et des dessins.
import math    # Fournit des fonctions mathématiques comme hypot pour calculer des distances.
import random  # Permet d'introduire des comportements aléatoires dans le jeu si besoin.
from settings import SCREEN_SIZE, display_path
from mapmaker import MapMaker
from enemies import Enemy

class Game:
    
    def __init__(self, map_maker: MapMaker):
        self.displayer = Displayer(self)
        self.map_maker = map_maker
        self.path = self.map_maker.path
        self.path_points = self.map_maker.points
        self.path_precision = self.map_maker.precision

        self.enemies = [Enemy(self.path)]
        self.towers = []

    def move_enemies(self, dt):
        for enemy in self.enemies:
            enemy.move(dt, self.path_points, self.path_precision)

    def run(self):
        pygame.init()
        dt = 0
        FPS = 60  # Permet de contrôler la fluidité de l'animation (60 images par seconde).

        clock = pygame.time.Clock()  # Objet permettant de contrôler le framerate
        run = True  # Contrôle principal de la boucle de jeu
        
        
        while run:
            clock.tick(FPS)
            dt = clock.get_time() / 1000
            
            # move enemies
            self.move_enemies(dt)

            self.displayer.display(dt) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
 
        pygame.quit()


class Displayer:

    def __init__(self, game):
        self.game:Game = game
        self.screen = pygame.display.set_mode(SCREEN_SIZE)  # Crée une fenêtre pygame de dimensions spécifiées.

    def display_enemies(self, enemies:list[Enemy]):
        for enemie in enemies:
            enemie.draw(self.screen)


    def display(self, dt):
        self.screen.fill('white')
        
        pygame.display.set_caption("Tower Defense | dt = " + str(dt))  # Donne un titre à la fenêtre.
        
        
        display_path(self.game.path_points, self.screen)
        self.display_enemies(self.game.enemies)

        # Met à jour l'écran après tous les dessins
        pygame.display.update()

if __name__ == "__main__":
    map_maker = MapMaker()
    # map_maker.run()
    game = Game(map_maker)
    if not map_maker.exit:
        game.run()