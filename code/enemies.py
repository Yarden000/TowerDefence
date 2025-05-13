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
    def __init__(self, path:Path):
        self.path = path  # Stocke le chemin que l'ennemi doit suivre.
        self.path_len = self.path.length()
        # self.path_index = 0  # Indice du point actuel dans le chemin.
        self.dist = 0  # distance on the path
        self.pos:tuple = comp_to_tup(self.path.point(self.dist)) # Position initiale de l'ennemi (premier point du chemin).
        self.speed = 100  # Vitesse de déplacement par mise à jour.
        self.color = 'red'

    def move(self, dt, path_points:list[tuple], path_precision:int):
        self.dist += self.speed * dt
        if self.dist <= self.path_len:
            rounded_dist = int(self.dist / path_precision)
            self.pos = path_points[rounded_dist]
            # self.pos = comp_to_tup(self.path.point(self.path.ilength(rounded_dist)))
        else:
            return True


    def draw(self, screen):
        # Dessine l'ennemi sur l'écran
        pygame.draw.circle(screen, self.color, self.pos, 10)