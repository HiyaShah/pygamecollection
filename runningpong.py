import pygame
import time
import random

pygame.init()
from pygame.locals import *

from createpong import paddle,ball,scores

screen= pygame.display.set_mode((600,600))
paddle1= paddle(0,200,(31,245,250))
paddle2= paddle(570,200,(31,250,145))
xchange= 1
ychange=1
leftc= 0
rightc= 0
score= 0
score1= scores(0, 20, 'Score Left: '+str(score),40,40)
score2= scores(2,20,'Score Right: '+str(score), 260,40)
ball1= ball(300,300,random.randint(1,5), random.randint(1,5))

while True:

    pygame.display.update()
    screen.fill((0,0,0))
    paddle1.dpaddle()
    
    paddle2.dpaddle()

    ball1.drawb(300,300)
    
    

    paddle1.move(leftc)

    paddle2.move(rightc)
    
    for event in pygame.event.get():
        if event.type== KEYDOWN:


            if event.key== K_DOWN:
                rightc= 1
            elif event.key== K_UP:
                rightc= -1
            elif event.key== K_w:
                leftc= -1
            elif event.key== K_s:
                leftc= 1
    ball1.moving()
    if score1.score == 21:
        screen.fill((0,0,0))
        score1.show_text(40, 'Left Wins!!',40,40)
        time.sleep(3)
        break
    elif score2.score== 21:
        screen.fill((0,0,0))
        score1.show_text(40, 'Right Wins!!',40,40)
        time.sleep(3)
        break
        
    score1.show_text(20, 'Score Left: '+str(score1.score),40,40)
    score2.show_text(20,'Score Right: '+str(score2.score), 260,40)
    if ball1.x-30 <= 30 and ball1.y in range(paddle1.ypong, paddle1.ypong + 200):
            ball1.xbchange= random.randint(1,5)
            score1.score+= 1
    if ball1.x+30 >= 570 and ball1.y in range(paddle2.ypong, paddle2.ypong+200):
            ball1.xbchange= random.randint(-5,-1)
            score2.score+= 1
