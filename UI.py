from matplotlib.pyplot import close, title
import pygame
from tkinter import *

SIZE=(1280,800)
pygame.init()
# COLOR
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
PURPLE=(128,0,128)
ORANGE=(255,165,0)
GREY=(128,128,128)
TURQUOISE=(64,224,208)

BG=pygame.image.load('Image/cold.jpg')
BG=pygame.transform.scale(BG,SIZE)



fontGame=pygame.font.SysFont('consolas',45)

class Button:

    def __init__(self,x,y,text,image):

        self.img=pygame.image.load(image)
        
        self.text=fontGame.render(text,True,YELLOW)
        self.clicked = False
        self.w=self.img.get_width()
        self.h=self.img.get_height()
        self.surface=pygame.Surface((self.w,self.h))
        self.surface.blit(self.img,(0,0))
        self.surface.blit(self.text,((self.w-self.text.get_width())//2,(self.h-self.text.get_height())//2))

        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        
        
    def draw(self, surface):

        #draw button on screen
        surface.blit(self.surface, (self.rect.x, self.rect.y))

    def hover(self):
        self.img=pygame.image.load("Image/choose_hover0.png")
    

class HomePage:
    def __init__(self):
        self.x=0
        self.y=0
        self.img=BG
        self.title=fontGame.render('PATH FINDING',True,YELLOW)
        self.w=self.img.get_width()
        self.h=self.img.get_height()
        

    def draw(self,WIN):
        WIN.blit(self.img,(int(self.x),int(self.y)))

        self.Title=Button(self.w//2-self.title.get_width()//2,50,'PathFinding','Image/bt1.jpg')
        
        self.Title.draw(WIN)
        

        self.A_Star=Button(self.w//2-200,self.h/7*2-50,'A_Star','Image/choose0.png')
        self.GBFS=Button(self.w//2-200,self.h/7*3-50,'GBFS','Image/choose0.png')
        self.BFS=Button(self.w//2-200,self.h/7*4-50,'BFS','Image/choose0.png')
        self.UCS=Button(self.w//2-200,self.h/7*5-50,'UCS','Image/choose0.png')
        self.IDS=Button(self.w//2-200,self.h/7*6-50,'IDS','Image/choose0.png')

        self.A_Star.draw(WIN)
        self.GBFS.draw(WIN)
        self.BFS.draw(WIN)
        self.UCS.draw(WIN)
        self.IDS.draw(WIN)


        
    def update(self):
        pygame.display.update()





     

