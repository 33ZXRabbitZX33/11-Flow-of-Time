import pygame, sys
import datetime
from pygame import *
from math import *

pygame.init()

WIDTH,HEIGHT = 800,700

DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIME")

BLACK = (0,0,0)
WHITE = (255,255,255)

FPS = 60

now = datetime.datetime.now().timestamp()
class Clock():
    def __init__(self):
        self.ti = 0
        self.clock1 = 0
    def draw(self):
         now2 = datetime.datetime.now().timestamp()
         if now < now2:
            self.ti = now2 - now
            self.clock1 += self.ti
            self.ti = 0

class clockcon():
    def __init__(self):
        self.point = (600,580)
        self.radius = 90
    def draw(self,color,secs,mins):
        pygame.draw.circle(DISPLAYSURF,color,self.point,self.radius)
        pygame.draw.line(DISPLAYSURF,BLACK,self.point,(600+self.radius*sin((pi*secs)/30),580-self.radius*cos((pi*secs)/30)))
        pygame.draw.line(DISPLAYSURF,BLACK,self.point,(600+self.radius*sin((pi*mins)/30),580-self.radius*cos((pi*mins)/30)))

def FONT(ann,color,x,y,size=50):
     font = pygame.font.SysFont("consolas",size)
     font = font.render("{}".format(ann),True,color)
     font_size = font.get_size()
     DISPLAYSURF.blit(font,((WIDTH-font_size[0])/2 +x,(HEIGHT-font_size[1])/2 +y ))

def FONT2(ann,color,x,y,size=50):
     font = pygame.font.SysFont("consolas",size)
     font = font.render("{}".format(ann),True,color)
     font_size = font.get_size()
     DISPLAYSURF.blit(font,(x,y))

birth = datetime.datetime(2001,3,30)
birth2 = birth.timestamp()

new = datetime.datetime(2024,1,1)
new2 = new.timestamp()

def GamePlay(cc):
     
  
     while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()

        now3 = datetime.datetime.now().date()
        now4 = datetime.datetime.now().time()
        now2 = datetime.datetime.now().timestamp()

        check = now2 + 53*24*3600
        check2 = datetime.datetime.fromtimestamp(check)
   

        seconds = now2 - birth2
        new3 = int(round((new2 - now2),3))

        font = pygame.font.SysFont("consolas",40)
        font = font.render("<{}>to<2024>".format(new3),True,WHITE)
        font_size = font.get_size()

        seconds2 = round(seconds,1)
        minutes = round(seconds/60,3)
        hours = round(seconds/(60*60),5)
        days = round(seconds/(60*60*24),3)
        years = round(seconds/(60*60*24*365),3)

        DISPLAYSURF.fill(BLACK)
       
        FONT(years,WHITE,0,-240)
        FONT(days,WHITE,160,-160)
   
        DISPLAYSURF.blit(font,( (WIDTH-font_size[0])/2 -200,(HEIGHT-font_size[1])/2 -160 ) )

        FONT2(hours,WHITE,70,470)
        FONT2(minutes,WHITE,50,550)
        FONT2(seconds2,WHITE,80,620)

        FONT("Tan Tan",WHITE,240,-240)
        FONT("Days",WHITE,340,-160)
        FONT("33ZX",WHITE,-240,-240)
        FONT("Flow of time",WHITE,-45,-290,20)


        FONT(now3,WHITE,-80,-80,80)
        FONT(now4,WHITE,0,45,60)
        
        cc.draw(WHITE,seconds2,minutes)
        

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

def main():
    cc = clockcon()
    while True:
        GamePlay(cc)
      
     

if __name__ == "__main__":
    main()

