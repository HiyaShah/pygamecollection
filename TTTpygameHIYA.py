import pygame
import time
import random
from pygame.locals import *
pygame.init()
##screen= pygame.display.set_mode((1000,1000))
##pygame.display.set_caption('Ex1')
##s=True
##r=1
##color= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
###while True:
####    pygame.display.update()
####    if s:
####         r= r+1
####         screen.fill((0,0,0))
####    else:
####        r=r-1
####        screen.fill((0,0,0))
####
####    if r==150:
####        s=False
####    if r==1:
####        s=True
####        pygame.draw.circle(screen,color,(150,150),r)
####
##
##
##colors= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##def alt():
##    while True:
##           pygame.display.update()
##    
##           for x in range(0,1000,100):
##               a= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##               b= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##               a,b=b,a
##               for y in range(0,1000,100):
##                   a= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##
##                   b= (random.randint(0,255),random.randint(0,255),random.randint(0,255))
##
##                   a,b=b,a
##                   pygame.draw.rect(screen,a,(x,y,100,100))
##alt()
##               
##               
##   
##
def cross(x,y):
                pygame.draw.line(screen,(255,255,255), (x-100,y-100), (x+100,y+100),10)
                pygame.draw.line(screen,(255,255,255), (x+100,y-100), (x-100,y+100),10)

##while True:
##    pygame.display.update()
##    pygame.draw.line(screen,(255,255,255), (100,100), (400,400),10)
##    pygame.draw.line(screen,(255,255,255), (400,100), (100,400),10)
##    pygame.draw.line(screen,(255,255,255), (500,100), (900,400),10)
##    pygame.draw.line(screen,(255,255,255), (900,100), (500,400),10)
##    for event in pygame.event.get():
##        if event.type== QUIT:
##            pygame.quit()
##            exit()
##        
##        if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1:
##            print('mouse at:', event.pos)
##            x,y = event.pos
##            cross(x,y)
            
def rect():    
    var= True
    while True:
        time.sleep(.1)
        
        pygame.display.update()
        pygame.draw.rect(screen,(0,255,255), (100,100,300,400),10)
        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                exit()
            
        if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1:
            print('mouse at:', event.pos)
            x,y = event.pos
            if x<400 and x>100 and y<500 and y>100:

                if var== False:
                    screen.fill((0,0,0))
                    var= True
                elif var== True:
                    cross(x,y)
                    var= False

def drawX(x, y):
    pygame.draw.line(screen, (255,255,255), (x, y), (x+300,y+300), 10)
    pygame.draw.line(screen, (255,255,255), (x+300, y), (x,y+300), 10)

def drawO(x,y):
    pygame.draw.circle(screen,(255,255,255),(x,y),(150),1)

def rectcir():
    var= True
    
    while True:
        time.sleep(.1)
        
        pygame.draw.rect(screen,(0,255,255),(100,100,300,400),10)
        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                exit()
            
        if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1:
            print('mouse at:', event.pos)
            x,y = event.pos
            if x<400 and x>100 and y<500 and y>100:
                if var== False:
                    screen.fill((0,0,0))
                    var= True
                elif var== True:
                    pygame.draw.circle(screen,(4,234,255),(x,y),100,10)
                    var= False
