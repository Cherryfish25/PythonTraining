import pygame
import sys

# Game constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BIRD_SIZE = 50
PLATFORM_SIZE = (100, 20)
TARGET_SIZE = 50
GRAVITY = 0.1
BIRD_LAUNCH_VELOCITY = [5, -5]  # Velocity applied when the bird is launched
START_PLATFORM_Y = SCREEN_HEIGHT - 50  # Y position of starting platform


class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([BIRD_SIZE, BIRD_SIZE])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y - self.rect.height  # Adjust the starting position
        self.velocity = [0, 0]


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface(PLATFORM_SIZE)
        self.image.fill((255, 140, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([TARGET_SIZE, TARGET_SIZE])
        self.image.fill((0, 128, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class StartPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([SCREEN_WIDTH, PLATFORM_SIZE[1]])
        self.image.fill((128, 0, 128))  # Purple color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    start_platform = StartPlatform(0, START_PLATFORM_Y)
    bird = Bird(SCREEN_WIDTH // 2, START_PLATFORM_Y)
    target = Target(SCREEN_WIDTH - TARGET_SIZE, SCREEN_HEIGHT // 2)
    platforms = pygame.sprite.Group()
    selected_platform = None  # Platform being dragged

    # Add some initial platforms
    for i in range(3):
        platform = Platform(i * (SCREEN_WIDTH // 3), SCREEN_HEIGHT // 2)
        platforms.add(platform)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for platform in platforms:
                    if platform.rect.collidepoint(x, y):
                        selected_platform = platform
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                selected_platform = None
            elif event.type == pygame.MOUSEMOTION:
                if selected_platform is not None:
                    x, y = event.pos
                    selected_platform.rect.x, selected_platform.rect.y = x, y
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and bird.velocity == [0, 0]:  # Only launch if bird is not moving
                    bird.velocity = BIRD_LAUNCH_VELOCITY.copy()

        # Bird physics
        bird.rect.x += bird.velocity[0]
        bird.rect.y += bird.velocity[1]
        if bird.rect.colliderect(start_platform.rect) and bird.velocity == [0, 0]:
            bird.rect.y = start_platform.rect.y - BIRD_SIZE  # Keep bird on start platform
        else:
            bird.velocity[1] += GRAVITY

        # Bounce bird off platforms
        for platform in platforms:
            if bird.rect.colliderect(platform.rect):
                bird.velocity[1] = -abs(bird.velocity[1])  # Bounce upwards

        # Check if bird has hit target
        if bird.rect.colliderect(target.rect):
            print("You win!")

            pygame.quit()
            sys.exit()

        # Game over if bird goes off screen
        if bird.rect.y > SCREEN_HEIGHT or bird.rect.y < 0 or bird.rect.x > SCREEN_WIDTH:
            print("Game over!")
            pygame.quit()
            sys.exit()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw all sprites
        screen.blit(bird.image, bird.rect)
        screen.blit(start_platform.image, start_platform.rect)
        screen.blit(target.image, target.rect)
        for platform in platforms:
            screen.blit(platform.image, platform.rect)

        pygame.display.flip()
        clock.tick(60)  # Limit to 60 FPS

if __name__ == "__main__":
    main()
