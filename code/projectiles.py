import pygame

class Projectile:
    # La classe Projectile représente un projectile tiré par une tour
    # TODO: Ajouter les attributs nécessaires pour le projectile
    def __init__(self, pos, target):
        # Position actuelle du projectile (part de la tour)
        # target est l'ennemi visé (classe Enemy)
        pass
        
    # TODO: Ajouter la méthode pour déplacer le projectile
    def move(self):
        # Cette méthode se charge de déplacer le projectile vers sa cible
        # Si le projectile atteint la cible, il doit infliger des dégâts et être retiré de la liste
        # Sinon, il continue à se déplacer vers la cible
        pass
        
    # TODO: Modifier la méthode pour dessiner le projectile 
    def draw(self, win):
        pygame.draw.circle(win, RED, (int(self.pos[0]), int(self.pos[1])), 5)  # Représente un tir avec un petit cercle bleu