import pygame
import random

# define some constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CIRCLE_RADIUS = 20

# initialize Pygame
pygame.init()

# set up some variables
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = pygame.font.Font(None, 36)
running = True
circle_x = random.randint(CIRCLE_RADIUS, WINDOW_WIDTH - CIRCLE_RADIUS)
circle_y = random.randint(CIRCLE_RADIUS, WINDOW_HEIGHT - CIRCLE_RADIUS)
circle_dx = random.randint(-1, 1)
circle_dy = random.randint(-1, 1)
circle_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
hits = 0
total_clicks = 0

while running:
    # clear the screen
    screen.fill((0, 0, 0))

    # draw the circle
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), CIRCLE_RADIUS)

    # move the circle
    circle_x += circle_dx
    circle_y += circle_dy

    # if the circle hits the edge of the screen, make it bounce
    if circle_x < CIRCLE_RADIUS or circle_x > WINDOW_WIDTH - CIRCLE_RADIUS:
        circle_dx *= -1
    if circle_y < CIRCLE_RADIUS or circle_y > WINDOW_HEIGHT - CIRCLE_RADIUS:
        circle_dy *= -1

    # draw the score
    if total_clicks > 0:
        score_text = font.render('Hit ratio: {:.2f}'.format(hits / total_clicks), True, (255, 255, 255))
    else:
        score_text = font.render('Hit ratio: 0', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # lose the game
    score = (hits / total_clicks) if total_clicks > 0 else 0
    if total_clicks > 10 and score < 0.2:  # modify this condition as needed
        running = False
        screen.fill((0, 0, 0))
        lose_text = font.render('Game Over', True, (255, 255, 255))
        screen.blit(lose_text,
                    ((WINDOW_WIDTH - lose_text.get_width()) // 2, (WINDOW_HEIGHT - lose_text.get_height()) // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # wait 2 seconds before quitting
        running = False

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            total_clicks += 1
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (circle_x - mouse_x)**2 + (circle_y - mouse_y)**2 < CIRCLE_RADIUS**2:
                hits += 1
                circle_x = random.randint(CIRCLE_RADIUS, WINDOW_WIDTH - CIRCLE_RADIUS)
                circle_y = random.randint(CIRCLE_RADIUS, WINDOW_HEIGHT - CIRCLE_RADIUS)
                circle_dx = random.randint(-1, 1)
                circle_dy = random.randint(-1, 1)
                circle_color = pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # update the display
    pygame.display.flip()

# quit Pygame
pygame.quit()
