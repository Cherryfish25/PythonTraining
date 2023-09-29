import pygame
import random
import numpy as np

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Define window parameters
WIDTH, HEIGHT = 800, 600
SIZE = (WIDTH, HEIGHT)

# Define grid parameters
TILESIZE = 20
GRIDWIDTH = WIDTH // TILESIZE
GRIDHEIGHT = HEIGHT // TILESIZE

# Create window
screen = pygame.display.set_mode(SIZE)

# Set the frame rate
FPS = 60
clock = pygame.time.Clock()

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ticks = 0

        # Initialize the neural network with random weights
        self.weights = np.random.randn(2, 2)


    def draw(self):
        pygame.draw.rect(screen, RED, (self.x*TILESIZE, self.y*TILESIZE, TILESIZE, TILESIZE))

    def update(self):
        self.ticks += 1
        if self.ticks % 10 == 0:  # only move every 10th tick
            # Find the direction to the nearest food source
            nearest_food = min(food, key=lambda f: (self.x-f[0])**2 + (self.y-f[1])**2)
            dx, dy = nearest_food[0] - self.x, nearest_food[1] - self.y

            # Feed the direction into the neural network
            inputs = np.array([dx, dy])
            outputs = np.sign(self.weights @ inputs)

            # Replace NaN values with zero
            outputs = np.nan_to_num(outputs)

            # Convert outputs to integers
            dx, dy = int(outputs[0]), int(outputs[1])

            # Move the entity
            if world[min(max(self.x+dx, 0), GRIDWIDTH-1)][min(max(self.y+dy, 0), GRIDHEIGHT-1)] == 'land':
                self.x += dx
                self.y += dy


# Create the world (a 2D list of tiles)
world = [['water' if random.random() < 0.3 else 'land' for _ in range(GRIDHEIGHT)] for _ in range(GRIDWIDTH)]

# Create some entities
entities = [Entity(random.randint(0, GRIDWIDTH-1), random.randint(0, GRIDHEIGHT-1)) for _ in range(10)]

# Create some food
food = [(random.randint(0, GRIDWIDTH-1), random.randint(0, GRIDHEIGHT-1)) for _ in range(20)]

# Game loop
running = True
while running:
    clock.tick(FPS)  # limit the frame rate

    # Fill screen with white
    screen.fill(WHITE)

    # Draw the world
    for x in range(GRIDWIDTH):
        for y in range(GRIDHEIGHT):
            if world[x][y] == 'water':
                pygame.draw.rect(screen, BLUE, (x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE))

    # Draw food
    for f in food:
        pygame.draw.rect(screen, YELLOW, (f[0]*TILESIZE, f[1]*TILESIZE, TILESIZE, TILESIZE))

    # Draw entities
    for entity in entities:
        entity.draw()

    # Update entities
    for entity in entities:
        entity.update()

        # Check if entity is on a food source and remove it
        if (entity.x, entity.y) in food:
            food.remove((entity.x, entity.y))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.flip()

pygame.quit()

