import math
from svgpathtools import Path, Line, Arc, CubicBezier, QuadraticBezier
import pygame
from settings import comp_to_tup
import random

class Enemy_spawner:

    def __init__(self, game):
        self.game = game
        self.averagw_spawn_rate = 1  # average number of enemies spawned each second


    def spawn(self, dt):
        spawn_prob = self.averagw_spawn_rate * dt
        while spawn_prob >= 1:
            spawn_prob -= 1
            self.game.spawn_enemy()
        x = random.random()
        if spawn_prob > x:
            self.game.spawn_enemy()


class Enemy:
    radius = 25
    color2 = 'red'
    color1 = 'green'
    max_hp = 100
    def __init__(self, game):
        self.game = game
        self.path:Path = self.game.path  # Stocke le chemin que l'ennemi doit suivre.
        self.path_len = self.path.length()
        # self.path_index = 0  # Indice du point actuel dans le chemin.
        self.dist = 0  # distance on the path
        self.pos:tuple = comp_to_tup(self.path.point(self.dist)) # Position initiale de l'ennemi (premier point du chemin).
        self.speed = 100  # Vitesse de déplacement par mise à jour.
        self.hp = self.max_hp
        self.damage_radius = 0

    def move(self, dt, path_points:list[tuple], path_precision:int):
        self.dist += self.speed * dt
        if self.dist <= self.path_len:
            rounded_dist = int(self.dist / path_precision)
            self.pos = path_points[rounded_dist]
            # self.pos = comp_to_tup(self.path.point(self.path.ilength(rounded_dist)))


    def take_damage(self, damage):
        self.hp -= damage
        self.damage_radius = self.radius * (1 - self.hp / self.max_hp)

    def draw(self, screen):
        # Dessine l'ennemi sur l'écran
        pygame.draw.circle(screen, self.color1, self.pos, self.radius)
        if self.damage_radius > 0:
            pygame.draw.circle(screen, self.color2, self.pos, self.damage_radius)
        pygame.draw.circle(screen, 'black', self.pos, self.radius, width=1)