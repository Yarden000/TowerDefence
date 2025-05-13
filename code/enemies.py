import math
from svgpathtools import Path, Line, Arc, CubicBezier, QuadraticBezier
import pygame
from settings import comp_to_tup


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
        '''
        # Permet à l'ennemi de se déplacer vers le prochain point du chemin
        if self.path_index < len(self.path) - 1: # Si l'ennemi n'est pas au dernier point
            # Calculer la position cible
            target = self.path[self.path_index + 1] # Prochain point du chemin
        else:
            # Si l'ennemi est au dernier point, il ne se déplace pas
            return True # Signale que l'ennemi est arrivé (il faudra faire une action)
        
        # Calculer le vecteur de direction vers la cible
        dir_vector = ( target[0] - self.pos[0], target[1] - self.pos[1] )
        # Calculer la distance entre la position actuelle et la cible
        distance = math.hypot(*dir_vector) #*dir_vector est équivalent à dir_vector[0], dir_vector[1], etc...
        
        
        # Si l'ennemi est proche du prochain point du chemin, il se déplace sur ce point
        if distance < self.speed:
            self.pos = list(target) # Met à jour la position exacte
            self.path_index += 1 # Passe au prochain point
        # Sinon, il se déplace dans la direction de la cible
        else:
            # Calculer le vecteur de direction normalisé
            dir_norm = (dir_vector[0]/distance, dir_vector[1]/distance)
            #Le vecteur de direction normalisé est multiplié par la vitesse pour obtenir le déplacement
            #Ajouter le déplacement à la position actuelle pour obtenir la nouvelle position
            self.pos[0] += dir_norm[0] * self.speed 
            self.pos[1] += dir_norm[1] * self.speed
        return False # Ennemi en mouvement
        '''
        self.dist += self.speed * dt
        if self.dist <= self.path_len:
            rounded_dist = int(self.dist / path_precision)
            self.pos = comp_to_tup(self.path.point(self.path.ilength(rounded_dist)))
        else:
            return True


    def draw(self, screen):
        # Dessine l'ennemi sur l'écran
        pygame.draw.circle(screen, self.color, self.pos, 10)