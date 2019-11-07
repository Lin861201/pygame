#程式名稱：animation-01.py
import pygame,random,threading
import os,time
from pygame.locals import *

#初始化
pygame.init()
pygame.mixer.init(22050,-16,1,512)

#螢幕大小and幀數
WIN_WIDTH, WIN_HEIGHT = 1280, 720
FRAME_PER_SECONDS = 110 #最大幀數
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("哎呀快要滑倒啦")
img_base_path = os.getcwd() + '/images/'
sound_base_path = os.getcwd() + '/sounds/'

#狀態宣告區
run = True #遊戲開始
screen1,screen2,screen3,switch = True,False,False,True #畫面切換
left,right=True,False #初始為右邊的圖像
x,y = 500,600 #人物座標
speed = 10 #人物速度
objspeed = 5 #落下速度
now = 0.0
counter = 0
score = 0
combo = 0
font = pygame.font.Font("fonts/1900805.ttf",72)
font1 = pygame.font.Font("fonts/1900805.ttf",24)
chinese = pygame.font.Font("fonts/KTEGAKI.ttf",24)
chinese3 = pygame.font.Font("fonts/KTEGAKI.ttf",96)

#動畫區
click = [       pygame.image.load(img_base_path + 'taiko-hit300k-0.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-1.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-2.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-3.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-4.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-5.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-6.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-7.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-8.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-9.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-10.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-11.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-12.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-13.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-14.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-15.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-16.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-17.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-18.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-19.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-20.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-21.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-22.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-23.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-24.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-25.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-26.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-27.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-28.png').convert_alpha(),
                pygame.image.load(img_base_path + 'taiko-hit300k-29.png').convert_alpha()]

obj1 = [        pygame.image.load(img_base_path + 'hit100-0.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-1.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-2.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-3.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-4.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-5.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-6.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-7.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-8.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-9.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-10.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-11.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-12.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-13.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-14.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-15.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-16.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-17.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-18.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-19.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-20.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-21.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-22.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-23.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-24.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-25.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-26.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-27.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-28.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit100-29.png').convert_alpha()]

obj2 = [        pygame.image.load(img_base_path + 'hit50-0.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-1.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-2.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-3.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-4.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-5.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-6.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-7.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-8.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-9.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-10.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-11.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-12.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-13.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-14.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-15.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-16.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-17.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-18.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-19.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-20.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-21.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-22.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-23.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-24.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-25.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-26.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-27.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-28.png').convert_alpha(),
                pygame.image.load(img_base_path + 'hit50-29.png').convert_alpha()]

obj3 = [] #直接引入click來用

#調整obj大小
for i in range(30):
    obj1[i] = pygame.transform.scale(obj1[i],(400,400)).convert_alpha()
    obj2[i] = pygame.transform.scale(obj2[i],(400,400)).convert_alpha()
    obj3.append(pygame.transform.scale(click[i],(400,400)).convert_alpha())

#角色
catchleft = pygame.image.load(img_base_path + 'catchleft.png').convert_alpha()
catchleft = pygame.transform.scale(catchleft,(193,208)).convert_alpha()
catchright = pygame.image.load(img_base_path + 'catchright.png').convert_alpha()
catchright = pygame.transform.scale(catchright,(193,208)).convert_alpha()

