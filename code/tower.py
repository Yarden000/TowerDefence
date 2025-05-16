import pygame
from settings import Vec2, cc_collision
from projectiles import Projectile
from enemies import Enemy

class Tower:
    radius = 15
    range = 150
    # La classe Tower représente une tour dans le jeu
    # TODO: Ajouter les attributs nécessaires pour la tour
    def __init__(self, game, pos):
        self.game = game
        self.cooldown = 0.5  # in seconds
        self.timefromlastshoot = 0
        self.pos = Vec2(pos) # Position de la tour

    # TODO: Ajouter la méthode pour tirer un projectile 

    def move_to(self, pos:Vec2):
        self.pos = pos
        
    def enemies_in_range(self):
        enemies = self.game.enemies
        in_range = [nme for nme in enemies if cc_collision(nme.pos, nme.radius, self.pos, self.range) ]
        return in_range
    
    def farthest_enemy(self, enemies:list[Enemy]):
        if enemies:
            farthest_enemy = max(enemies, key=lambda x: x.dist)
            return farthest_enemy
        return None

    def shoot(self, dt, enemies = None, projectiles = None):
        self.timefromlastshoot += dt
        if self.timefromlastshoot >= self.cooldown:
            self.timefromlastshoot %= self.cooldown
            if farthest := self.farthest_enemy(self.enemies_in_range()):
                dir = (farthest.pos - self.pos).normalize()
                self.game.add_projectile(Projectile(self.pos, dir))
            
        # Cette méthode se charge de sélectionner un ennemi et de tirer un projectile
        # Le projectile sera créé et ajouté à la liste des projectiles
        pass # TODO: Implémenter la logique de tir
        
    # TODO: Modifier la méthode pour dessiner la tour 
    def draw(self, screen, color = 'Black'):
        pygame.draw.circle(screen, color, self.pos, self.radius)
        pygame.draw.circle(screen, color, self.pos, self.range, width = 1)
