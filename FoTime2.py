import pygame, sys
import datetime
from pygame import *
from math import *
import time
import json

pygame.init()

WIDTH,HEIGHT = 1000,750

DISPLAYSURF = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("TIME")

icon_image = pygame.image.load("2.png")
icon_image = pygame.transform.scale(icon_image, (45, 45))
pygame.display.set_icon(icon_image)

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,128,0)

FPS = 60

now = datetime.datetime.now().timestamp()
class Clock():
    def __init__(self):
        self.ti = 0
        self.clock1 = 0
    def draw(self):
         times = datetime.datetime.now().timestamp()
         if now < times:
            self.ti = times - now
            self.clock1 += self.ti
            self.ti = 0


nownow = datetime.datetime.now().timestamp()
class Clock2():
     def __init__(self):
         save = 0
         self.tinow = 0
     def draw(self):
          global pause,save,nownow

          now33 = datetime.datetime.now().timestamp()
          store = now33 - nownow
          save = store
          if pause == True:
         
            nownow = datetime.datetime.now().timestamp()
   

          print(nownow,now33,save)
          hours = save //3600
          mins = (save //60)%60   
          secs = save %60    

          font = pygame.font.SysFont("consolas",40)
          font = font.render("<{}:{}:{}>".format(hours,mins,secs),True,WHITE)
          font_size = font.get_size()
          DISPLAYSURF.blit(font,(750,500))
def count_seconds():
    start_time = time.time()
    counting = True

    while True:
        

        # Draw the elapsed time on the screen
        
        print(start_time)
        
        pygame.display.flip()



class clockcon():
    def __init__(self):
        self.point = (570,580)
        self.radius = 90
    def draw(self,color,secs,mins):
        pygame.draw.circle(DISPLAYSURF,color,self.point,self.radius)
        pygame.draw.line(DISPLAYSURF,BLACK,self.point,(570+self.radius*sin((pi*secs)/30),580-self.radius*cos((pi*secs)/30)))
        pygame.draw.line(DISPLAYSURF,BLACK,self.point,(570+self.radius*sin((pi*mins)/30),580-self.radius*cos((pi*mins)/30)))

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

count = datetime.datetime(2024,2,4).timestamp() ################################### Start time
global n
n = True

try:
    with open("save.txt") as save:
         sav0 = json.load(save)
except:
    sav0 = 0
    print("No file save")


start_time = time.time()-sav0
counting = True
def GamePlay(cc):
    global counting,start_time,n
    while n ==True:
            elapsed_time = time.time() - start_time
            counting = False
            n = False
    
        
    
    font_pause2 = pygame.font.SysFont("consolas",50)
    font_pause2 = font_pause2.render("<Work>",True,WHITE)
    font_size = font_pause2.get_size()

    font_pause = pygame.font.SysFont("consolas",50)
    font_pause = font_pause.render("<Working...>",True,GREEN)
    font_size_pause = font_pause.get_size()
    x = 650
    y = 350
    box_pause = pygame.Rect(x,y,font_size_pause[0],font_size_pause[1]) 

    while True:
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 with open("save.txt","w") as save:
                    if counting:
                        # Stop counting and save the elapsed time
                        elapsed_time = time.time() - start_time
                    json.dump(elapsed_time,save)
                 pygame.quit()
                 sys.exit()
             if event.type == pygame.MOUSEBUTTONDOWN:
                if box_pause.collidepoint(event.pos): 
                    if counting:
                        # Stop counting and save the elapsed time
                        elapsed_time = time.time() - start_time
                        counting = False
                    else:
                        # Resume counting from where it left off
                        start_time = time.time() - elapsed_time
                        counting = True       

        now3 = datetime.datetime.now().date()
        time1 = datetime.datetime.now().time()
        times = datetime.datetime.now().timestamp()
        now5 = datetime.datetime(int("{}".format(now3.year)),3,30).date()
        ye = now5 - now3
        age = now3.year - birth.year - ye.days/365

        new = datetime.datetime(int("{}".format(now3.year+1)),1,1)
        new2 = new.timestamp()

        times2 = datetime.datetime(int("{}".format(now3.year+1)),1,1).timestamp()
        times3 = datetime.datetime(int("{}".format(now3.year)),1,1).timestamp()
        times4 = times2 - times3

        seconds = times - birth2
        timeleft = int(round((new2 - times),3))
        rate = round((1-timeleft/times4)*100)

        font = pygame.font.SysFont("consolas",40)
        font = font.render("<{}>({}%)to<{}>".format(timeleft,rate,now3.year+1),True,WHITE)
        font_size = font.get_size()

        
        seconds2 = round(seconds,2)
        minutes = round(seconds/60,3)
        hours = round(seconds/(60*60),5)
        days = round(seconds/(60*60*24),3)
        years = round(age,3)
        
        DISPLAYSURF.fill(BLACK)
        
        FONT(years,WHITE,0,-240)
        FONT(days,WHITE,200,-160)
   
        DISPLAYSURF.blit(font,( (WIDTH-font_size[0])/2 -200,(HEIGHT-font_size[1])/2 -160 ) )

        FONT2(hours,WHITE,50,470)
        FONT2(minutes,WHITE,50,545)
        FONT2(seconds2,WHITE,50,620)

        FONT("Tan Tan ",WHITE,240,-240)
        FONT("Days",WHITE,380,-160)
        FONT("33ZX",WHITE,-240,-240)
        FONT("Flow of time",WHITE,0,-290,20)

        FONT("1000H to Expert, 10000H to Master",WHITE,0,340,20)

        sd = round((times - count)/(3600*24),2)
        FONT2(f"Day {sd}",WHITE,680,270) ###


        ######################################
        if counting == True:
            DISPLAYSURF.blit(font_pause,(box_pause.x,box_pause.y))
        else:
            DISPLAYSURF.blit(font_pause2,(box_pause.x,box_pause.y))
        ##########
        if counting:
            save = time.time() - start_time
            text = render(save)
        else:
            text = render(elapsed_time)
 

        DISPLAYSURF.blit(text, (750, 500))
        ################################
            
        FONT(now3,WHITE,-80,-80,80)
        FONT2(time1,WHITE,100,360,60)
        
        cc.draw(WHITE,seconds2,minutes)
        

        pygame.display.update()
        pygame.time.Clock().tick(FPS)

def render(ti):
    font22 = pygame.font.SysFont("consolas", 36)
    hours = round(ti //3600)
    mins = round((ti //60)%60)   
    secs = round(ti %60) 
    tt = int((ti % 1) * 100) 
    text = font22.render("<{}:{}:{}:{}>".format(hours,mins,secs,tt),True,WHITE)
    return text

def main():
    cc = clockcon()
    while True:
        GamePlay(cc)
      
     

if __name__ == "__main__":
    main()

