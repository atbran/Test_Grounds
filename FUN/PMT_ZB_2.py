#Simulation of a photomultiplier tube (PMT) with dynodes.
#The PMT has a photocathode, dynodes, and an anode. Photons are emitted from the photocathode, and particles are released
#from the dynodes. The particles move and bounce off the dynodes and the anode.
#You can adjust the number of dynodes, sensitivity, photon speed and photon error.
#should refactor at some point
#WIP
# import time
import pygame
import sys
import math
import random

WIDTH, HEIGHT, FPS = 1000, 600, 60
BLACK, WHITE, BLUE, RED, GREEN, YELLOW = (0, 0, 0), (255, 255, 255), (100, 149, 237), (220, 20, 60), (100, 139, 34), (255, 215, 0)

# You can now input any number of dynodes
num_dynodes = 12  # Adjust this number as needed
photocathode_x, anode_x = 100, 900
HEIGHT_CENTER = HEIGHT / 2

MAX_PARTICLES = 50_000  # Maximum number of active particles
INITIAL_PHOTONS = 10  # Initial number of photons to emit
photons_lost = 0

# Dynamic parameters
photocathode_sensitivity = 2  # Default sensitivity (1.0 to 5.0)
photon_speed = 5  # Default photon speed
photon_error = 1  # Default photon error in degrees (max 15)

def calculate_dynode_positions(photocathode_x, anode_x, num_dynodes, height_center):
    """Calculate dynode positions and sizes dynamically based on the number of dynodes."""
    delta_x = (anode_x - photocathode_x) / (num_dynodes + 1)

    # Adjust dynode radius to prevent overlap and fit within the screen
    dynode_radius = min(40, delta_x * 0.4)
    dynode_radius = max(10, dynode_radius)  # Ensure a minimum size


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
small_font = pygame.font.SysFont(None, 24)

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

def calculate_velocity(current_pos, target_pos, speed):
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
    global photon_emitted, particles, photon_x, photon_y, photon_vx, photons_detected, photons_lost
    particles.clear()
    photon_x, photon_y = photocathode_x - 150, HEIGHT_CENTER
    photon_vx = 3
    photon_emitted = False
    photons_detected = 0
    photons_lost = 0

# UI elements for dynamic parameters
speed_slider = pygame.Rect(10, HEIGHT - 120, 200, 20)
error_slider = pygame.Rect(10, HEIGHT - 70, 200, 20)
sensitivity_slider = pygame.Rect(10, HEIGHT - 20, 200, 20)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if speed_slider.collidepoint(event.pos):
                photon_speed = 1 + 9 * (event.pos[0] - speed_slider.x) / speed_slider.width
            elif error_slider.collidepoint(event.pos):
                photon_error = 15 * (event.pos[0] - error_slider.x) / error_slider.width
            elif sensitivity_slider.collidepoint(event.pos):
                photocathode_sensitivity = 1 + 4 * (event.pos[0] - sensitivity_slider.x) / sensitivity_slider.width

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
            for _ in range(INITIAL_PHOTONS):
                angle = math.atan2(dynodes[0].rect.centery - HEIGHT_CENTER, dynodes[0].rect.centerx - photocathode_x)
                angle += math.radians((random.random() - 0.5) * photon_error * (5 / num_dynodes))
                vx, vy = photon_speed * math.cos(angle), photon_speed * math.sin(angle)
                particles.append(Particle(photocathode_x, HEIGHT_CENTER, vx, vy, 0, is_electron=True))
    else:
        new_particles = []
        for particle in particles:
            particle.move()

            if particle.is_off_screen():
                photons_lost += 1
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
                    next_target = dynodes[particle.generation + 1].rect.center if particle.generation + 1 < num_dynodes else (anode_x, HEIGHT_CENTER)
                    new_particle_count = random.randint(1, int(photocathode_sensitivity))  # Random number between 1 and sensitivity
                    for _ in range(new_particle_count):
                        if len(new_particles) + len(particles) < MAX_PARTICLES:
                            base_angle = math.atan2(next_target[1] - particle.y, next_target[0] - particle.x)
                            angle = base_angle + math.radians((random.random() - 0.5) * photon_error * (5 / num_dynodes))
                            vx, vy = photon_speed * math.cos(angle), photon_speed * math.sin(angle)
                            new_particles.append(Particle(particle.x, particle.y, vx, vy, particle.generation + 1,
                                                          int(particle.intensity * 1.2), is_electron=False))
                    continue
            new_particles.append(particle)
        particles = new_particles

    if len(particles) == 0 and photon_emitted:
        reset_simulation()

    photon_count_text = font.render(f"Photons Collected: {photon_count}", True, WHITE)
    active_particles_text = font.render(f"Active Particles: {len(particles)}", True, WHITE)
    photons_lost_text = font.render(f"Photons Lost: {photons_lost}", True, WHITE)
    text_rect1 = photon_count_text.get_rect(center=(WIDTH // 2, 30))
    text_rect2 = active_particles_text.get_rect(center=(WIDTH // 2, 70))
    text_rect3 = photons_lost_text.get_rect(center=(WIDTH // 2, 110))
    screen.blit(photon_count_text, text_rect1)
    screen.blit(active_particles_text, text_rect2)
    screen.blit(photons_lost_text, text_rect3)

    # Draw UI elements
    pygame.draw.rect(screen, WHITE, speed_slider)
    pygame.draw.rect(screen, RED, (speed_slider.x + speed_slider.width * (photon_speed - 1) / 9 - 5, speed_slider.y, 10, speed_slider.height))
    speed_label = small_font.render("Photon Speed", True, WHITE)
    screen.blit(speed_label, (speed_slider.x, speed_slider.y - 20))

    pygame.draw.rect(screen, WHITE, error_slider)
    pygame.draw.rect(screen, GREEN, (error_slider.x + error_slider.width * photon_error / 15 - 5, error_slider.y, 10, error_slider.height))
    error_label = small_font.render("Photon Error", True, WHITE)
    screen.blit(error_label, (error_slider.x, error_slider.y - 20))

    pygame.draw.rect(screen, WHITE, sensitivity_slider)
    pygame.draw.rect(screen, BLUE, (sensitivity_slider.x + sensitivity_slider.width * (photocathode_sensitivity - 1) / 4 - 5, sensitivity_slider.y, 10, sensitivity_slider.height))
    sensitivity_label = small_font.render("Photocathode Sensitivity", True, WHITE)
    screen.blit(sensitivity_label, (sensitivity_slider.x, sensitivity_slider.y - 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()