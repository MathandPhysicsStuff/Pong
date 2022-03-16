import pygame
import time
import math
import random
from math import sin, cos, fabs, pi
from CONSTANCE import *


def divider_line(screen):
    
    line_segment = 0
    while line_segment < HEIGHT:

        pygame.draw.line(screen, LIGHT_GRAY_2, (X_ORIGIN, line_segment), (X_ORIGIN, line_segment + 10), 2)

        line_segment += 20


def paddle(screen, x, y, width, height):

    paddle_rect = pygame.Rect(x, y[0], width, height)
    
    pygame.draw.rect(screen, LIGHT_GRAY, paddle_rect)


def control_paddle(screen, y, up, down):

    keys = pygame.key.get_pressed()

    if keys[up]:
        if y[0] > 0:
            y[0] -= MOVE
            
        else:
            y[0] += 0
           

    elif keys[down]:
        if y[0] + PADDLE_HEIGHT < HEIGHT:
            y[0] += MOVE
          
        else:
            y[0] += 0
    

def ball(screen, right_x, left_x, right_y, left_y, ball_pos, vel):

    r = 4
    theta = random.uniform(-pi, pi) 
 
    right_rect = pygame.Rect(right_x, right_y[0], PADDLE_WIDTH, PADDLE_HEIGHT)
    left_rect = pygame.Rect(left_x, left_y[0], PADDLE_WIDTH, PADDLE_HEIGHT)
    ball_rect = pygame.Rect(ball_pos[0], ball_pos[1], BALL, BALL)

    right_collide = pygame.Rect.colliderect(right_rect, ball_rect)
    left_collide = pygame.Rect.colliderect(left_rect, ball_rect)
    
    pygame.draw.rect(screen, LIGHT_GRAY, ball_rect)
   
    #Handling bounces off the front of the right paddle
    if -PADDLE_WIDTH < (right_x - BALL) - ball_pos[0] <= 0  and right_y[0] - BALL <= ball_pos[1] <= right_y[0] + PADDLE_HEIGHT:
        vel[0] *= -1
        ball_pos[0] += vel[0]

    #Handling bounces off the front of the left paddle
    elif 0 <= left_x + PADDLE_WIDTH - ball_pos[0] <= PADDLE_WIDTH and left_y[0] - BALL <= ball_pos[1] <= left_y[0] + PADDLE_HEIGHT:
        vel[0] *= -1
        ball_pos[0] += vel[0]

    else:
        ball_pos[0] += vel[0]
    #Handling bounces off the top and bottom of the right paddle
    if right_collide: 
        
        #Top
        if right_y[0] + PADDLE_HEIGHT >= ball_pos[1] + BALL >= right_y[0]:
            vel[1] *= -1.2
            ball_pos[1] += vel[1] - MOVE 
            
        #Bottom
        elif right_y[0] + PADDLE_HEIGHT >= ball_pos[1] >= right_y[0]:  
            vel[1] *= -1.2
            ball_pos[1] += vel[1] + MOVE

    #Handling bounces off the top and bottom of the left paddle
    if left_collide: 

        #Top
        if left_y[0] + PADDLE_HEIGHT >= ball_pos[1] + BALL >= left_y[0]:
            vel[1] *= -1.2
            ball_pos[1] += vel[1] - MOVE 
            
        #Bottom
        elif left_y[0] + PADDLE_HEIGHT >= ball_pos[1] >= left_y[0]:  
            vel[1] *= -1.2
            ball_pos[1] += vel[1] + MOVE

    #Wall bounce
    if ball_pos[1] + BALL >= HEIGHT:
        vel[1] *= -1
        ball_pos[1] += vel[1]
    
    elif ball_pos[1] <= 0:
        vel[1] *= -1
        ball_pos[1] += vel[1]

    else: 
        ball_pos[1] += vel[1]

    #Handling ball out of bounds
    if ball_pos[0] > WIDTH + BALL:
        time.sleep(2)
        vel[0] = r
        vel[1] = r * cos(theta)
        ball_pos[0] = X_ORIGIN - BALL // 2
        ball_pos[1] = random.randint(0, HEIGHT - BALL)
        time.sleep(2)

    elif ball_pos[0] + BALL < 0 - BALL:
        time.sleep(2)
        vel[0] = -r
        vel[1] = r * cos(theta)
        ball_pos[0] = X_ORIGIN - BALL // 2
        ball_pos[1] = random.randint(0, HEIGHT - BALL)
        time.sleep(2)


def score(screen, font, text, rect, ball_pos, trigger):
    
    ball_rect = pygame.Rect(ball_pos[0], ball_pos[1], BALL, BALL)
    right_side_rect = pygame.Rect(WIDTH, -50, 1, HEIGHT + 100)    
    left_side_rect = pygame.Rect(0, -50, 1, HEIGHT + 100)    

    display_score = font.render(str(int(text[0])), True, LIGHT_GRAY)
    
    if ball_rect.colliderect(right_side_rect) and trigger == "right":
        text[0] += 0.5

    if ball_rect.colliderect(left_side_rect) and trigger == "left":
        text[0] += 0.5

    screen.set_clip(rect)

    screen.blit(display_score, rect) 
    
    screen.set_clip(None)


def game_engine(screen):
    pass




















