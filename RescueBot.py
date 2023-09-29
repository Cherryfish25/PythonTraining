import pygame
pygame.init()

def main():
    botColor = (255, 0, 0)
    targetColor = (0, 0, 255)
    running = True
    backgroundColor = (255, 255, 255)
    botX = 0
    botY = 450
    move_distance = 50  # Adjust the number of pixels to move
    move_delay = 100  # Adjust the delay in milliseconds

    # Collision for the obstacles
    obstacleLocation = [
        (200, 50),
        (350, 50),
        (100, 150),
        (250, 150),
        (400, 150),
        (50, 250),
        (200, 250),
        (350, 250),
        (100, 350),
        (250, 350),
        (400, 350),
        (200, 450),
        (350, 450),
        (50, 50),
        (50, 450),
        (450, 450),
        (150, 100),
        (0,0,0,0)
        ]

    screen = pygame.display.set_mode((500, 500))
    screen.fill(backgroundColor)
    pygame.display.set_caption("Rescue Bot")

    last_move_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    current_time = pygame.time.get_ticks()
                    if (botX, botY - 50) not in obstacleLocation:
                        if botY >= 50:
                            if current_time - last_move_time >= move_delay:
                                botY -= move_distance
                                last_move_time = current_time
                elif event.key == pygame.K_DOWN:
                    current_time = pygame.time.get_ticks()
                    if (botX, botY + 50) not in obstacleLocation:
                        if botY <= 420:
                            if current_time - last_move_time >= move_delay:
                                botY += move_distance
                                last_move_time = current_time
                elif event.key == pygame.K_RIGHT:
                    current_time = pygame.time.get_ticks()
                    if (botX + 50, botY) not in obstacleLocation:
                        if botX <= 420:
                            if current_time - last_move_time >= move_delay:
                                botX += move_distance
                                last_move_time = current_time
                elif event.key == pygame.K_LEFT:
                    current_time = pygame.time.get_ticks()
                    if (botX - 50, botY) not in obstacleLocation:
                        if botX >= 50:
                            if current_time - last_move_time >= move_delay:
                                botX -= move_distance
                                last_move_time = current_time


        # Clear the screen
        screen.fill(backgroundColor)

        # Redraw the grid lines
        for x in range(0, 500, 50):
            pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, 500), 3)
            pygame.draw.line(screen, (0, 0, 0), (0, x), (500, x), 3)

        # Draw the square at the updated position
        pygame.draw.rect(screen, botColor, pygame.Rect(botX, botY, 47, 47))

        # Draw the target
        pygame.draw.rect(screen, targetColor, pygame.Rect(450, 50, 47, 47))

        if (botX, botY) == (450, 50):
            font = pygame.font.Font(None, 36)
            text = font.render("Bot reached the target!", True, (0, 255, 0))

            text_position = (200, 200)
            screen.blit(text, text_position)

        # Drawing the obstacles
        obstacles = [(200, 50, 50, 50),
            (350, 50, 50, 50),
            (100, 150, 50, 50),
            (250, 150, 50, 50),
            (400, 150, 50, 50),
            (50, 250, 50, 50),
            (200, 250, 50, 50),
            (350, 250, 50, 50),
            (100, 350, 50, 50),
            (250, 350, 50, 50),
            (400, 350, 50, 50),
            (200, 450, 50, 50),
            (350, 450, 50, 50),
            (50, 50, 50, 50),
            (50, 450, 50, 50),
            (450, 450, 50, 50),
            (150, 100, 50, 50),
            (0,0,0,0)
            ]


        indexNumber = 0

        for x in range(0, len(obstacles) - 1, 1):
            pygame.draw.rect(screen, (0,0,0), pygame.Rect(obstacles[indexNumber]))
            indexNumber = indexNumber + 1

        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
