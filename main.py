import pygame
import sys
import random
import math
from math import sin, cos, pi
import functions
from CONSTANCE import *
from functions import *

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

def main():

    #Font
    terminus = pygame.font.SysFont("terminus", 48)

    #GAME VARIABLES

    #Right paddle variables
    right_x = WIDTH - 120 - PADDLE_WIDTH
    right_y = [(Y_ORIGIN - (PADDLE_HEIGHT // 2))]
    right_up = pygame.K_UP
    right_down = pygame.K_LEFT
    right_rect = pygame.Rect(right_x, right_y[0], PADDLE_WIDTH, PADDLE_HEIGHT)

    #Left paddle variables
    left_x = 120
    left_y = [(Y_ORIGIN - (PADDLE_HEIGHT // 2))]
    left_up = pygame.K_w
    left_down = pygame.K_d
    left_rect = pygame.Rect(left_x, left_y[0], PADDLE_WIDTH, PADDLE_HEIGHT)

    #Score variables
    right_score = [0]
    left_score = [0]
    right_score_rect = pygame.Rect(WIDTH - 100, 32, 64, 64) 
    left_score_rect = pygame.Rect(20, 32, 64, 64)
    right = "right"
    left = "left"

    #Ball variables
    ball_pos = [(X_ORIGIN - BALL // 2), #x
                (random.randint(0, HEIGHT - BALL))] #y
    r = 4
    theta = random.uniform(0, 2 * pi)
    vel = [r, r * sin(theta)]

    active = True
    while active:

        screen.fill((DARK_GRAY))
        
        divider_line(screen)

        #Right paddle
        control_paddle(screen, right_y, right_up, right_down)
        paddle(screen, right_x, right_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        score(screen, terminus, right_score, left_score_rect, ball_pos, right)
        
        #Left paddle
        control_paddle(screen, left_y, left_up, left_down)
        paddle(screen, left_x, left_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        score(screen, terminus, left_score, right_score_rect, ball_pos, left)

        #Ball
        ball(screen, right_x, left_x, right_y, left_y, ball_pos, vel)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False


        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()



