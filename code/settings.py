import pygame
from svgpathtools import Path, Line, Arc, CubicBezier, QuadraticBezier


comp_to_tup = lambda c: (c.real, c.imag)
tup_to_comp = lambda t: t[0] + t[1] * 1j

def display_path(points:list[tuple], screen, color = 'green', thikness = 5) -> None:
    positions = points
    if thikness > 5:
        thikness = 5
    for pos in positions:
        pygame.draw.circle(screen, color, pos, thikness)

def path_points(path:Path, precision:int) -> list[tuple]:
    path_len = path.length()
    n = int(path_len / precision) + 1  # number of points
    positions = [comp_to_tup(path.point(path.ilength(path_len * i / n))) for i in range(n)]
    return positions

Vec2 = pygame.Vector2
SCREEN_SIZE = 1200, 600  # Modélise l'espace de jeu où se déplaceront ennemis et tours.