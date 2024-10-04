import pygame
import random
from collections import deque

res = width, height = 1202, 902

tile_size = 25

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
        self.in_path = False  # For solving visualization

    def draw_current_cell(self):
        x = self.x * self.maze.tile_size + self.maze.x_offset
        y = self.y * self.maze.tile_size + self.maze.y_offset
        pygame.draw.rect(sc, 'darkorange', (x, y, self.maze.tile_size, self.maze.tile_size))

    def draw(self):
        x = self.x * self.maze.tile_size + self.maze.x_offset
        y = self.y * self.maze.tile_size + self.maze.y_offset
        if self.in_path:
            pygame.draw.rect(sc, 'red', (x, y, self.maze.tile_size, self.maze.tile_size))
        elif self.visited:
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
        self.generation_complete = False
        self.solving = False
        self.solved = False
        self.solution_path = []
        self.visited_cells = []
        self.start_cell = self.grid_cells[0]
        self.end_cell = self.grid_cells[-1]
        self.algorithm = None

    def generate_maze(self):
        self.current_cell.visited = True
        next_cell = self.current_cell.check_neighbors()
        if next_cell:
            next_cell.visited = True
            self.stack.append(self.current_cell)
            remove_walls(self.current_cell, next_cell)
            self.current_cell = next_cell
        elif self.stack:
            self.current_cell = self.stack.pop()
        else:
            self.generation_complete = True

    def update(self):
        if not self.generation_complete:
            self.generate_maze()
        elif self.solving and not self.solved:
            self.solve_step()

    def draw(self):
        for cell in self.grid_cells:
            cell.draw()
        if not self.generation_complete:
            self.current_cell.draw_current_cell()

    def solve_maze(self, algorithm):
        self.algorithm = algorithm
        self.solving = True
        self.visited_cells = []
        self.solution_path = []
        if algorithm == 'dfs':
            self.stack = [self.start_cell]
        elif algorithm == 'bfs':
            self.queue = deque([self.start_cell])
        elif algorithm == '4o_algo':
            self.open_set = [self.start_cell]
        self.start_cell.in_path = True

    def solve_step(self):
        if self.algorithm == 'dfs':
            if self.stack:
                current_cell = self.stack.pop()
                self.visited_cells.append(current_cell)
                if current_cell == self.end_cell:
                    self.solved = True
                    return
                neighbors = self.get_neighbors(current_cell)
                for neighbor in neighbors:
                    if neighbor not in self.visited_cells and neighbor not in self.stack:
                        neighbor.in_path = True
                        self.stack.append(neighbor)
            else:
                self.solved = True  # No solution found

        elif self.algorithm == 'bfs':
            if self.queue:
                current_cell = self.queue.popleft()
                self.visited_cells.append(current_cell)
                if current_cell == self.end_cell:
                    self.solved = True
                    return
                neighbors = self.get_neighbors(current_cell)
                for neighbor in neighbors:
                    if neighbor not in self.visited_cells and neighbor not in self.queue:
                        neighbor.in_path = True
                        self.queue.append(neighbor)
            else:
                self.solved = True  # No solution found

        elif self.algorithm == '4o_algo':
            if self.open_set:
                # A* algorithm
                current_cell = min(self.open_set, key=lambda cell: cell.f)
                self.open_set.remove(current_cell)
                self.visited_cells.append(current_cell)
                if current_cell == self.end_cell:
                    self.reconstruct_path(current_cell)
                    self.solved = True
                    return
                neighbors = self.get_neighbors(current_cell)
                for neighbor in neighbors:
                    if neighbor in self.visited_cells:
                        continue
                    tentative_g = current_cell.g + 1
                    if neighbor not in self.open_set:
                        self.open_set.append(neighbor)
                    elif tentative_g >= neighbor.g:
                        continue
                    neighbor.came_from = current_cell
                    neighbor.g = tentative_g
                    neighbor.h = abs(neighbor.x - self.end_cell.x) + abs(neighbor.y - self.end_cell.y)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.in_path = True
            else:
                self.solved = True  # No solution found

    def get_neighbors(self, cell):
        neighbors = []
        x, y = cell.x, cell.y
        if not cell.walls['top']:
            neighbor = self.grid_cells[x + (y - 1) * self.cols]
            neighbors.append(neighbor)
        if not cell.walls['right']:
            neighbor = self.grid_cells[(x + 1) + y * self.cols]
            neighbors.append(neighbor)
        if not cell.walls['bottom']:
            neighbor = self.grid_cells[x + (y + 1) * self.cols]
            neighbors.append(neighbor)
        if not cell.walls['left']:
            neighbor = self.grid_cells[(x - 1) + y * self.cols]
            neighbors.append(neighbor)
        return neighbors

    def reconstruct_path(self, current):
        while hasattr(current, 'came_from'):
            current.in_path = True
            current = current.came_from

# Configuration for the maze
num_mazes_x = 1
num_mazes_y = 1
maze_width = width // num_mazes_x
maze_height = height // num_mazes_y
cols = maze_width // tile_size
rows = maze_height // tile_size

# Create maze instance
maze = Maze(0, 0, cols, rows, tile_size)

# Main loop
selected_algorithm = None
waiting_for_selection = True

while True:
    sc.fill(pygame.Color('darkslategray'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and waiting_for_selection:
            if event.key == pygame.K_d:
                selected_algorithm = 'dfs'
                maze.solve_maze('dfs')
                waiting_for_selection = False
            elif event.key == pygame.K_b:
                selected_algorithm = 'bfs'
                maze.solve_maze('bfs')
                waiting_for_selection = False
            elif event.key == pygame.K_f:
                selected_algorithm = '4o_algo'
                # Initialize variables for A* algorithm
                for cell in maze.grid_cells:
                    cell.g = float('inf')
                    cell.h = float('inf')
                    cell.f = float('inf')
                    cell.came_from = None
                maze.start_cell.g = 0
                maze.start_cell.h = abs(maze.start_cell.x - maze.end_cell.x) + abs(maze.start_cell.y - maze.end_cell.y)
                maze.start_cell.f = maze.start_cell.h
                maze.solve_maze('4o_algo')
                waiting_for_selection = False

    maze.update()
    maze.draw()

    if maze.generation_complete and not maze.solving and waiting_for_selection:
        # Display instructions
        font = pygame.font.SysFont(None, 36)
        text = font.render('Press D for DFS, B for BFS, F for 4o algo', True, pygame.Color('white'))
        sc.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)
