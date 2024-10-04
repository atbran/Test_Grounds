import time
import pygame
import sys
import math
import random

WIDTH, HEIGHT, FPS = 1000, 600, 60
BLACK, WHITE, BLUE, RED, GREEN, YELLOW = (0, 0, 0), (255, 255, 255), (100, 149, 237), (220, 20, 60), (34, 139, 34), (
255, 215, 0)

# You can now input any number of dynodes
num_dynodes = 9  # Adjust this number as needed
photocathode_x, anode_x = 100, 900
HEIGHT_CENTER = HEIGHT / 2

MAX_PARTICLES = 30000  # Maximum number of active particles


def calculate_dynode_positions(photocathode_x, anode_x, num_dynodes, height_center):
    """Calculate dynode positions and sizes dynamically based on the number of dynodes."""
    delta_x = (anode_x - photocathode_x) / (num_dynodes + 1)

    # Adjust dynode radius to prevent overlap and fit within the screen
    dynode_radius = min(40, delta_x * 0.4)
    dynode_radius = max(10, dynode_radius)  # Ensure a minimum size

    # Adjust vertical offset based on dynode radius
    vertical_offset = dynode_radius * 1.5

    positions = []
    for i in range(num_dynodes):
        x = photocathode_x + (i + 1) * delta_x
        y = height_center + ((-1) ** i) * vertical_offset
        positions.append((x, y))
    return positions, dynode_radius


dynodes_positions, dynode_radius = calculate_dynode_positions(photocathode_x, anode_x, num_dynodes, HEIGHT_CENTER)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Photomultiplier Tube Simulation")

font = pygame.font.SysFont(None, 36)


def create_crescent(radius, thickness, color):
    size = (radius * 2, radius * 2)
    surf = pygame.Surface(size, pygame.SRCALPHA)
    pygame.draw.circle(surf, color, (radius, radius), radius)
    pygame.draw.circle(surf, (0, 0, 0, 0), (radius + thickness, radius), radius - thickness)
    return surf


class Dynode:
    def __init__(self, center, next_center, radius, thickness=None, color=GREEN):
        if thickness is None:
            thickness = radius / 4
        self.rect = create_crescent(radius, thickness, color).get_rect(center=center)
        dx, dy = next_center[0] - center[0], next_center[1] - center[1]
        angle = math.degrees(math.atan2(-dy, dx))
        self.surface = pygame.transform.rotate(create_crescent(radius, thickness, color), angle)
        self.rect = self.surface.get_rect(center=center)
        self.mask = pygame.mask.from_surface(self.surface)


class Particle:
    def __init__(self, x, y, vx, vy, generation, intensity=1, is_electron=True):
        self.x, self.y = x, y
        self.vx, self.vy = vx, vy
        self.generation = generation
        self.intensity = intensity
        self.is_electron = is_electron

    def move(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self, surface):
        color = YELLOW if self.is_electron else WHITE
        size = max(2, int(3 * math.log(self.intensity + 1))) if self.is_electron else 4
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), size)

    def is_off_screen(self):
        return self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT


def calculate_velocity(current_pos, target_pos, speed=5):
    dx, dy = target_pos[0] - current_pos[0], target_pos[1] - current_pos[1]
    dist = math.hypot(dx, dy)
    return (0, 0) if dist == 0 else (speed * dx / dist, speed * dy / dist)


dynodes = [Dynode(dynodes_positions[i],
                  dynodes_positions[i + 1] if i < num_dynodes - 1 else (anode_x, HEIGHT_CENTER),
                  radius=dynode_radius)
           for i in range(num_dynodes)]
particles, clock, photon_emitted, running, time_counter = [], pygame.time.Clock(), False, True, 0
photon_x, photon_y, photon_vx = photocathode_x - 150, HEIGHT_CENTER, 3

flash_active, flash_counter, flash_duration = False, 0, 1000
photon_count, photons_detected = 0, 0
squares = []
square_lifetime = 30

