import pygame
import math

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

#color def
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY = (128, 128, 128)

class Cell:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = BLACK
        self.neighbors = 0
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def is_alive(self):
        return self.color == GREEN

    def is_dead(self):
        return self.color == BLACK

    def make_alive(self):
        self.color = GREEN

    def make_dead(self):
        self.color = BLACK 

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = 0
        
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_dead(): #down
            self.neighbors += 1

        if self.row > 0 and not grid[self.row - 1][self.col].is_dead(): #up
            self.neighbors += 1
        
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_dead(): #right
            self.neighbors += 1

        if self.col > 0 and not grid[self.row][self.col - 1].is_dead(): #left
            self.neighbors += 1

        if self.row > 0 and self.col < self.total_rows - 1 and not grid[self.row - 1][self.col + 1].is_dead(): #top_r
            self.neighbors += 1

        if self.row > 0 and self.col > 0 and not grid[self.row - 1][self.col - 1].is_dead(): #top_l
            self.neighbors += 1

        if self.row < self.total_rows - 1 and self.col < self.total_rows - 1 and not grid[self.row + 1][self.col + 1].is_dead(): #bot_r
            self.neighbors += 1

        if self.row < self.total_rows - 1 and self.col > 0 and not grid[self.row + 1][self.col - 1].is_dead(): #bot_l
            self.neighbors += 1
            
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

def life(draw, grid):
    for row in grid:
        for cell in row:
            if cell.neighbors < 2 or cell.neighbors > 3:
                cell.make_dead()
            elif cell.neighbors == 3:
                cell.make_alive()

    draw()

    return False

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    run = True
    started = False

    while run:
        clock.tick(60)

        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if started:
                for row in grid:
                    for cell in row:
                        cell.update_neighbors(grid)     

                life(lambda : draw(win, grid, ROWS, width), grid)
            
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]

                print("Make alive", row, col)

                cell.make_alive()

            elif pygame.mouse.get_pressed()[2]: 
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                cell = grid[row][col]

                print("Make dead", row, col)
            
                cell.make_dead()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    started = not started

                if event.key == pygame.K_c:
                    grid = make_grid(ROWS, width)

    pygame.quit()

main(WIN, WIDTH)
        


