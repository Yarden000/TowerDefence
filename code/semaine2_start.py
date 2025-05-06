
# Importation des bibliothèques nécessaires
import pygame  # Bibliothèque principale pour la création de la fenêtre, la gestion des événements et des dessins.
import math    # Fournit des fonctions mathématiques comme hypot pour calculer des distances.
import random  # Permet d'introduire des comportements aléatoires dans le jeu si besoin.

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
GREY = (200,200,200)     # Utilisé pour le chemin

# Définition du nombre d'images par seconde
FPS = 60  # Permet de contrôler la fluidité de l'animation (60 images par seconde).

# Définition du chemin que suivent les ennemis
PATH = [(50, 50), (300, 50), (300, 250), (500, 250), (500, 150), (750, 150), (750, 500), (50, 500)]  
# Liste de points (x, y) par lesquels les ennemis doivent passer, modélise leur trajet.

#========================================================================================

# Définition de la classe Enemy (ennemi du jeu)
class Enemy:
    def __init__(self, path):
        self.path = path  # Stocke le chemin que l'ennemi doit suivre.
        self.path_index = 0  # Indice du point actuel dans le chemin.
        self.pos = list(self.path[0])  # Position initiale de l'ennemi (premier point du chemin).
        self.speed = 3  # Vitesse de déplacement par mise à jour.

    def move(self):
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
    
    def draw(self, win):
        # Dessine l'ennemi sur l'écran
        pygame.draw.circle(win, BLACK, self.pos,10)

#========================================================================================

# Classe Tower à compléter
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

#========================================================================================

# Classe Projectile à compléter
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
#========================================================================================

# Fonction principale contenant la boucle du jeu
def main():
    clock = pygame.time.Clock()  # Objet permettant de contrôler le framerate
    run = True  # Contrôle principal de la boucle de jeu
    
    NMI = Enemy(PATH)  # Crée une instance de l'ennemi avec le chemin défini

    while run:
        clock.tick(FPS)
        WIN.fill(WHITE)

        # Dessiner le chemin
        for i in range(len(PATH)-1):
            pygame.draw.line(WIN, GREY, PATH[i], PATH[i+1] , 3)
            
        # Dessiner et déplacer les ennemis
        NMI.move()
        NMI.draw(WIN)
        # TODO: Dessiner les tours
        
        # TODO: Dessiner les projectiles
        
        # Met à jour l'écran après tous les dessins
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # TODO: Ajouter une tour à la position de la souris
                pass

    pygame.quit()

if __name__ == "__main__":
    main()
