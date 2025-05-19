'''
helpull resources:
    svg: https://pypi.org/project/svgpathtools/ https://www.w3.org/TR/SVG/paths.html#PathLengthAttribute
'''
import time
import pygame  # Bibliothèque principale pour la création de la fenêtre, la gestion des événements et des dessins.
import math    # Fournit des fonctions mathématiques comme hypot pour calculer des distances.
import random  # Permet d'introduire des comportements aléatoires dans le jeu si besoin.
from svgpathtools import Path, Line, Arc, CubicBezier, QuadraticBezier
from settings import SCREEN_SIZE, display_path, path_points, tup_to_comp, Vec2, closest_to_point, dist, comp_to_tup


class TemporairyPath:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        


    


class MapMaker:

    def __init__(self):
        # temporary
        self.precision = 1
        self.path = Path()
        vertecies = [(0, 150), (500, 150), (500, 300), (800, 300), (800, 450)]
        '''
        for i in range(len(vertecies) - 1):
            self.path += Path(Line(tup_to_comp(vertecies[i]), tup_to_comp(vertecies[i+1])))
        self.path += Path(CubicBezier(800 + 450j, 500 - 200j, 800 + 800j, 450j))
        '''
        '''
        self.path = Path()
        self.path += Path(QuadraticBezier(200 + 100j, 200j, 200 + 400j))
        self.path += Path(CubicBezier(200 + 400j, 600j, 800 + 500j, 300 + 600j))
        '''
        #self.points = path_points(self.path, self.precision)
        self.exit = False  # if true means you want to close the program => no need to run the game in the main file

        self.special_point_rad = 20

    def run(self):
        
        temporairy_precision = 20

        pygame.init()

        SCREEN = pygame.display.set_mode(SCREEN_SIZE)  # Crée une fenêtre pygame de dimensions spécifiées.
        pygame.display.set_caption("Tower Defense - MapMaker")  # Donne un titre à la fenêtre.

        FPS = 60  # Permet de contrôler la fluidité de l'animation (60 images par seconde).

        clock = pygame.time.Clock()  # Objet permettant de contrôler le framerate
        run = True  # Contrôle principal de la boucle de jeu
        
        finished = False
        drawing = True

        '''path info'''
        start = None
        path_being_drawn = None
        paths:list[dict] = []
        # TODO for now only lines work
        start_pos: None|tuple = None
        end_pos = None
        # (if line just start_point and end_point needed)
        # if Arc

        type: None|Line|Arc|QuadraticBezier|CubicBezier = None
        edditing_path:int = 0

        original_mouse_pressed = (False, False, False)

        point_selected = None
        while not finished:

            clock.tick(FPS)
            SCREEN.fill('white')

            events = pygame.event.get()
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if mouse_pressed == original_mouse_pressed:
                mouse_pressed = (False, False, False)
            else:
                original_mouse_pressed = mouse_pressed
            keys = pygame.key.get_pressed()
            

            
            
            if drawing:
                
                if start:
                    if path_being_drawn:
                        if tup_to_comp(mouse_pos) != path_being_drawn.start:
                            path_being_drawn.end = tup_to_comp(mouse_pos)
                    else:
                        if paths:
                            path_being_drawn = Line(paths[-1]['path'].end, tup_to_comp(mouse_pos + Vec2(0, 1)))
                        else:
                            Line(tup_to_comp(start), tup_to_comp(start + Vec2(0, 1)))
                else:
                    path_being_drawn = None
                if mouse_pressed[0]:
                    if not start:
                        start = mouse_pos
                        path_being_drawn = Line(tup_to_comp(start), tup_to_comp(start + Vec2(0, 1)))
                        '''
                        elif not paths:
                            print('first path')
                            path = Line(tup_to_comp(start), tup_to_comp(mouse_pos))
                            paths.append({type: Line, 'start': start, 'end': mouse_pos, 'path': path, 'points': path_points(path, temporairy_precision)})
                            #path = Line(tup_to_comp(start), tup_to_comp(mouse_pos))
                        '''
                    else:
                        path_len = len(paths)

                        if paths:
                            paths.append({'type': Line, 'path': path_being_drawn, 'points': path_points(path_being_drawn, temporairy_precision)})
                            path_being_drawn = Line(paths[-1]['path'].end, tup_to_comp(mouse_pos + Vec2(0, 1)))

                        else:
                            paths.append({'type': Line, 'path': path_being_drawn, 'points': path_points(path_being_drawn, temporairy_precision)})
                            path_being_drawn = Line(paths[-1]['path'].end, tup_to_comp(mouse_pos + Vec2(0, 1)))



                if paths:
                    for event in events:
                        if event.type == pygame.KEYDOWN:
                            if pygame.K_p == event.key:
                                drawing = not drawing
                                path_being_drawn = None
                            if drawing and pygame.K_d == event.key:
                                paths.pop()
                                if paths:
                                    path_being_drawn = Line(paths[-1]['path'].end, tup_to_comp(mouse_pos + Vec2(0, 1)))
                                else:
                                    start = None

            # edditing existing paths
            else:
                
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        prev_eddited_path = edditing_path

                        if pygame.K_DOWN == event.key:
                            edditing_path -= 1
                            point_selected = None

                        if pygame.K_UP == event.key:
                            edditing_path += 1
                            point_selected = None

                        if edditing_path < 0:
                            edditing_path = len(paths) - 1

                        if edditing_path >= len(paths):
                            edditing_path = 0

                        if edditing_path != prev_eddited_path:
                            paths[prev_eddited_path]['points'] = path_points(paths[prev_eddited_path]['path'], temporairy_precision)


                
                if mouse_pressed[0]:
                    # TODO needs implementation for other path types
                    p = paths[edditing_path]

                    if not point_selected:

                        if p['type'] == Line:
                            if dist(mouse_pos, comp_to_tup(p['path'].start)) > dist(mouse_pos, comp_to_tup(p['path'].end)) and dist(mouse_pos, comp_to_tup(p['path'].end)) < self.special_point_rad:
                                point_selected = 'end'
                                
                            elif dist(mouse_pos, comp_to_tup(p['path'].end)) > dist(mouse_pos, comp_to_tup(p['path'].start)) and dist(mouse_pos, comp_to_tup(p['path'].start)) < self.special_point_rad:
                                point_selected = 'start'
                                

                if mouse_pressed[2]:
                    point_selected = None
                print(point_selected)

                if point_selected == 'start':
                    p['path'].start = tup_to_comp(mouse_pos)

                if point_selected == 'end':
                    p['path'].end = tup_to_comp(mouse_pos)

                



                # type of path selected  TODO not yet implemented for paths other than line
                if keys[pygame.K_1]:
                    type = Line
                if keys[pygame.K_2]:
                    type = Arc
                if keys[pygame.K_3]:
                    type = QuadraticBezier
                if keys[pygame.K_4]:
                    type = CubicBezier

            if paths:
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if pygame.K_0 == event.key:
                            drawing = not drawing
                            path_being_drawn = None
                            point_selected = None
                            paths[edditing_path]['points'] = path_points(paths[edditing_path]['path'], temporairy_precision)


            
            # displays
            '''
            start_time = time.time()
            points = path_points(self.path, temporairy_precision)
            print('time = ', time.time() - start_time)
            '''
            if drawing:
                for path_ in paths:
                    display_path(path_['points'], SCREEN, color = 'black', thikness = temporairy_precision)
                if path_being_drawn:
                    display_path(path_points(path_being_drawn, temporairy_precision), SCREEN, color = 'black', thikness = temporairy_precision)
            else:
                for num, path_ in enumerate(paths):
                    if num != edditing_path:
                        display_path(path_['points'], SCREEN, color = 'black', thikness = temporairy_precision)
                    
                path_being_eddited = paths[edditing_path]
                display_path(path_points(path_being_eddited['path'], temporairy_precision), SCREEN, color = 'green', thikness = temporairy_precision)
                pygame.draw.circle(SCREEN, 'red', comp_to_tup(path_being_eddited['path'].start), self.special_point_rad)
                pygame.draw.circle(SCREEN, 'red', comp_to_tup(path_being_eddited['path'].end), self.special_point_rad)

            # Met à jour l'écran après tous les dessins
            pygame.display.update()

            for event in events:
                if event.type == pygame.QUIT:
                    finished = True
                    self.exit = True

            if keys[pygame.K_q]:
                finished = True

        pygame.quit()
        for path in paths:
            self.path += Path(path['path'])
        self.points = path_points(self.path, self.precision)