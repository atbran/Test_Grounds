import pygame
import random
from collections import deque

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
        self.in_path = False  # For exploration visualization
        self.is_solution = False  # For final solution path visualization
        self.g = float('inf')  # Cost so far
        self.h = float('inf')  # Heuristic
        self.f = float('inf')  # Total cost
        self.came_from = None  # Parent cell in path

    def draw_current_cell(self):
        x = self.x * self.maze.tile_size + self.maze.x_offset
        y = self.y * self.maze.tile_size + self.maze.y_offset
        pygame.draw.rect(sc, 'darkorange', (x, y, self.maze.tile_size, self.maze.tile_size))

    def draw(self):
        x = self.x * self.maze.tile_size + self.maze.x_offset
        y = self.y * self.maze.tile_size + self.maze.y_offset
        if self.is_solution:
            pygame.draw.rect(sc, 'yellow', (x, y, self.maze.tile_size, self.maze.tile_size))
        elif self.in_path:
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
        self.solved = False
        self.visited_cells = []
        self.solution_path = []
        for cell in self.grid_cells:
            cell.in_path = False
            cell.is_solution = False
            cell.visited = False
            cell.g = float('inf')
            cell.h = float('inf')
            cell.f = float('inf')
            cell.came_from = None
        if algorithm == 'dfs':
            self.stack = [self.start_cell]
        elif algorithm == 'bfs':
            self.queue = deque([self.start_cell])
        elif algorithm == '4o_algo':
            self.open_set = [self.start_cell]
            self.start_cell.g = 0
            self.start_cell.h = abs(self.start_cell.x - self.end_cell.x) + abs(self.start_cell.y - self.end_cell.y)
            self.start_cell.f = self.start_cell.g + self.start_cell.h
        elif algorithm == 'gbfs':
            self.open_set = [self.start_cell]
            self.start_cell.h = abs(self.start_cell.x - self.end_cell.x) + abs(self.start_cell.y - self.end_cell.y)
            self.start_cell.f = self.start_cell.h
        elif algorithm == 'dijkstra':
            self.open_set = [self.start_cell]
            self.start_cell.g = 0
            self.start_cell.f = self.start_cell.g
        elif algorithm == 'random':
            self.current_cell = self.start_cell
        self.start_cell.in_path = True

    def solve_step(self):
        if self.algorithm == 'dfs':
            if self.stack:
                current_cell = self.stack.pop()
                current_cell.visited = True
                if current_cell == self.end_cell:
                    self.reconstruct_path(current_cell)
                    self.solved = True
                    return
                neighbors = self.get_neighbors(current_cell)
                for neighbor in neighbors:
                    if not neighbor.visited and neighbor not in self.stack:
                        neighbor.came_from = current_cell
                        neighbor.in_path = True
                        self.stack.append(neighbor)
            else:
                self.solved = True  # No solution found

        elif self.algorithm == 'bfs':
            if self.queue:
                current_cell = self.queue.popleft()
                current_cell.visited = True
                if current_cell == self.end_cell:
                    self.reconstruct_path(current_cell)
                    self.solved = True
                    return
                neighbors = self.get_neighbors(current_cell)
                for neighbor in neighbors:
                    if not neighbor.visited and neighbor not in self.queue:
                        neighbor.came_from = current_cell
                        neighbor.in_path = True
                        self.queue.append(neighbor)
            else:
                self.solved = True  # No solution found

        elif self.algorithm == '4o_algo':
            if self.open_set:
                # A* algorithm
                current_cell = min(self.open_set, key=lambda cell: cell.f)
                self.open_set.remove(current_cell)
                current_cell.visited = True
                if current_cell == self.end_cell:
                    self.reconstruct_path(current_cell)
                    self.solved = True
                    return
                neighbors = self.get_neighbors(current_cell)
                for neighbor in neighbors:
                    if neighbor.visited:
                        continue
                    tentative_g = current_cell.g + 1
                    if tentative_g < neighbor.g:
                        neighbor.came_from = current_cell
                        neighbor.g = tentative_g
                        neighbor.h = abs(neighbor.x - self.end_cell.x) + abs(neighbor.y - self.end_cell.y)
                        neighbor.f = neighbor.g + neighbor.h
                        if neighbor not in self.open_set:
                            neighbor.in_path = True
                            self.open_set.append(neighbor)
            else:
                self.solved = True  # No solution found

        elif self.algorithm == 'gbfs':
            if self.open_set:
                current_cell = min(self.open_set, key=lambda cell: cell.h)
                self.open_set.remove(current_cell)
                current_cell.visited = True
                if current_cell == self.end_cell:
                    self.reconstruct_path(current_cell)
                    self.solved = True
                    return
                neighbors = self.get_neighbors(current_cell)
                for neighbor in neighbors:
                    if neighbor.visited:
                        continue
                    neighbor.came_from = current_cell
                    neighbor.h = abs(neighbor.x - self.end_cell.x) + abs(neighbor.y - self.end_cell.y)
                    if neighbor not in self.open_set:
                        neighbor.in_path = True
                        self.open_set.append(neighbor)
            else:
                self.solved = True

        elif self.algorithm == 'dijkstra':
            if self.open_set:
                current_cell = min(self.open_set, key=lambda cell: cell.g)
                self.open_set.remove(current_cell)
                current_cell.visited = True
                if current_cell == self.end_cell:
                    self.reconstruct_path(current_cell)
                    self.solved = True
                    return
                neighbors = self.get_neighbors(current_cell)
                for neighbor in neighbors:
                    if neighbor.visited:
                        continue
                    tentative_g = current_cell.g + 1
                    if tentative_g < neighbor.g:
                        neighbor.came_from = current_cell
                        neighbor.g = tentative_g
                        neighbor.f = neighbor.g
                        if neighbor not in self.open_set:
                            neighbor.in_path = True
                            self.open_set.append(neighbor)
            else:
                self.solved = True

        elif self.algorithm == 'random':
            current_cell = self.current_cell
            current_cell.visited = True
            if current_cell == self.end_cell:
                self.reconstruct_path(current_cell)
                self.solved = True
                return
            neighbors = self.get_neighbors(current_cell)
            if neighbors:
                next_cell = random.choice(neighbors)
                next_cell.came_from = current_cell
                next_cell.in_path = True
                self.current_cell = next_cell
            else:
                # Dead end, backtrack
                if current_cell.came_from:
                    self.current_cell = current_cell.came_from
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
        while current:
            current.is_solution = True
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
                maze.solve_maze('4o_algo')
                waiting_for_selection = False
            elif event.key == pygame.K_g:
                selected_algorithm = 'gbfs'
                maze.solve_maze('gbfs')
                waiting_for_selection = False
            elif event.key == pygame.K_k:
                selected_algorithm = 'dijkstra'
                maze.solve_maze('dijkstra')
                waiting_for_selection = False
            elif event.key == pygame.K_r:
                selected_algorithm = 'random'
                maze.solve_maze('random')
                waiting_for_selection = False

    maze.update()
    maze.draw()

    if maze.generation_complete and not maze.solving and waiting_for_selection:
        # Display instructions
        font = pygame.font.SysFont(None, 24)
        text1 = font.render('Press D for DFS, B for BFS, F for 4o algo', True, pygame.Color('white'))
        text2 = font.render('Press G for Greedy Best-First Search, K for Dijkstra\'s Algorithm, R for Random Walk', True, pygame.Color('white'))
        sc.blit(text1, (20, 20))
        sc.blit(text2, (20, 50))

    pygame.display.flip()
    clock.tick(60)
