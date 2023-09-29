# Snake

import pygame
import random
import time

# window dimensions
WIDTH = 800
HEIGHT = 600

# dimensions of each segment of the snake and apple
SEG_SIZE = 20

# define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# initialize Pygame
pygame.init()

# set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# set up assets
snake = [(100, 100), (80, 100), (60, 100)]
apple = (random.randint(1, WIDTH//SEG_SIZE-1)*SEG_SIZE, random.randint(1, HEIGHT//SEG_SIZE-1)*SEG_SIZE)
direction = 'RIGHT'

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], SEG_SIZE, SEG_SIZE))

def draw_apple(apple):
    pygame.draw.rect(screen, RED, pygame.Rect(apple[0], apple[1], SEG_SIZE, SEG_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'

    # update snake position
    if direction == 'UP':
        snake.insert(0, (snake[0][0], snake[0][1]-SEG_SIZE))
    elif direction == 'DOWN':
        snake.insert(0, (snake[0][0], snake[0][1]+SEG_SIZE))
    elif direction == 'LEFT':
        snake.insert(0, (snake[0][0]-SEG_SIZE, snake[0][1]))
    elif direction == 'RIGHT':
        snake.insert(0, (snake[0][0]+SEG_SIZE, snake[0][1]))

    # check if snake collided with apple
    if snake[0] == apple:
        apple = (random.randint(1, WIDTH//SEG_SIZE-1)*SEG_SIZE, random.randint(1, HEIGHT//SEG_SIZE-1)*SEG_SIZE)
    else:
        snake.pop()

    # check if snake collided with itself or the edges
    if (snake[0] in snake[1:]) or (snake[0][0] < 0 or snake[0][0] >= WIDTH) or (snake[0][1] < 0 or snake[0][1] >= HEIGHT):
        running = False

    screen.fill((0, 0, 0))
    draw_snake(snake)
    draw_apple(apple)
    pygame.display.flip()

    # control the speed of the game
    time.sleep(0.5)

pygame.quit()
