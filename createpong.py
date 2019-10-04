import pygame
import time
import random

xbchange= random.randint(1,5)
ybchange= random.randint(-5,-1)
rightc= 0
pygame.init()
from pygame.locals import *
screen= pygame.display.set_mode((600,600))


class paddle:
    def __init__(self, xpong,ypong,color):
        self.xpong= xpong
        self.ypong= ypong
        self.color= color

    def dpaddle(self):
        pygame.draw.rect(screen, self.color, (self.xpong, self.ypong,30,200))
    def move(self,ychange):
        self.ypong+=ychange
        
        if self.ypong>= 400:
            self.ypong=400
        if self.ypong <=0:
            self.ypong=0
               
class scores:
    def __init__(self,score,size,msg,xmsg,ymsg):
        self.score= score
        self.size= size
        self.msg= msg
        self.xmsg= xmsg
        self.ymsg= ymsg
    def show_text(self,size, msg, xmsg, ymsg):
      fontobj= pygame.font.SysFont('freesans', size)
      msgobj= fontobj.render(msg,False,(255,255,255))
      screen.blit(msgobj,(xmsg,ymsg))    
        
        
class ball:
    def __init__(self,x,y,xbchange,ybchange):
        self.x= x
        self.y= y
        self.xbchange= xbchange
        self.ybchange= ybchange
        
    def drawb(self,x,y):
        pygame.draw.circle(screen,(51,161,201),(self.x,self.y),30)
    def moving(self):
        self.x+= self.xbchange
        self.y+= self.ybchange
        if self.x>= 570:
            self.xbchange= - random.randint(1,5)
        elif self.x<=30:
            self.xbchange=  random.randint(1,5)
        elif self.y>=570:
            self.ybchange= - random.randint(1,5)
        elif self.y<= 30:
            self.ybchange=random.randint(1,5)
