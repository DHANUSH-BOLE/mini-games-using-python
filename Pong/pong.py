import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)

# Define constants
BALL_RADIUS = 10
PAD_WIDTH = 10
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
BALL_POS = [WIDTH // 2, HEIGHT // 2]
BALL_VEL = [random.choice([-2, 2]), random.choice([-2, 2])]
PADDLE1_POS = HEIGHT // 2 - HALF_PAD_HEIGHT
PADDLE2_POS = HEIGHT // 2 - HALF_PAD_HEIGHT
PADDLE_VEL = 4
score1 = 0
score2 = 0

# Function to spawn ball
def spawn_ball():
    global BALL_POS, BALL_VEL
    BALL_POS = [WIDTH // 2, HEIGHT // 2]
    BALL_VEL = [random.choice([-2, 2]), random.choice([-2, 2])]

# Function to update ball position and velocity
def update_ball():
    global BALL_POS, BALL_VEL, score1, score2
    BALL_POS[0] += BALL_VEL[0]
    BALL_POS[1] += BALL_VEL[1]

    # Collision with top or bottom wall
    if BALL_POS[1] - BALL_RADIUS <= 0 or BALL_POS[1] + BALL_RADIUS >= HEIGHT:
        BALL_VEL[1] = -BALL_VEL[1]
    
    # Collision with paddles
    if BALL_POS[0] - BALL_RADIUS <= PAD_WIDTH:
        if PADDLE1_POS <= BALL_POS[1] <= PADDLE1_POS + PAD_HEIGHT:
            BALL_VEL[0] = -BALL_VEL[0]
        else:
            score2 += 1
            spawn_ball()
    elif BALL_POS[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if PADDLE2_POS <= BALL_POS[1] <= PADDLE2_POS + PAD_HEIGHT:
            BALL_VEL[0] = -BALL_VEL[0]
        else:
            score1 += 1
            spawn_ball()

# Function to draw elements on the screen
def draw():
    global PADDLE1_POS, PADDLE2_POS, score1, score2

    # Clear the screen
    screen.fill(WHITE)

    # Draw mid line and gutters
    pygame.draw.line(screen, PURPLE, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 3)
    pygame.draw.line(screen, PURPLE, [PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(screen, PURPLE, [WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1)

    # Draw paddles and ball
    pygame.draw.rect(screen, PURPLE, [0, PADDLE1_POS, PAD_WIDTH, PAD_HEIGHT])
    pygame.draw.rect(screen, PURPLE, [WIDTH - PAD_WIDTH, PADDLE2_POS, PAD_WIDTH, PAD_HEIGHT])
    pygame.draw.circle(screen, PURPLE, BALL_POS, BALL_RADIUS)

    # Draw scores
    font = pygame.font.Font(None, 36)
    score1_text = font.render(str(score1), True, PURPLE)
    score2_text = font.render(str(score2), True, PURPLE)
    screen.blit(score1_text, (WIDTH // 4, 50))
    screen.blit(score2_text, (3 * WIDTH // 4, 50))

    # Update the display
    pygame.display.flip()

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update paddle positions
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and PADDLE1_POS > 0:
        PADDLE1_POS -= PADDLE_VEL
    if keys[pygame.K_s] and PADDLE1_POS < HEIGHT - PAD_HEIGHT:
        PADDLE1_POS += PADDLE_VEL
    if keys[pygame.K_UP] and PADDLE2_POS > 0:
        PADDLE2_POS -= PADDLE_VEL
    if keys[pygame.K_DOWN] and PADDLE2_POS < HEIGHT - PAD_HEIGHT:
        PADDLE2_POS += PADDLE_VEL

    # Update ball position and velocity
    update_ball()

    # Draw elements on the screen
    draw()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
