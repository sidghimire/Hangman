import pygame,sys
import pygame.freetype
import string
import random

words=['CAR','BUS','BABY','LAMBORGHINI']
choice=random.choice(words)
word_list=list(choice)
collection=[]
ans=[]
for empty in range(len(word_list)):
    ans.append("")
mouseX=None
mouseY=None
countOnce=0
btn=0
pygame.init()
size=width,height=800,700
black=0,0,0
screen=pygame.display.set_mode(size)
white=pygame.color.Color('#ffffff')
alphabet=[""]

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
                        print("Punish")
                    else:
                        break    
                    
        if event.type == pygame.QUIT:sys.exit()
    
 
    

    make_blank_space()
    display_text(black, 40, 340, 30, "Hangman")
    make_keyboard()
    
    pygame.display.flip()
    screen.fill(white)
pygame.time.wait(5000)