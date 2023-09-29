import pygame
import sys

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 600))

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Game loop
while True:
    # Fill screen with white
    screen.fill(white)

    # Draw head
    pygame.draw.ellipse(screen, black, (300, 200, 200, 300))  # head

    # Draw eyes
    pygame.draw.ellipse(screen, blue, (350, 300, 40, 30))  # left eye
    pygame.draw.ellipse(screen, blue, (410, 300, 40, 30))  # right eye

    # Draw nose
    pygame.draw.line(screen, blue, (400, 330), (400, 360), 3)  # nose

    # Draw mouth
    pygame.draw.arc(screen, blue, (360, 420, 80, 40), 3.14, 2*3.14, 3)  # mouth

    # Update display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
