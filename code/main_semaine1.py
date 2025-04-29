"""install svg: python3 -m pip install --user svg.py"""


# Importation des bibliothèques nécessaires
import pygame  # Bibliothèque principale pour la création de la fenêtre, la gestion des événements et des dessins.
import math    # Fournit des fonctions mathématiques comme hypot pour calculer des distances.
import random  # Permet d'introduire des comportements aléatoires dans le jeu si besoin.
import svg
help(svg)
# Initialisation de Pygame
pygame.init()  # Démarre l'ensemble des modules de pygame pour permettre l'affichage graphique et les interactions.

# Définition des dimensions de la fenêtre du jeu
WIDTH, HEIGHT = 800, 600  # Modélise l'espace de jeu où se déplaceront ennemis et tours.
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # Crée une fenêtre pygame de dimensions spécifiées.
pygame.display.set_caption("Tower Defense - Semaine 1 - Enemies")  # Donne un titre à la fenêtre.

# Définition des couleurs utilisées dans le jeu (format RGB)
WHITE = (255, 255, 255)  # Utilisé pour le fond de l'écran (neutralité).
BLACK = (0, 0, 0)        # Utilisé pour les tours.
RED = (255, 0, 0)        # Utilisé pour les ennemis (indique danger, menace).
GREEN = (0, 255, 0)      # Utilisé pour la barre de vie restante.
BLUE = (0, 0, 255)       # Utilisé pour les projectiles tirés par les tours.

# Définition du nombre d'images par seconde
FPS = 60  # Permet de contrôler la fluidité de l'animation (60 images par seconde).

# Définition du chemin que suivent les ennemis
PATH = [(50, 50), (300, 50), (300, 250), (500, 250), (500, 150), (750, 150), (750, 500), (50, 500)]  
# Liste de points (x, y) par lesquels les ennemis doivent passer, modélise leur trajet.

# Définition de la classe Enemy (ennemi du jeu)
class Enemy:
    def __init__(self, path):
        self.path = path  # Stocke le chemin que l'ennemi doit suivre.
        self.path_index = 0  # Indice du point actuel dans le chemin.
        self.pos = list(self.path[0])  # Position initiale de l'ennemi (premier point du chemin).
        self.speed = 2  # Vitesse de déplacement par mise à jour.

    def move(self):
        # Permet à l'ennemi de se déplacer vers le prochain point du chemin
        pass
        
    def draw(self, win):
        # Dessine l'ennemi sur l'écran
        pass

# Fonction principale contenant la boucle du jeu
def main():
    clock = pygame.time.Clock()  # Objet permettant de contrôler le framerate
    run = True  # Contrôle principal de la boucle de jeu
    
    NMI = Enemy(PATH)  # Crée une instance de l'ennemi avec le chemin défini

    while run:
        clock.tick(FPS)
        WIN.fill(WHITE)

        # TODO: Dessiner le chemin

        # TODO: Dessiner et déplacer les ennemis

        # Met à jour l'écran après tous les dessins
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
