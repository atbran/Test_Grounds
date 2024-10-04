import pygame
import random

res = width, height = 1202, 902

tile_size = 50

pygame.init()
sc = pygame.display.set_mode(res)
clock = pygame.time.Clock()

def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False

class Cell:
    def __init__(self, x, y, maze):
        self.x = x
        self.y = y
        self.maze = maze
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.visited = False

    def draw_current_cell(self):
        x = self.x * self.maze.tile_size + self.maze.x_offset
        y = self.y * self.maze.tile_size + self.maze.y_offset
        pygame.draw.rect(sc, 'darkorange', (x, y, self.maze.tile_size, self.maze.tile_size))

    def draw(self):
        x = self.x * self.maze.tile_size + self.maze.x_offset
        y = self.y * self.maze.tile_size + self.maze.y_offset
        if self.visited:
            pygame.draw.rect(sc, 'black', (x, y, self.maze.tile_size, self.maze.tile_size))

        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color('darkblue'), (x, y), (x + self.maze.tile_size, y), 2)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color('darkblue'), (x + self.maze.tile_size, y), (x + self.maze.tile_size, y + self.maze.tile_size), 2)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color('darkblue'), (x + self.maze.tile_size, y + self.maze.tile_size), (x, y + self.maze.tile_size), 2)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color('darkblue'), (x, y + self.maze.tile_size), (x, y), 2)

    def check_cell(self, x, y):
        if x < 0 or x > self.maze.cols - 1 or y < 0 or y > self.maze.rows - 1:
            return None
        return self.maze.grid_cells[x + y * self.maze.cols]

    def check_neighbors(self):
        neighbors = []
        top = self.check_cell(self.x, self.y - 1)
        right = self.check_cell(self.x + 1, self.y)
        bottom = self.check_cell(self.x, self.y + 1)
        left = self.check_cell(self.x - 1, self.y)

        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        return random.choice(neighbors) if neighbors else None

class Maze:
    def __init__(self, x_offset, y_offset, cols, rows, tile_size):
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.cols = cols
        self.rows = rows
        self.tile_size = tile_size
        self.grid_cells = [Cell(col, row, self) for row in range(self.rows) for col in range(self.cols)]
        self.current_cell = self.grid_cells[0]
        self.stack = []

    def update(self):
        self.current_cell.visited = True
        next_cell = self.current_cell.check_neighbors()
        if next_cell:
            next_cell.visited = True
            self.stack.append(self.current_cell)
            remove_walls(self.current_cell, next_cell)
            self.current_cell = next_cell
        elif self.stack:
            self.current_cell = self.stack.pop()

    def draw(self):
        for cell in self.grid_cells:
            cell.draw()
        self.current_cell.draw_current_cell()

# Configuration for multiple mazes
num_mazes_x = 2
num_mazes_y =
maze_width = width // num_mazes_x
maze_height = height // num_mazes_y
cols = maze_width // tile_size
rows = maze_height // tile_size

# Create multiple maze instances
mazes = []
for i in range(num_mazes_y):
    for j in range(num_mazes_x):
        x_offset = j * maze_width
        y_offset = i * maze_height
        mazes.append(Maze(x_offset, y_offset, cols, rows, tile_size))

# Main loop
while True:
    sc.fill(pygame.Color('darkslategray'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for maze in mazes:
        maze.update()
        maze.draw()

    pygame.display.flip()
    clock.tick(120)
