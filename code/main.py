import pygame  # Bibliothèque principale pour la création de la fenêtre, la gestion des événements et des dessins.
import math    # Fournit des fonctions mathématiques comme hypot pour calculer des distances.
import random  # Permet d'introduire des comportements aléatoires dans le jeu si besoin.
from settings import SCREEN_SIZE, display_path, cc_collision
from mapmaker import MapMaker
from enemies import Enemy,Enemy_spawner
from tower import Tower
from projectiles import Projectile

class Game:
    
    def __init__(self, map_maker: MapMaker):
        self.displayer = Displayer(self)
        self.enemy_spawner = Enemy_spawner(self)
        self.map_maker = map_maker
        self.path = self.map_maker.path
        self.path_len = self.path.length()
        self.path_points = self.map_maker.points
        self.path_precision = self.map_maker.precision

        self.enemies: list[Enemy] = []
        self.towers:list[Tower] = []
        self.projectiles:list[Projectile] = []

        self.player_health = 100
        self.player_money = 100000

    def spawn_enemy(self):
        self.enemies.append(Enemy(self))

    def move_enemies(self, dt):
        for enemy in self.enemies:
            enemy.move(dt, self.path_points, self.path_precision)

    def move_projectiles(self, dt):
        for projectile in self.projectiles:
            projectile.move(dt)

    def shoot_towers(self, dt):
        for tower in self.towers:
            tower.shoot(dt)

    def add_tower(self, new_tower:Tower):
        for tower in self.towers:
            if cc_collision(new_tower.pos, new_tower.radius, tower.pos, tower.radius) or new_tower.cost > self.player_money:
                return False
        self.towers.append(new_tower)
        self.player_money -= new_tower.cost

    def add_projectile(self, projectile):
        self.projectiles.append(projectile)


    def run(self):
        pygame.init()
        dt = 0
        FPS = 120  # Permet de contrôler la fluidité de l'animation (60 images par seconde).

        clock = pygame.time.Clock()  # Objet permettant de contrôler le framerate
        run = True  # Contrôle principal de la boucle de jeu
        
        # the acion curently doing
        action = None
        

        self.pre_tower = None
        while run:
            clock.tick(FPS)
            dt = clock.get_time() / 1000

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()

            # actions
            if action != None and keys[pygame.K_0]:
                action = None
                print('action = ' + str(action))
                self.pre_tower = None

            elif action == None and keys[pygame.K_1]:
                action = 'placing_tower'
                print('action = ' + str(action))
                self.pre_tower = Tower(self, mouse_pos)

            # place towers
            elif action == 'placing_tower':
                if mouse_pressed[0]:
                    print('placing')
                    print('--------')
                    self.add_tower(self.pre_tower)
                    self.pre_tower = Tower(self, mouse_pos)
                
                self.pre_tower.move_to(mouse_pos)
            # spawn enemies
            self.enemy_spawner.spawn(dt)
            
            # move enemies
            self.move_projectiles(dt)

            # projectiles hit enemies
            # TODO: needs optimisation: grid
            for projectile in self.projectiles:
                for enemy in self.enemies:
                    if enemy not in projectile.enemies_hit:
                        if cc_collision(projectile.pos, projectile.radius, enemy.pos, enemy.radius):
                            enemy.take_damage(5)
                            projectile.enemies_hit.append(enemy)
            # kill enemies
            enemy_list_copy = self.enemies.copy()
            for enemy in self.enemies:
                if enemy.hp <= 0:
                    enemy_list_copy.remove(enemy)
                    self.player_money += 1
            self.enemies = enemy_list_copy
                    
            self.move_enemies(dt)

            # enemies at end
            enemy_list_copy = self.enemies.copy()
            for enemy in self.enemies:
                if enemy.dist >= self.path_len:
                    enemy_list_copy.remove(enemy)
                    self.player_health -= 1
            self.enemies = enemy_list_copy

            self.shoot_towers(dt)

            self.displayer.display(dt) 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
 
        pygame.quit()


class Displayer:

    def __init__(self, game):
        self.game:Game = game
        self.screen = pygame.display.set_mode(SCREEN_SIZE)  # Crée une fenêtre pygame de dimensions spécifiées.
        self.displaying_pretower = False

    def display_enemies(self, ):
        for enemie in self.game.enemies:
            enemie.draw(self.screen)

    def display_towers(self):
        for tower in self.game.towers:
            tower.draw(self.screen)

    def display_projectiles(self):
        for projectile in self.game.projectiles:
            projectile.draw(self.screen)

    def display_pre_tower(self):
        if self.game.pre_tower:
            self.game.pre_tower.draw(self.screen, color = 'red')

    def display(self, dt):
        self.screen.fill('white')
        pygame.display.set_caption(
            "Tower Defense | dt = " + str(dt)
            + " | hp = " + str(self.game.player_health)
            + " | money = " + str(self.game.player_money)
            )  # Donne un titre à la fenêtre.
        
        
        display_path(self.game.path_points, self.screen, thikness=1)
        self.display_enemies()
        self.display_towers()
        self.display_projectiles()
        self.display_pre_tower()
        

        # Met à jour l'écran après tous les dessins
        pygame.display.update()

if __name__ == "__main__":
    print('starting ...')
    map_maker = MapMaker()
    # map_maker.run()
    game = Game(map_maker)
    if not map_maker.exit:
        game.run()