import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
GROUND_HEIGHT = 100
GRAVITY = 0.25
JUMP_STRENGTH = -7
PIPE_WIDTH = 80
PIPE_GAP = 200
PIPE_SPEED = 3

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_image = pygame.image.load("bird.png")
bird_rect = bird_image.get_rect()
bird_rect.center = (100, SCREEN_HEIGHT // 2)

pipe_image = pygame.image.load("pipe.png")
pipe_rect = pipe_image.get_rect()

ground_image = pygame.Surface((SCREEN_WIDTH, GROUND_HEIGHT))
ground_image.fill(BLUE)
ground_rect = ground_image.get_rect()
ground_rect.topleft = (0, SCREEN_HEIGHT - GROUND_HEIGHT)

# Game variables
bird_velocity = 0
score = 0
pipes = []

# Load a font for the score
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = JUMP_STRENGTH

    # Move the bird
    bird_velocity += GRAVITY
    bird_rect.y += bird_velocity

    # Check for collisions
    if bird_rect.colliderect(ground_rect):
        pygame.quit()
        sys.exit()

    for pipe in pipes:
        pipe[0] -= PIPE_SPEED
        if bird_rect.colliderect(pipe[1]) or bird_rect.colliderect(pipe[2]):
            pygame.quit()
            sys.exit()
        if pipe[0] + PIPE_WIDTH < 0:
            pipes.remove(pipe)
            score += 1

    # Add a new pipe
    if len(pipes) < 3:
        pipe_height = random.randint(50, 300)
        pipe_rect_top = pipe_image.get_rect(topleft=(SCREEN_WIDTH, -pipe_height))
        pipe_rect_bottom = pipe_image.get_rect(topleft=(SCREEN_WIDTH, pipe_height + PIPE_GAP))
        pipes.append([SCREEN_WIDTH, pipe_rect_top, pipe_rect_bottom])

    # Draw everything
    screen.fill(WHITE)
    screen.blit(bird_image, bird_rect)
    screen.blit(ground_image, ground_rect)

    for pipe in pipes:
        screen.blit(pipe_image, pipe[1])
        screen.blit(pipe_image, pipe[2])

    # Draw the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(60)
