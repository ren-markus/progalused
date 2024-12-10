import pygame
import random

pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CAR_WIDTH = 50
CAR_HEIGHT = 100
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 100
OBSTACLE_SPEED = 5
FPS = 70

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Laeb pildid
car_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT))
car_image.fill(GREEN)
pygame.display.set_caption('Loading Screen')
image = pygame.image.load('highway.png')

obstacle_image = pygame.Surface((OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
obstacle_image.fill(RED)

# Ekraani seadistamine
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Kiired ja vigased")

# Mängu muutujad
def reset_game():
    global car_x, car_y, obstacles, score, speed, running
    car_x = SCREEN_WIDTH // 2 - CAR_WIDTH // 2
    car_y = SCREEN_HEIGHT - CAR_HEIGHT - 10
    obstacles = []
    score = 0
    speed = 0
    running = True

reset_game()
clock = pygame.time.Clock()
game_over = False

def create_obstacle():
    x = random.randint(0, SCREEN_WIDTH - OBSTACLE_WIDTH)
    return [x, -OBSTACLE_HEIGHT]

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_image, (obstacle[0], obstacle[1]))

def move_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle[1] += OBSTACLE_SPEED

def remove_offscreen_obstacles(obstacles):
    return [obstacle for obstacle in obstacles if obstacle[1] < SCREEN_HEIGHT]

def check_collision(car_x, car_y, obstacles):
    for obstacle in obstacles:
        if (car_x < obstacle[0] + OBSTACLE_WIDTH and
            car_x + CAR_WIDTH > obstacle[0] and
            car_y < obstacle[1] + OBSTACLE_HEIGHT and
            car_y + CAR_HEIGHT > obstacle[1]):
            return True
    return False

# Mäng loopis
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and car_x > 0:
            car_x -= 5
        if keys[pygame.K_RIGHT] and car_x < SCREEN_WIDTH - CAR_WIDTH:
            car_x += 5

        # Create new obstacles
        if random.randint(1, 20) == 1:  # Adjust the probability of obstacle creation
            obstacles.append(create_obstacle())

        move_obstacles(obstacles)
        obstacles = remove_offscreen_obstacles(obstacles)

        if check_collision(car_x, car_y, obstacles):
            game_over = True

        score += 1  # Iga sekund läheb skoor kõrgemaks
        speed = min(100, score // 10)  # Kiirus tõuseb koos skooriga, kiirus piiratud kuni 100km/h

        
        screen.blit(car_image, (car_x, car_y))
        draw_obstacles(obstacles)

        # Kuvab skoori
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        # Kuvab spedomeetri
        speed_text = font.render(f"Speed: {speed} km/h", True, BLACK)
        screen.blit(speed_text, (10, 50))

    else:
        # Mäng läbi screen
        font = pygame.font.Font(None, 74)
        text = font.render("Mäng läbi!", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))

        font = pygame.font.Font(None, 36)
        text = font.render("Vajutage R, et uuesti proovida!", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))

        # Kuvab lõppskoor
        final_score_text = font.render(f"Lõplik skoor: {score}", True, BLACK)
        screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

        # Kuvab lõppkiirus
        
        final_speed_text = font.render(f"Lõplik kiirus: {speed} km/h", True, BLACK)
        screen.blit(final_speed_text, (SCREEN_WIDTH // 2 - final_speed_text.get_width() // 2, SCREEN_HEIGHT // 2 + 90))

        if keys[pygame.K_r]:
            reset_game()
            game_over = False

    pygame.display.flip()
    clock.tick(FPS)