def TTT():
    var= True
    player=     'x'
    dicti= dict()
    dicti= {0: "", 1: '',2:'',3:'',4:'',5:'',6:'',7:'',8:''}

    def wins(msg, x,y,color):
        fontobj= pygame.font.SysFont("freesans",75)
        msgobj= fontobj. render(msg,False,color)
        screen.blit(msgobj,(x,y))
    while True:
        pygame.draw.rect(screen, (7,237,255),(50,50,900,900),10)
        pygame.draw.rect(screen, (60,200,255),(50,50,300,300),10)
        pygame.draw.rect(screen, (30,200,255),(350,50,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(650,50,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(350,350,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(650,650,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(650,50,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(50,650,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(50,350,300,300),10)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1:
                x,y = event.pos
                x = x -50
                y = y-50
                spot= x//300+(y//300*3)
                print(x,y)
                print(spot)
                print(dicti)
                if player== 'x':
                    if dicti[spot] == '':
                        print("Player is X and spot is not present")
                        drawX((x//300*300)+50,(y//300*300)+50)
                        dicti[spot]= 'X'
                        player='o'
                elif player=='o':
                    if dicti[spot] == '':
                        print("Player is O and spot is not present")
                        drawO((x//300*300)+200,(y//300*300)+200)
                        dicti[spot]= 'O'
                        player= 'x'
        pygame.display.update()
        if dicti[0] == 'X' and dicti[1] == 'X' and dicti[2] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[3] == 'X' and dicti[6] == 'X' and dicti[0] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[3] == 'X' and dicti[4] == 'X' and dicti[5] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[6] == 'X' and dicti[7] == 'X' and dicti[8] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[1] == 'X' and dicti[4] == 'X' and dicti[7] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[2] == 'X' and dicti[5] == 'X' and dicti[8] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[2] == 'X' and dicti[4] == 'X' and dicti[6] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[0] == 'X' and dicti[4] == 'X' and dicti[8] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break


        if dicti[0] == 'O' and dicti[1] == 'O' and dicti[2] == 'O':
            wins('O wins!',450,450,(255,255,255))
            print('O wins')
            break
        if dicti[3] == 'O' and dicti[6] == 'O' and dicti[0] == 'O':
            wins('O wins!',450,450,(255,255,255))
            print('O wins')
            break
        if dicti[3] == 'O' and dicti[4] == 'O' and dicti[5] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[6] == 'O' and dicti[7] == 'O' and dicti[8] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[1] == 'O' and dicti[4] == 'O' and dicti[7] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[2] == 'O' and dicti[5] == 'O' and dicti[8] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[2] == 'O' and dicti[4] == 'O' and dicti[6] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[0] == 'O' and dicti[4] == 'O' and dicti[8] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if '' not in dicti.values():
            wins('Tie! Click to return to menu',100,450,(255,255,255))
    if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1:
        screen.fill((0,0,0))
        pygame.display.update()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(screen,(63,178,45),(100,200,300,300),1)
    show_text('Play',110,210,(255,255,255))
    pygame.draw.rect(screen,(255,255,255),(400,200,300,300),1)
    show_text('Quit',410,210,(63,178,45))
    if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1:
        x,y = event.pos
        if x >= 100 and x<=410 and y>=200 and y<=500:
            time.sleep(3)
            screen.fill((0,0,0))
            TTT()
        if x >= 410 and x<=710 and y>=200 and y<=500:
            print('Game Over')


def show_text(msg,x,y,color):
        fontobj= pygame.font.SysFont("freesans",150)
        msgobj= fontobj. render(msg,False,color)
        screen.blit(msgobj,(x,y))
screen= pygame.display.set_mode((1000,1000))
def menu():
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.draw.rect(screen,(63,178,45),(100,200,300,300),1)
        show_text('Play',110,210,(255,255,255))
        pygame.draw.rect(screen,(255,255,255),(400,200,300,300),1)
        show_text('Quit',410,210,(63,178,45))
        if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1:
            x,y = event.pos
            if x >= 100 and x<=410 and y>=200 and y<=500:
                time.sleep(3)
                screen.fill((0,0,0))
                time.sleep(1)
                TTT()
            if x >= 410 and x<=710 and y>=200 and y<=500:
                break
menu()

def TTT():
    var= True
    player=     'x'
    dicti= dict()
    dicti= {0: "", 1: '',2:'',3:'',4:'',5:'',6:'',7:'',8:''}

    def wins(msg, x,y,color):
        fontobj= pygame.font.SysFont("freesans",75)
        msgobj= fontobj. render(msg,False,color)
        screen.blit(msgobj,(x,y))
    while True:
        pygame.draw.rect(screen, (7,237,255),(50,50,900,900),10)
        pygame.draw.rect(screen, (60,200,255),(50,50,300,300),10)
        pygame.draw.rect(screen, (30,200,255),(350,50,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(650,50,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(350,350,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(650,650,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(650,50,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(50,650,300,300),10)
        pygame.draw.rect(screen, (90,200,255),(50,350,300,300),10)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1:
                x,y = event.pos
                x = x -50
                y = y-50
                spot= x//300+(y//300*3)
                print(x,y)
                print(spot)
                print(dicti)
                if player== 'x':
                    if dicti[spot] == '':
                        print("Player is X and spot is not present")
                        drawX((x//300*300)+50,(y//300*300)+50)
                        dicti[spot]= 'X'
                        player='o'
                elif player=='o':
                    if dicti[spot] == '':
                        print("Player is O and spot is not present")
                        drawO((x//300*300)+200,(y//300*300)+200)
                        dicti[spot]= 'O'
                        player= 'x'
        pygame.display.update()
        if dicti[0] == 'X' and dicti[1] == 'X' and dicti[2] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[3] == 'X' and dicti[6] == 'X' and dicti[0] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[3] == 'X' and dicti[4] == 'X' and dicti[5] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[6] == 'X' and dicti[7] == 'X' and dicti[8] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[1] == 'X' and dicti[4] == 'X' and dicti[7] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[2] == 'X' and dicti[5] == 'X' and dicti[8] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[2] == 'X' and dicti[4] == 'X' and dicti[6] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break
        if dicti[0] == 'X' and dicti[4] == 'X' and dicti[8] == 'X':
            print('X wins')
            wins('X wins!',450,450,(255,255,255))
            break


        if dicti[0] == 'O' and dicti[1] == 'O' and dicti[2] == 'O':
            wins('O wins!',450,450,(255,255,255))
            print('O wins')
            break
        if dicti[3] == 'O' and dicti[6] == 'O' and dicti[0] == 'O':
            wins('O wins!',450,450,(255,255,255))
            print('O wins')
            break
        if dicti[3] == 'O' and dicti[4] == 'O' and dicti[5] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[6] == 'O' and dicti[7] == 'O' and dicti[8] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[1] == 'O' and dicti[4] == 'O' and dicti[7] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[2] == 'O' and dicti[5] == 'O' and dicti[8] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[2] == 'O' and dicti[4] == 'O' and dicti[6] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if dicti[0] == 'O' and dicti[4] == 'O' and dicti[8] == 'O':
            print('O wins')
            wins('O wins!',450,450,(255,255,255))
            break
        if '' not in dicti.values():
            wins('Tie! Click to return to menu',450,450,(255,255,255))
    if event.type== pygame.MOUSEBUTTONDOWN and event.button== 1:
        pygame.display.update()
        screen.fill((0,0,0))
        menu()
