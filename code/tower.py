import pygame
from settings import Vec2
from projectiles import Projectile

class Tower:
    radius = 15
    # La classe Tower représente une tour dans le jeu
    # TODO: Ajouter les attributs nécessaires pour la tour
    def __init__(self, game, pos):
        self.game = game
        self.cooldown = 0.5  # in seconds
        self.timefromlastshoot = 0
        self.pos = pos # Position de la tour

    # TODO: Ajouter la méthode pour tirer un projectile 
    def shoot(self, dt, enemies = None, projectiles = None):
        self.timefromlastshoot += dt
        if self.timefromlastshoot >= self.cooldown:
            self.timefromlastshoot -= self.cooldown
            dir = Vec2(1,0)
            self.game.add_projectile(Projectile(self.pos, dir))
            
        # Cette méthode se charge de sélectionner un ennemi et de tirer un projectile
        # Le projectile sera créé et ajouté à la liste des projectiles
        pass # TODO: Implémenter la logique de tir
        
    # TODO: Modifier la méthode pour dessiner la tour 
    def draw(self, screen):
        pygame.draw.circle(screen, 'Black', (int(self.pos[0]), int(self.pos[1])), self.radius)
