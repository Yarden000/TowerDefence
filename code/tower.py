import pygame


class Tower:
    # La classe Tower représente une tour dans le jeu
    # TODO: Ajouter les attributs nécessaires pour la tour
    def __init__(self, pos):
        self.pos = pos # Position de la tour

    # TODO: Ajouter la méthode pour tirer un projectile 
    def shoot(self, enemies, projectiles):
        # Cette méthode se charge de sélectionner un ennemi et de tirer un projectile
        # Le projectile sera créé et ajouté à la liste des projectiles
        pass # TODO: Implémenter la logique de tir
        
    # TODO: Modifier la méthode pour dessiner la tour 
    def draw(self, win):
        pygame.draw.circle(win, GREEN, (int(self.pos[0]), int(self.pos[1])), 15)
