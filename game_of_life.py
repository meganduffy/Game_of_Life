import random
import sys

import pygame

from colours import dark_blue, green, black

def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))

def draw_cells():
    for (x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)

def get_neighbours((x, y)):
    positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                 (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
    return [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]

def evolve():
    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours < 2 or live_neighbours > 3:
                cells[position] = False
        elif live_neighbours == 3:
                cells[position] = True


def make_pattern():
    pattern = ""
    pattern_string = raw_input("Enter the string you want to convert to cells: ")
    for c, x in enumerate(pattern_string):
        pattern += str(c) + "\n"
    return pattern

pattern = make_pattern()

def points_of_string(pattern):
    pattern_lines = pattern.split("\n")
    return {(row_number, col_number) for row_number, row in enumerate(pattern_lines) for col_number, column in enumerate(pattern_lines)}


def get_cells():
    cells = points_of_string(pattern)
    board = {(c, r): (c,r) in cells for c in range(columns) for r in range(rows)}
    return board

pygame.init()


columns, rows = 50, 50
cells = get_cells()
clock = pygame.time.Clock()
speed = 1

cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)


while True:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if speed > 1 and event.key == pygame.K_LEFT:
                speed -= 1
            if event.key == pygame.K_RIGHT:
                speed += 1

    draw_cells()
    evolve()
    draw_grid()

    pygame.display.update()