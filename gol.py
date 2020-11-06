import pygame
import math

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Game of Life")

#color def
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 255)
GREY = (128, 128, 128)

class Cell:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = BLACK
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_post(self):
        return self.row, self.col

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(0, rows):
        grid.append([])
        for j in range(0, rows):
            cell = Cell(i, j, gap, rows)
            grid[i].append(cell)

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(BLACK)

    for row in grid:
        for cell in row:
            cell.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def main(win, width):
    ROWS = 25
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            

    pygame.quit()

main(WIN, WIDTH)
        


