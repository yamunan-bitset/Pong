import pygame
import sys
import calculate
from consts import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Paddles and ball
left_paddle = pygame.Rect(30, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH-40, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)
ball_vel = [BALL_SPEED_X, BALL_SPEED_Y]
right_paddle_vel = 0
ai_calculate = calculate.Calculate(right_paddle, right_paddle_vel, ball, ball_vel, left_paddle)

# Scores
left_score = 0
right_score = 0
font = pygame.font.SysFont(None, 48)

def reset_ball():
    ball.center = (WIDTH//2, HEIGHT//2)
    ball_vel[0] *= -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    ai_calculate.update(ball, ball_vel, left_paddle)
    ai_calculate.random_moves()

    # Ball movement
    ball.x += ball_vel[0]
    ball.y += ball_vel[1]

    # Left paddle should follow the ball
    left_paddle.y = ball.y - PADDLE_HEIGHT // 2 

    # Collision with top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_vel[1] *= -1

    # Collision with paddles
    if ball.colliderect(left_paddle) and ball_vel[0] < 0:
        ball_vel[0] *= -1
    if ball.colliderect(right_paddle) and ball_vel[0] > 0:
        ball_vel[0] *= -1

    # Score
    if ball.left <= 0:
        right_score += 1
        reset_ball()
    if ball.right >= WIDTH:
        left_score += 1
        reset_ball()

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    screen.blit(left_text, (WIDTH//4, 20))
    screen.blit(right_text, (WIDTH*3//4, 20))

    pygame.display.flip()
    clock.tick(60)