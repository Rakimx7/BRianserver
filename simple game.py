import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks!")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_speed = 5
enemies = []

# Game variables
running = True
score = 0
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

def create_enemy():
    x_pos = random.randint(0, WIDTH - enemy_size)
    return pygame.Rect(x_pos, 0, enemy_size, enemy_size)

def move_enemies():
    global score
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)
            enemies.append(create_enemy())
            score += 1

def check_collision(player_rect):
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            return True
    return False

# Initial enemies
enemies.append(create_enemy())

while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    move_enemies()
    
    # Check collision
    if check_collision(player_rect):
        running = False
    
    # Draw player and enemies
    pygame.draw.rect(screen, BLUE, player_rect)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
