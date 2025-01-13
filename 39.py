import pygame
import random

# 初始化 pygame
pygame.init()

# 遊戲視窗設定
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("皮卡丘打排球")

# 顏色定義
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# 遊戲參數
ball_radius = 15
ball_speed = [4, -4]
ball_pos = [WIDTH // 2, HEIGHT // 2]

paddle_width, paddle_height = 20, 80
pikachu1_pos = [50, HEIGHT // 2 - paddle_height // 2]
pikachu2_pos = [WIDTH - 50 - paddle_width, HEIGHT // 2 - paddle_height // 2]
paddle_speed = 5

# 分數
score1, score2 = 0, 0
font = pygame.font.Font(None, 36)

# 遊戲迴圈
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 控制按鍵
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and pikachu1_pos[1] > 0:
        pikachu1_pos[1] -= paddle_speed
    if keys[pygame.K_s] and pikachu1_pos[1] < HEIGHT - paddle_height:
        pikachu1_pos[1] += paddle_speed
    if keys[pygame.K_UP] and pikachu2_pos[1] > 0:
        pikachu2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and pikachu2_pos[1] < HEIGHT - paddle_height:
        pikachu2_pos[1] += paddle_speed

    # 更新球的位置
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # 碰撞檢測：上下邊界
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # 碰撞檢測：左側皮卡丘
    if (pikachu1_pos[0] <= ball_pos[0] - ball_radius <= pikachu1_pos[0] + paddle_width and
        pikachu1_pos[1] <= ball_pos[1] <= pikachu1_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]

    # 碰撞檢測：右側皮卡丘
    if (pikachu2_pos[0] <= ball_pos[0] + ball_radius <= pikachu2_pos[0] + paddle_width and
        pikachu2_pos[1] <= ball_pos[1] <= pikachu2_pos[1] + paddle_height):
        ball_speed[0] = -ball_speed[0]

    # 判斷得分
    if ball_pos[0] < 0:
        score2 += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.choice([4, -4]), random.choice([4, -4])]
    if ball_pos[0] > WIDTH:
        score1 += 1
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_speed = [random.choice([4, -4]), random.choice([4, -4])]

    # 畫面更新
    screen.fill(WHITE)

    # 畫球
    pygame.draw.circle(screen, RED, ball_pos, ball_radius)

    # 畫皮卡丘
    pygame.draw.rect(screen, YELLOW, (*pikachu1_pos, paddle_width, paddle_height))
    pygame.draw.rect(screen, YELLOW, (*pikachu2_pos, paddle_width, paddle_height))

    # 顯示分數
    score_text = font.render(f"Player 1: {score1}  Player 2: {score2}", True, BLACK)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 20))

    # 更新畫面
    pygame.display.flip()

    # 控制遊戲速度
    clock.tick(60)

pygame.quit()
