
import pygame
import sys
import winsound
alpha= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
screen= pygame.display.set_mode((600,600))
balloonlist= []
pygame.init()
pygame.display.set_caption("Balloons")
from pygame.locals import *
import random
def show_text(msg, x, y, color):
    fontobj= pygame.font.SysFont("freesans", 32)
    msgobj= fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
class Balloon:
    def __init__(self):

        self.x= random.randint(20,140)
        self.y= 610
        self.width= 100
        self.height= 300
        self.thickness= 5
        
        self.image= pygame.image.load("Green_Balloon_sprite_005.png")
        self.letter= random.choice(alpha)
        self.image= pygame.transform.scale(self.image, (self.width, self.height))
        
    def draw(self):

        screen.blit(self.image, (self.x,self.y))
        show_text(self.letter, self.x+50, self.y+20, ((0,0,0)))

        
def gamerun():
    balloonlist.clear()
    balloonlist.append(Balloon())
    fps= pygame.time.Clock()
    score= 0
    time= 20
    out= 0
    game= True
    
    while game:
        screen.fill((154,192,205))
        myscore = 'Score: ' + str(score)
        show_text(myscore, 400, 100, (255,255,255))
        for b in balloonlist:
            b.draw()
            b.y-= 5
            if b.y == 100:
                balloonlist.append(Balloon())
            if b.y+300< 0:
                out += 1
                balloonlist.append(Balloon())
                balloonlist.remove(b)
                winsound.PlaySound('SystemAsterisk', winsound.SND_ASYNC)
            if out == 3:
                
                game= False
        fps.tick(time)
        
        pygame.display.update()  
        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()
                          
            elif event.type== KEYDOWN:
                
                keyLetter = pygame.key.name(event.key)
                
                for b in balloonlist:
                    if keyLetter== b.letter:
                        balloonlist.append(Balloon())
                        winsound.PlaySound('SystemExclamation', winsound.SND_ASYNC)
                        score += 1
                        show_text('Score :' + str(score), 400, 100, (255,255,255))
                        time+=4
                        balloonlist.remove(b)
                        break

    screen.fill((209,238,238))
    show_text('Game Over', 150,  60, (0, 0,0))
    show_text('Score:'+ str(score), 20,  20, (0,0,0))
    pygame.display.update()

            
#at beginning and end of game
def menu():
    firstword= "PLAY"
    secword= "QUIT"
    screen.fill((209,238,238))
    while True:

        pygame.draw.rect(screen, (205,140,149), (100, 200, 400, 50), 50)

        pygame.draw.rect(screen, (205,129,98), (100, 400, 400, 50), 50)

        show_text(firstword, 250,200, (255,250,205))
        
        show_text(secword, 250,400, (255,250,205))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type== QUIT:
                pygame.quit()
                sys.exit()
            elif event.type== MOUSEBUTTONDOWN:
                if event.button== 1:
                    print(event.pos)
                    x, y= event.pos
                    if x in range (70,530) and y in range (180,280):
                        
                        gamerun()
                    if x in range (70,530) and y in range (375,475):
                        pygame.quit()
                        sys.exit()
        
menu()
                        

            
