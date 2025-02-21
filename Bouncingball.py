import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing Ball Animation")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ball_radius = 20
ball_x, ball_y = width // 2, height // 2
ball_dx, ball_dy = 5, 5
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    ball_x += ball_dx
    ball_y += ball_dy

    if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
        ball_dx *= -1
    if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
        ball_dy *= -1
    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(60)
