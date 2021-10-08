import pygame,sys
import pygame.freetype
import string
import random

words=['CAR','BUS','BABY','LAMBORGHINI','LOVELY','PUPPY','CUTE','HUG','SKY','DOG','CAT','DOUBLE']
choice=random.choice(words)
word_list=list(choice)
collection=[]
ans=[]
for empty in range(len(word_list)):
    ans.append("")
mouseX=None
mouseY=None
countOnce=0
mistake=0
won=0
btn=0
pygame.init()
size=width,height=800,700
black=0,0,0
screen=pygame.display.set_mode(size)
white=pygame.color.Color('#ffffff')
alphabet=[""]


def draw_hanger(x,y):
    pygame.draw.rect(screen, black,(x,y,10,200))
    pygame.draw.rect(screen, black,(x,y,100,10))
    pygame.draw.rect(screen, black,(x+100,y,10,40))

def make_mistake(x,y):
    if(mistake >= 1):
        pygame.draw.circle(screen, black, (x+5,y+25), 30)
        if(mistake >= 2):
            pygame.draw.rect(screen, black,(x+5,y+40,10,90))
            if(mistake >= 3):
                pygame.draw.line(screen, black, (x+10,y+60), (x-35,y+100),width=10)
                if(mistake >= 4):
                    pygame.draw.line(screen, black, (x+10,y+60), (x+45,y+100),width=10)
                    if(mistake >= 5):
                        pygame.draw.line(screen, black, (x+10,y+120), (x-35,y+180),width=10)
                        if(mistake >= 6):
                            pygame.draw.line(screen, black, (x+10,y+120), (x+45,y+180),width=10)
                            display_text(black, 40, 340, 350, "Game Over")
    

def getAlphabet():
    for x in range(ord('A'),ord('Z')+1):
        alphabet.append(chr(x))
    

def checkContain(a,b,x,y,btn):
    if((x>a and a+50>x) and (y>b and b+50>y)):
        return btn

def display_text(color,size,x,y,words):
    font=pygame.font.Font(None,size)
    text=font.render(words,True,color)
    screen.blit(text,(x,y))
    
def make_keyboard():
    global countOnce
    count=0
    initX=40
    initY=500
    font=pygame.font.Font(None,50)
    for x in range(ord('A'),ord('J')+1):
        count+=1
        if(countOnce==0):
            box=[initX,initY,count]
            collection.append(box)
        pygame.draw.rect(screen,black,(initX,initY,50,50))
        text=font.render(chr(x),True,white)
        screen.blit(text,(initX+15,initY+10))
        initX+=75
    initX=40
    initY+=60 
    for x in range(ord('K'),ord('T')+1):
        count+=1
        if(countOnce==0):
            box=[initX,initY,count]
            collection.append(box)
        pygame.draw.rect(screen,black,(initX,initY,50,50))
        text=font.render(chr(x),True,white)
        screen.blit(text,(initX+15,initY+10))
        initX+=75
    initX=40
    initX+=150
    initY+=60 
    for x in range(ord('U'),ord('Z')+1):
        count+=1
        if(countOnce==0):
            box=[initX,initY,count]
            collection.append(box)
        pygame.draw.rect(screen,black,(initX,initY,50,50))
        text=font.render(chr(x),True,white)
        screen.blit(text,(initX+15,initY+10))
        initX+=75
    countOnce=1
    
def make_blank_space():
    initY=400
    if(len(choice)<=5):
        initX=350
    elif(len(choice)<=11):
        initX=100
    elif(len(choice)<=16):
        initX=50
    font=pygame.font.Font(None,80)
    for x in range(len(ans)):
        if(ans[x]==""):
            text=font.render("_",True,black) 
        else:
            text=font.render(ans[x],True,black)
        screen.blit(text,(initX,initY))   
        initX+=50
getAlphabet()     
#Main        
while 1:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if("" not in ans):
                mistake=6
            if(mistake>=6 or won==1):
                exit()
            mouseX= pygame.mouse.get_pos()[0]
            mouseY= pygame.mouse.get_pos()[1]
            for i in range(26):
                location=[]
                count=0
                btn=checkContain(collection[i][0],collection[i][1],mouseX,mouseY,collection[i][2])
                if(btn!=None):
                    for j in range(len(word_list)):
                        if(alphabet[btn]==word_list[j]):
                            ans[j]=word_list[j]
                            count=count+1
                    if count==0:
                        mistake+=1;
                    else:
                        if("" not in ans):
                            won=1
                        break    
        if event.type == pygame.QUIT:sys.exit()
    make_blank_space()
    display_text(black, 40, 340, 30, "Hangman")
    make_keyboard()
    make_mistake(400,140)
    draw_hanger(300,100)
    if(won==1):
        display_text(black, 40, 340, 350, "You Win")
    pygame.display.flip()
    screen.fill(white)
pygame.time.wait(5000)