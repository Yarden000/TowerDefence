import pygame
from settings import Vec2

class Projectile:
    speed = 500
    radius = 5
    # La classe Projectile représente un projectile tiré par une tour
    # TODO: Ajouter les attributs nécessaires pour le projectile
    def __init__(self, pos, dir, target = None):
        self.pos = Vec2(pos)
        self.target = target
        self.dir = Vec2(dir).normalize()
        self.enemies_hit = []

    # TODO: Ajouter la méthode pour déplacer le projectile
    def move(self, dt):
        if self.target:
            raise ValueError('not yet implemented')
        else:
            self.pos += self.dir * self.speed * dt
        # Cette méthode se charge de déplacer le projectile vers sa cible
        # Si le projectile atteint la cible, il doit infliger des dégâts et être retiré de la liste
        # Sinon, il continue à se déplacer vers la cible
        
        
    # TODO: Modifier la méthode pour dessiner le projectile 
    def draw(self, win):
        pygame.draw.circle(win, 'purple', self.pos, self.radius)  # Représente un tir avec un petit cercle bleu