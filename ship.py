import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter!")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5

# Enemy settings
enemy_size = 50
enemy_speed = 3
enemies = []

# Bullet settings
bullet_width, bullet_height = 5, 10
bullets = []
bullet_speed = 7

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

def move_bullets():
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

def check_collisions():
    global score
    for enemy in enemies[:]:
        for bullet in bullets[:]:
            if enemy.colliderect(bullet):
                enemies.remove(enemy)
                bullets.remove(bullet)
                enemies.append(create_enemy())
                score += 1
                break

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player_x + player_size//2, player_y, bullet_width, bullet_height))
    
    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    move_enemies()
    move_bullets()
    check_collisions()
    
    # Check collision
    if check_collision(player_rect):
        running = False
    
    # Draw player, enemies, and bullets
    pygame.draw.rect(screen, BLUE, player_rect)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    for bullet in bullets:
        pygame.draw.rect(screen, YELLOW, bullet)
    
    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