#背景
bg = pygame.image.load(img_base_path + 'menu-background.jpg').convert_alpha()
bg = pygame.transform.scale(bg,(WIN_WIDTH,WIN_HEIGHT)).convert_alpha()
bg1 = pygame.image.load(img_base_path + 'bg1.jpg').convert_alpha()
bg1 = pygame.transform.scale(bg1,(WIN_WIDTH,WIN_HEIGHT)).convert_alpha()
bg2 = pygame.image.load(img_base_path + 'bg2.jpg').convert_alpha()
bg2 = pygame.transform.scale(bg2,(WIN_WIDTH,WIN_HEIGHT)).convert_alpha()
start = pygame.image.load(img_base_path + 'start.png').convert_alpha()
end = pygame.image.load(img_base_path + 'end.png').convert_alpha()
end = pygame.transform.scale(end,(104,65)).convert_alpha()
rankingpanel = pygame.image.load(img_base_path + 'ranking-panel old.png').convert_alpha()
rank = pygame.image.load(img_base_path + 'ranking-XH.png').convert_alpha()
rank = pygame.transform.scale(rank,(185,222)).convert_alpha()
retry = pygame.image.load(img_base_path + 'pause-retry.png').convert_alpha()
clock = pygame.time.Clock()
menuhit = pygame.mixer.Sound(sound_base_path + 'menuhit.wav')
objhit = pygame.mixer.Sound(sound_base_path + 'normal-hitwhistle.wav')
intro1 = chinese.render('Game introduce:' +'',True,(0,0,0))
intro2 = chinese.render('以左右移動人物',True,(0,0,0))
intro3 = chinese.render('接住落下的方塊',True,(0,0,0))
intro4 = chinese.render('享受愉快的節奏!',True,(0,0,0))
#人物物件
class Mysprite(pygame.sprite.Sprite):
    def __init__(self,target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
    def load(self,filename):
        self.image = filename
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    def update(self,left,right,speed):
        if left:
            if self.rect.centerx > 100:
                self.rect.centerx -= speed
        if right:
            if self.rect.centerx < 1200:
                self.rect.centerx += speed
#碰撞物
class obj(pygame.sprite.Sprite):
    def __init__(self,target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.count = 0
        self.burst = False
        self.select = 1
    def load(self,filename):
        if filename == 1:
            self.image = obj1[0]
            self.select = 1
        elif filename == 2:
            self.image = obj2[0]
            self.select = 2
        elif filename == 3:
            self.image = obj3[0]
            self.select = 3
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(500,700)
        #self.rect.centerx = 500 #測試用
        self.rect.centery = -20
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        global combo
        if self.burst == False and self.rect.centery < 800:
            self.rect.centery += objspeed
        elif self.burst == True and self.count < 29:
            if self.count == 0:
                #objhit.play()
                combo += 1
            self.count+=1
            if self.select == 1:
                self.image = obj1[self.count]
            elif self.select == 2:
                self.image = obj2[self.count]
            elif self.select == 3:
                self.image = obj3[self.count]
        elif self.rect.centery >= 800:
            combo = 0
            group1.remove(self)
        else:
            group1.remove(self)
                
#精靈初始化        
character = Mysprite(win)
group = pygame.sprite.Group()
group1 = pygame.sprite.Group()
fall = []
for i in range(500):
    fall.append(obj(win))
    fall[i].load((i % 3) + 1)
#渲染
def redrawGameWindow():
    global clickanimation,screen1,screen2,switch,now
    fps = font1.render('FPS:' + str(int(clock.get_fps())),True,(0,0,0))
    if screen1:
        #切換畫面
        if switch:
            switch = False
            pygame.mixer.music.load(sound_base_path + 'bgm.mp3')
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
            
        win.blit(bg, (0, 0))
        win.blit(fps,(1150,0))
        win.blit(intro1,(125,100))
        win.blit(intro2,(125,150))
        win.blit(intro3,(125,200))
        win.blit(intro4,(125,250))
        win.blit(start,(1050,500))
        win.blit(end,(10,585))
        #按鍵動畫
        if clickanimation:
            for i in range(30):
                clock.tick(60)
                clickfps = font1.render('FPS:' + str(int(clock.get_fps())),True,(0,0,0))
                win.blit(bg, (0, 0))
                win.blit(clickfps,(1150,0))
                win.blit(intro1,(125,100))
                win.blit(intro2,(125,150))
                win.blit(intro3,(125,200))
                win.blit(intro4,(125,250))
                win.blit(start,(1050,500))
                win.blit(end,(10,585))
                win.blit(click[i % 30],(pygame.mouse.get_pos()[0] - 400,pygame.mouse.get_pos()[1] - 400))
                pygame.display.update()
        pygame.display.update()
    if screen2:
        if switch:
            switch = False
            pygame.mixer.music.load(sound_base_path + 'audio.mp3')
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            now = time.time() #音樂撥放時開始計時
            t.start()
            #t1.start()
            character.load(catchright)
            character.rect.centerx = x
            character.rect.centery = y
            group.add(character)
        if left:
            character.image = catchleft
        if right:
            character.image = catchright
        group.update(left,right,speed)
        group1.update()
        text = font.render('SCORE:' + str(score),True,(0,0,0))
        text1 = font.render('COMBO:' + str(combo),True,(0,0,0))
        win.blit(bg1,(0,0))
        win.blit(text,(25,25)) #繪製分數
        win.blit(text1,(25,100))
        win.blit(fps,(1150,0))
        group.draw(win)
        group1.draw(win)
        pygame.display.update()
    if screen3:
        if switch:
            switch = False
            pygame.mixer.music.load(sound_base_path + 'transfer.mp3')
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play()
        printscore = chinese3.render(str(score),True,(100,100,100))
        printcombo = chinese3.render(str(combo),True,(100,100,100))
        songname = chinese.render('Reona - Niji no Kanata ni',True,(225,225,225))
        win.blit(bg2,(0,0))
        win.blit(fps,(1150,0))
        win.blit(rankingpanel,(0,0))
        win.blit(printscore,(75,70))
        win.blit(printcombo,(75,450))
        win.blit(rank,(405,415))
        win.blit(songname,(73,640))
        win.blit(retry,(1150,450))
        if clickanimation:
            for i in range(30):
                clock.tick(60)
                clickfps = font1.render('FPS:' + str(int(clock.get_fps())),True,(0,0,0))
                win.blit(bg2,(0,0))
                win.blit(clickfps,(1150,0))
                win.blit(rankingpanel,(0,0))
                win.blit(printscore,(75,70))
                win.blit(printcombo,(75,450))
                win.blit(rank,(405,415))
                win.blit(songname,(73,640))
                win.blit(retry,(1150,450))
                win.blit(click[i % 30],(pygame.mouse.get_pos()[0] - 400,pygame.mouse.get_pos()[1] - 400))
                pygame.display.update()
        pygame.display.update()
#碰撞偵測
def detectCollisions(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x2+w2>=x1>=x2 and y2+h2>=y1>=y2):
        return True 
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1>=y2): 
        return True 
    elif (x2+w2>=x1>=x2 and y2+h2>=y1+h1>=y2): 
        return True 
    elif (x2+w2>=x1+w1>=x2 and y2+h2>=y1+h1>=y2): 
        return True 
    else:
        return False
#產生物件
def produce(a):
    global now, counter,screen1,screen2,screen3,switch,t
    while True:
        if a ==[] and len(group1) == 0:
            screen1 = False
            screen2 = False
            screen3 = True
            switch = True
            pygame.mixer.music.fadeout(4000)
            break
        tmp = time.time() - now
        if a != [] and tmp >= a[0]:
            group1.add(fall[counter])
            del a[0]
            counter += 1
arr = [8.378,8.69,9.007,9.608,9.92,10.249,10.88,11.196,11.821,12.446,
13.375,13.687,14,14.604,14.916,15.229,15.854,16.166,16.789,17.401,18.356,
18.685,18.93,19.59,19.909,20.228,20.846,21.134,21.463,21.772,22.091,
22.423,23.401,23.72,23.995,24.626,24.99,25.273,25.903,26.219,26.377,
26.523,26.826,27.103,27.432,27.735,28.341,28.644,28.947,29.256,29.565,
29.874,30.184,30.802,31.146,31.42,31.778,32.097,32.416,33.054,33.334,
33.654,33.973,34.586,34.892,34.586,34.892,35.207,35.81,36.116,36.422,
36.736,37.05,37.364,37.678,38.306,38.62,38.778,38.935,39.226,39.517,
39.823,40.129,40.747,41.056,41.211,41.365,41.671,41.977,42.283,43.201,
43.507,43.813,44.116,44.419,44.734,45.025,45.328,45.631,45.934,46.085,
46.237,46.543,46.849,47.138,47.444,48.056,48.685,49.612,49.922,50.231,
50.849,51.159,51.465,52.103,52.409,52.728,53.606,54.536,54.842,55.913,
57.602,57.921,58.241,58.56,58.864,59.129,59.518,59.853,60.119,60.445,
60.757,60.996,61.323,61.635,61.91,62.519,62.823,63.128,63.28,63.432,
63.742,64.051,64.36,64.67,64.979,65.279,65.729,65.881,66.214,66.547,
66.814,67.396,67.693,68.026,68.305,68.456,68.608,68.911,69.248,69.554,
69.86,70.166,70.472,70.728,71.06,71.339,71.679,72.02,72.292,72.601,
72.91,73.141,73.744,74.045,74.347,74.648,74.95,75.251,75.553,75.856,
76.159,76.462,77.068,77.371,77.674,77.825,77.977,78.277,78.577,78.877,
79.477,79.777,80.077,80.227,80.377,80.683,80.989,81.295,81.907,82.06,
82.366,82.519,82.672,82.825,83.477,83.777,84.065,84.365,84.665,84.965,
85.249,85.552,85.855,86.158,86.764,87.067,87.37,87.682,87.994,88.316,
88.628,88.941,89.253,89.553,89.882,90.191,90.513,90.836,91.14,91.457,
91.774,92.409,92.764,93.37,93.673,93.976,94.279,94.57,94.897,95.206,
95.515,95.83,96.146,96.429,96.712,97.006,97.3,97.615,97.931,98.247,
98.547,98.847,99.127,99.421,99.715,100.037,100.346,101.908,102.217,
102.363,102.509,102.809,103.108,103.406,103.719,104.37,105,105.31,
105.623,105.96,106.619,106.904,107.213,107.498,107.808,108.118,108.438,
108.738,109.368,109.678,109.829,109.981,110.292,110.602,110.912,111.219,
111.539,111.84,112.157,112.461,113.086,113.398,113.711,114.336,114.676,
114.973,115.288,115.604,115.92,116.236,116.551,116.836,117.481,118.087,
118.39,118.541,118.693,119.299]
t = threading.Thread(target=produce,args=(arr,))
'''
def down():
    while True:
        clock.tick(60)
        group1.update()
t1 = threading.Thread(target=down)
'''
while run:
    clock.tick(FRAME_PER_SECONDS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    mousep = pygame.mouse.get_pressed()
    #開始畫面判斷
    if mousep[0] and screen1 == True: 
        menuhit.play()
        clickanimation = True
        if detectCollisions(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],8,8,10,585,104,65):
            pygame.mixer.music.fadeout(2000)
            run = False
        elif detectCollisions(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],8,8,1050,500,208,134):
            for i in range(30):
                clickfps = font1.render('FPS:' + str(int(clock.get_fps())),True,(0,0,0))
                clock.tick(60)
                win.blit(bg, (0, 0))
                win.blit(clickfps,(1150,0))
                win.blit(intro1,(125,100))
                win.blit(intro2,(125,150))
                win.blit(intro3,(125,200))
                win.blit(intro4,(125,250))
                win.blit(start,(1050,500))
                win.blit(end,(10,585))
                win.blit(click[i % 30],(pygame.mouse.get_pos()[0] - 400,pygame.mouse.get_pos()[1] - 400))
                pygame.display.update()
            screen1 = False
            screen2 = True
            screen3 = False
            switch = True
            pygame.mixer.music.fadeout(2000)
    #遊戲中
    elif screen2 == True:
        if keys[pygame.K_LEFT]:
            left = True
            right = False
        elif keys[pygame.K_RIGHT]:
            left = False
            right = True
        else:
            left = False
            right = False
        tmp = pygame.sprite.spritecollide(character,group1,False,pygame.sprite.collide_mask)
        if tmp:
            for i in tmp:
                score += 100
                i.burst = True
    elif screen3 == True and mousep[0]:
        clickanimation = True
        menuhit.play()
        if detectCollisions(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],8,8,1150,450,83,85):
            run = False
            pygame.mixer.music.fadeout(2000)
    else:
        clickanimation = False
    redrawGameWindow()        
pygame.quit()