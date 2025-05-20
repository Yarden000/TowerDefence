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



        


    


class MapMaker:

    def __init__(self):
        # temporary
        self.precision = 1
        self.path = Path()

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
        paths:list[dict[dict]] = []

        edditing_path:int = 0  # the position of the subpath being eddited

        original_mouse_pressed = (False, False, False)  # helps not to count double if mouse button is kept pressed

        point_selected = None
        type_ = None
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
                            path_type = paths[-1]['type chosen']
                            path_being_drawn = Line(paths[-1][path_type]['path'].end, tup_to_comp(mouse_pos + Vec2(0, 1)))
                        else:
                            Line(tup_to_comp(start), tup_to_comp(start + Vec2(0, 1)))
                else:
                    path_being_drawn = None
                if mouse_pressed[0]:
                    if not start:
                        start = mouse_pos
                        path_being_drawn = Line(tup_to_comp(start), tup_to_comp(start + Vec2(0, 1)))

                    else:

                        if paths:
                            paths.append({Line: {'path': path_being_drawn, 'points': path_points(path_being_drawn, temporairy_precision)}, 'type chosen': Line})
                            path_type = paths[-1]['type chosen']
                            path_being_drawn = Line(paths[-1][path_type]['path'].end, tup_to_comp(mouse_pos + Vec2(0, 1)))

                        else:
                            paths.append({Line: {'path': path_being_drawn, 'points': path_points(path_being_drawn, temporairy_precision)}, 'type chosen': Line})
                            path_type = paths[-1]['type chosen']
                            path_being_drawn = Line(paths[-1][path_type]['path'].end, tup_to_comp(mouse_pos + Vec2(0, 1)))



                if paths:
                    for event in events:
                        if event.type == pygame.KEYDOWN:
                            if drawing and pygame.K_d == event.key:
                                paths.pop()
                                if paths:
                                    path_type = paths[-1]['type chosen']
                                    path_being_drawn = Line(paths[-1][path_type]['path'].end, tup_to_comp(mouse_pos + Vec2(0, 1)))
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
                            path_type = paths[prev_eddited_path]['type chosen']
                            paths[prev_eddited_path][path_type]['points'] = path_points(paths[prev_eddited_path][path_type]['path'], temporairy_precision)
                            type_ = paths[edditing_path]['type chosen']

                        if pygame.K_1 == event.key:
                            type_ = Line
                        elif pygame.K_2 == event.key:
                            type_ = QuadraticBezier
                        elif pygame.K_3 == event.key:
                            type_ = CubicBezier
                        
                        
                        

                        if type_ != paths[edditing_path]['type chosen'] and type_ != None:

                            if not (type_ in paths[edditing_path]):

                                if type_ == QuadraticBezier:
                                    s = paths[edditing_path][Line]['path'].start
                                    e = paths[edditing_path][Line]['path'].end
                                    c_in_vec = (Vec2(comp_to_tup(s)) + Vec2(comp_to_tup(e))) * 0.5 + Vec2(10, 10)
                                    c = tup_to_comp(tuple(c_in_vec))
                                    path__ = QuadraticBezier(s, c, e)
                                    paths[edditing_path][QuadraticBezier] = {'path': path__, 'points': path_points(path__, temporairy_precision)}      

                                elif type_ == CubicBezier:
                                    s = paths[edditing_path][Line]['path'].start
                                    e = paths[edditing_path][Line]['path'].end
                                    c1_in_vec = (Vec2(comp_to_tup(s)) + Vec2(comp_to_tup(e))) * 0.5 + Vec2(20, 20)
                                    c1 = tup_to_comp(tuple(c1_in_vec))
                                    c2_in_vec = (Vec2(comp_to_tup(s)) + Vec2(comp_to_tup(e))) * 0.5 - Vec2(20, 20)
                                    c2 = tup_to_comp(tuple(c2_in_vec))
                                    path__ = CubicBezier(s, c1, c2, e)
                                    paths[edditing_path][CubicBezier] = {'path': path__, 'points': path_points(path__, temporairy_precision)}      


                                else:
                                    raise ValueError('path type not yet implemented')
                            
                            paths[edditing_path]['type chosen'] = type_
                            print(paths[edditing_path]['type chosen'])



                
                if mouse_pressed[0]:
                    # TODO needs implementation for other path types
                    path_type = paths[edditing_path]['type chosen']
                    p = paths[edditing_path][path_type]

                    if not point_selected:

                        if path_type == Line:
                            if dist(mouse_pos, comp_to_tup(p['path'].start)) > dist(mouse_pos, comp_to_tup(p['path'].end)) and dist(mouse_pos, comp_to_tup(p['path'].end)) < self.special_point_rad:
                                point_selected = 'end'
                                
                            elif dist(mouse_pos, comp_to_tup(p['path'].end)) > dist(mouse_pos, comp_to_tup(p['path'].start)) and dist(mouse_pos, comp_to_tup(p['path'].start)) < self.special_point_rad:
                                point_selected = 'start'

                        if path_type == QuadraticBezier:
                            important_points = [comp_to_tup(p['path'].start), comp_to_tup(p['path'].control), comp_to_tup(p['path'].end)]
                            closest_to_point_dist = closest_to_point(mouse_pos, important_points, want_dist=True)[1]

                            if closest_to_point_dist < self.special_point_rad:
                                if closest_to_point_dist == dist(mouse_pos, comp_to_tup(p['path'].start)):
                                    point_selected = 'start'
                                if closest_to_point_dist == dist(mouse_pos, comp_to_tup(p['path'].control)):
                                    point_selected = 'control'
                                if closest_to_point_dist == dist(mouse_pos, comp_to_tup(p['path'].end)):
                                    point_selected = 'end'

                        if path_type == CubicBezier:
                            important_points = [comp_to_tup(p['path'].start), comp_to_tup(p['path'].control1), comp_to_tup(p['path'].control2), comp_to_tup(p['path'].end)]
                            closest_to_point_dist = closest_to_point(mouse_pos, important_points, want_dist=True)[1]

                            if closest_to_point_dist < self.special_point_rad:
                                if closest_to_point_dist == dist(mouse_pos, comp_to_tup(p['path'].start)):
                                    point_selected = 'start'
                                if closest_to_point_dist == dist(mouse_pos, comp_to_tup(p['path'].control1)):
                                    point_selected = 'control1'
                                if closest_to_point_dist == dist(mouse_pos, comp_to_tup(p['path'].control2)):
                                    point_selected = 'control2'
                                if closest_to_point_dist == dist(mouse_pos, comp_to_tup(p['path'].end)):
                                    point_selected = 'end'

                if mouse_pressed[2]:
                    point_selected = None

                if point_selected == 'start':
                    p['path'].start = tup_to_comp(mouse_pos)

                if point_selected == 'end':
                    p['path'].end = tup_to_comp(mouse_pos)

                if point_selected == 'control':
                    p['path'].control = tup_to_comp(mouse_pos)
                
                if point_selected == 'control1':
                    p['path'].control1 = tup_to_comp(mouse_pos)

                if point_selected == 'control2':
                    p['path'].control2 = tup_to_comp(mouse_pos)

                
            # switches from drawing to editing
            if paths:
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if pygame.K_0 == event.key:
                            drawing = not drawing
                            path_being_drawn = None
                            point_selected = None
                            path_type = paths[edditing_path]['type chosen']
                            paths[edditing_path][path_type]['points'] = path_points(paths[edditing_path][path_type]['path'], temporairy_precision)


            
            # displays
            if drawing:
                for path_ in paths:
                    path_type = path_['type chosen']
                    display_path(path_[path_type]['points'], SCREEN, color = 'black', thikness = temporairy_precision)
                if path_being_drawn:
                    display_path(path_points(path_being_drawn, temporairy_precision), SCREEN, color = 'black', thikness = temporairy_precision)
            else:
                for num, path_ in enumerate(paths):
                    if num != edditing_path:
                        path_type = path_['type chosen']
                        display_path(path_[path_type]['points'], SCREEN, color = 'black', thikness = temporairy_precision)
                    
                path_type = paths[edditing_path]['type chosen']
                path_being_eddited = paths[edditing_path][path_type]
                display_path(path_points(path_being_eddited['path'], temporairy_precision), SCREEN, color = 'green', thikness = temporairy_precision)
                
                pygame.draw.circle(SCREEN, 'red', comp_to_tup(path_being_eddited['path'].start), self.special_point_rad)
                pygame.draw.circle(SCREEN, 'red', comp_to_tup(path_being_eddited['path'].end), self.special_point_rad)
                if path_type == QuadraticBezier:
                    pygame.draw.circle(SCREEN, 'red', comp_to_tup(path_being_eddited['path'].control), self.special_point_rad)

                if path_type == CubicBezier:
                    pygame.draw.circle(SCREEN, 'red', comp_to_tup(path_being_eddited['path'].control1), self.special_point_rad)
                    pygame.draw.circle(SCREEN, 'red', comp_to_tup(path_being_eddited['path'].control2), self.special_point_rad)



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
            path_type = path['type chosen']
            self.path += Path(path[path_type]['path'])
        self.points = path_points(self.path, self.precision)