# Define the detection area for the anode
ANODE_WIDTH, ANODE_HEIGHT = 10, 100
anode_rect = pygame.Rect(anode_x, HEIGHT_CENTER - ANODE_HEIGHT // 2, ANODE_WIDTH, ANODE_HEIGHT)


def reset_simulation():
    global photon_emitted, particles, photon_x, photon_y, photon_vx, photons_detected
    particles.clear()
    photon_x, photon_y = photocathode_x - 150, HEIGHT_CENTER
    photon_vx = 3
    photon_emitted = False
    photons_detected = 0


while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, BLUE, (photocathode_x - 10, HEIGHT_CENTER - 50, 10, 100))
    pygame.draw.rect(screen, RED, anode_rect)

    [screen.blit(dynode.surface, dynode.rect) for dynode in dynodes]

    for square in squares:
        x, y, remaining_lifetime = square
        pygame.draw.rect(screen, WHITE, (x, y, 5, 5))
        square[2] -= 1
    squares = [square for square in squares if square[2] > 0]

    if flash_active:
        row, col = divmod(flash_counter, 100)
        x, y = col * 8, 100 + row * 8
        squares.append([x, y, square_lifetime])
        flash_counter += 1
        if flash_counter >= flash_duration:
            flash_active, flash_counter = False, 0

    if not photon_emitted and len(particles) < MAX_PARTICLES:
        pygame.draw.circle(screen, WHITE, (int(photon_x), int(photon_y)), 8)
        photon_x += photon_vx
        if photon_x >= photocathode_x:
            photon_emitted = True
            vx, vy = calculate_velocity((photocathode_x, HEIGHT_CENTER), dynodes[0].rect.center)
            particles.append(Particle(photocathode_x, HEIGHT_CENTER, vx, vy, 0, is_electron=True))
    else:
        new_particles = []
        for particle in particles:
            particle.move()

            if particle.is_off_screen():
                continue

            particle.draw(screen)

            # Check for anode collision first
            if anode_rect.collidepoint(particle.x, particle.y):
                flash_active = True
                photon_count += 1
                photons_detected += 1
                continue

            if particle.generation < num_dynodes:
                target_dynode = dynodes[particle.generation]
                local_x = int(particle.x - target_dynode.rect.left)
                local_y = int(particle.y - target_dynode.rect.top)
                if 0 <= local_x < target_dynode.surface.get_width() and \
                        0 <= local_y < target_dynode.surface.get_height() and \
                        target_dynode.mask.get_at((local_x, local_y)):
                    next_target = dynodes[
                        particle.generation + 1].rect.center if particle.generation + 1 < num_dynodes else (
                    anode_x, HEIGHT_CENTER)
                    for _ in range(3):
                        if len(new_particles) + len(particles) < MAX_PARTICLES:
                            angle = math.atan2(next_target[1] - particle.y, next_target[0] - particle.x) + math.radians(
                                random.uniform(-10, 10))
                            speed = 5 * random.uniform(0.8, 1.2)
                            vx, vy = speed * math.cos(angle), speed * math.sin(angle)
                            new_particles.append(Particle(particle.x, particle.y, vx, vy, particle.generation + 1,
                                                          particle.intensity * 1.5, is_electron=False))
                    continue
            new_particles.append(particle)
        particles = new_particles

    if len(particles) == 0 and photon_emitted:
        reset_simulation()

    photon_count_text = font.render(f"Photons Collected: {photon_count}", True, WHITE)
    active_particles_text = font.render(f"Active Particles: {len(particles)}", True, WHITE)
    text_rect1 = photon_count_text.get_rect(center=(WIDTH // 2, 30))
    text_rect2 = active_particles_text.get_rect(center=(WIDTH // 2, 70))
    screen.blit(photon_count_text, text_rect1)
    screen.blit(active_particles_text, text_rect2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()