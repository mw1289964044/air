# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 11:04:01 2021

@author: Administrator
"""

import pygame
import sys
import math
import random

#初始界面
pygame.init()
screen_width=1920
screen_height=1080
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('迷失飞机')
icon=pygame.image.load('ufo.jpg')
pygame.display.set_icon(icon)
bgImg=pygame.image.load('331.png')
#立绘
lihuiImg=pygame.image.load('lihui@0.1x@0.75x.png')
lihuiX=2210
lihuiY=1616
#飞机
playerImg=pygame.image.load('player5.png')
playerX=909
playerY=800
playerXStep = 0
playerYStep = 0
HP = 1000
number_of_bullets = 100
S=1#分数加参数
R=5000#奖励分数
#boss
B=1
boss=pygame.image.load('boss.png')
bossX=909
bossY=200
bossXstep=3
bossYstep=0
bossHP = 5000
#cpu时间
time_eplased = 0
now = 0
#背景音乐
bgm = 'bg.flac'
#分数
score = 1
font = pygame.font.SysFont('Calibri',32)#?
def show_score():
    text = f"score:{score}"
    score_render = font.render(text,True,(0,255,255))
    screen.blit(score_render,(1550,820))
def show_HP():
    text = f"HP:{HP}"
    HP_render = font.render(text,True,(0,255,255))
    screen.blit(HP_render,(1615,900))
def show_number_of_bullets():
    text = f"number of bullets:{number_of_bullets}"
    number_of_bullets_render = font.render(text,True,(0,255,255))
    screen.blit(number_of_bullets_render,(1420,860))   
def show_bossHP():
    text = f"bossHP:{bossHP}"
    bossHP_render = font.render(text,True,(0,255,255))
    screen.blit(bossHP_render,(1540,780)) 

def score_time():
    global score,HP,S,R
    if HP > 0:
        if time_eplased > 0:
            if now%10 == 0:
                score += S
                if bossHP > 0:
                    R-= 1
                if HP < 1000:
                    HP += 1

def R_18():
    global bgImg
    if score==100 or score==101 or score==102:
        bgImg=pygame.image.load('1.png')
    if score==200 or score==201 or score==202:
        bgImg=pygame.image.load('全-2.png')
    if score==300 or score==301 or score==302:
        bgImg=pygame.image.load('15-3.png')
    if score==400 or score==401 or score==402:
        bgImg=pygame.image.load('15-6.png')
    if score==500 or score==501 or score==502:
        bgImg=pygame.image.load('15-6.png')
    if score==600 or score==601 or score==602:
        bgImg=pygame.image.load('15-5.png')
    if score==700 or score==701 or score==702:
        bgImg=pygame.image.load('15-5.png')
    if score==800 or score==801 or score==802:
        bgImg=pygame.image.load('15-4.png')
    if score==900 or score==901 or score==902:
        bgImg=pygame.image.load('15-4.png')

class boss_Bullet1():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX +15
        self.y = bossY + 175
        self.xstep = 7
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP,playerX,playerY,is_over,bgImg
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets1.remove(self)
boss_Bullets1 = []  
class boss_Bullet2():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX +15
        self.y = bossY + 175
        self.xstep = 5
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets2.remove(self)
boss_Bullets2 = []
class boss_Bullet3():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX +15
        self.y = bossY + 175
        self.xstep = -7
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets3.remove(self)
boss_Bullets3 = [] 
class boss_Bullet4():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX +15
        self.y = bossY + 175
        self.xstep = -5
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets4.remove(self)
boss_Bullets4 = []
class boss_Bullet5():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX + 150
        self.y = bossY + 175
        self.xstep = -5
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets5.remove(self)
boss_Bullets5 = []
class boss_Bullet6():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX + 150
        self.y = bossY + 175
        self.xstep = -7
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets6.remove(self)
boss_Bullets6 = []
class boss_Bullet7():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX + 150
        self.y = bossY + 175
        self.xstep = 7
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets7.remove(self)
boss_Bullets7 = []
class boss_Bullet8():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX + 150
        self.y = bossY + 175
        self.xstep = 5
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets8.remove(self)
boss_Bullets8 = []
class boss_Bullet9():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX + 40
        self.y = bossY + 175
        self.xstep = -bossXstep
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets9.remove(self)
boss_Bullets9 = []
class boss_Bullet10():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX + 80
        self.y = bossY + 175
        self.xstep = -bossXstep
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets10.remove(self)
boss_Bullets10 = []
class boss_Bullet11():
    def __init__(self):
        self.img = pygame.image.load('boss bullet.png')
        self.x = bossX + 120
        self.y = bossY + 175
        self.xstep = -bossXstep
        self.ystep = 5
    def boss_hit(self):
        global score,number_of_enemies,bossHP,HP
        if (distance(self.x+12,self.y+12,playerX+45,playerY+50)<50):             
            score -= 10
            HP-=50
            boss_Bullets11.remove(self)
boss_Bullets11 = []

def show_boss_bullets():
    global score
    for b in boss_Bullets1:
        screen.blit(b.img,(b.x,b.y))
        b.boss_hit()
        b.x -= b.xstep
        b.y += b.ystep
        if b.y > 1080 or b.x < 0:
            boss_Bullets1.remove(b)
    for c in boss_Bullets2:
        screen.blit(c.img,(c.x,c.y))
        c.boss_hit()
        c.x -= c.xstep
        c.y += c.ystep
        if c.y > 1080 or c.x < 0:
            boss_Bullets2.remove(c)
    for d in boss_Bullets3:
        screen.blit(d.img,(d.x,d.y))
        d.boss_hit()
        d.x -= d.xstep
        d.y += d.ystep
        if d.y > 1080 or d.x > 1900:
            boss_Bullets3.remove(d)
    for e in boss_Bullets4:
        screen.blit(e.img,(e.x,e.y))
        e.boss_hit()
        e.x -= e.xstep
        e.y += e.ystep
        if e.y > 1080 or e.x > 1900:
            boss_Bullets4.remove(e)
    for f in boss_Bullets5:
        screen.blit(f.img,(f.x,f.y))
        f.boss_hit()
        f.x -= f.xstep
        f.y += f.ystep
        if f.y > 1080 or f.x > 1900:
            boss_Bullets5.remove(f)
    for g in boss_Bullets6:
        screen.blit(g.img,(g.x,g.y))
        g.boss_hit()
        g.x -= g.xstep
        g.y += g.ystep
        if g.y > 1080 or g.x > 1900:
            boss_Bullets6.remove(g)
    for h in boss_Bullets7:
        screen.blit(h.img,(h.x,h.y))
        h.boss_hit()
        h.x -= h.xstep
        h.y += h.ystep
        if h.y > 1080 or h.x < 0:
            boss_Bullets7.remove(h)
    for i in boss_Bullets8:
        screen.blit(i.img,(i.x,i.y))
        i.boss_hit()
        i.x -= i.xstep
        i.y += i.ystep
        if i.y > 1080 or i.x < 0:
            boss_Bullets8.remove(i)
    for j in boss_Bullets9:
        screen.blit(j.img,(j.x,j.y))
        j.boss_hit()
        j.x -= j.xstep
        j.y += j.ystep
        if j.y > 1080 :
            boss_Bullets9.remove(j)
    for l in boss_Bullets10:
        screen.blit(l.img,(l.x,l.y))
        l.boss_hit()
        l.x -= l.xstep
        l.y += l.ystep
        if l.y > 1080 :
            boss_Bullets10.remove(l)
    for m in boss_Bullets11:
        screen.blit(m.img,(m.x,m.y))
        m.boss_hit()
        m.x -= m.xstep
        m.y += m.ystep
        if m.y > 1080 :
            boss_Bullets11.remove(m)
                    

def bullets_score():
    global number_of_bullets,test1
    test1=0
    if time_eplased > 0:
        if score > 99:
            if score%100 == 0 or score%100 == 1 or score%100 == 2:
                if now%20 == 0:
                    test1+=10
                    if test1%10==0: 
                        number_of_bullets += test1

#游戏结束
is_over = False
Over_font = pygame.font.SysFont('Calibri',100)
def check_is_over():
    global B,HP,playerX,playerY,bgImg,score,is_over
    if number_of_enemies == 0:
        if HP <= 0:
            is_over = True
            bgImg =pygame.image.load('结束.png')
            playerX=909
            playerY=800
            bullets1.clear()
            bullets2.clear()
            bullets3.clear()
            score = score
            HP = 0
    if is_over:
        text1 = "Game Over"
        text2 = f"score:{score}"
        text3 = "You Lose"
        render1 = Over_font.render(text1,True,(0,255,0))
        render2 = Over_font.render(text2,True,(0,255,0))
        render3 = Over_font.render(text3,True,(0,255,0))
        screen.blit(render1,(700,450))
        screen.blit(render2,(760,550))
        screen.blit(render3,(760,350))
        B=0 
        boss_Bullets1.clear()
        boss_Bullets2.clear()
        boss_Bullets3.clear()
        boss_Bullets4.clear()
        boss_Bullets5.clear()
        boss_Bullets6.clear()
        boss_Bullets7.clear()
        boss_Bullets8.clear()
        boss_Bullets9.clear()
        boss_Bullets10.clear()
        boss_Bullets11.clear()
        if HP <= 0:
            HP =0
    if R==0:
        bgImg =pygame.image.load('结束.png')
        text1 = "Game Over"
        text2 = f"score:{score}"
        text3 = "You Win"
        render1 = Over_font.render(text1,True,(0,255,0))
        render2 = Over_font.render(text2,True,(0,255,0))
        render3 = Over_font.render(text3,True,(0,255,0))
        screen.blit(render1,(700,450))
        screen.blit(render2,(725,550))
        screen.blit(render3,(785,350))
        B=0 
        boss_Bullets1.clear()
        boss_Bullets2.clear()
        boss_Bullets3.clear()
        boss_Bullets4.clear()
        boss_Bullets5.clear()
        boss_Bullets6.clear()
        boss_Bullets7.clear()
        boss_Bullets8.clear()
        boss_Bullets9.clear()
        boss_Bullets10.clear()
        boss_Bullets11.clear()
        bullets1.clear()
        bullets2.clear()
        bullets3.clear()
        

#添加敌人
number_of_enemies = random.randint(40, 50)
class Enemy():
    def __init__(self):
        self.img = pygame.image.load('陨石.png')
        self.x = random.randint(182,1631)
        self.y = random.randint(130,430)
        self.xstep = random.randint(-20,20)
        self.ystep = random.randint(-20,20)
    def reset(self):
        self.x = random.randint(182,1631)
        self.y = random.randint(130,430)
        self.xstep = random.randint(-20,20)
        self.ystep = random.randint(-20,20)
enemies = []
for i in range(number_of_enemies):
    enemies.append(Enemy())
    
#添加boss
def show_boss():
    global number_of_enemies,S,B,R,boss,score,bossX,bossY,bossHP,bossXstep,bossYstep,number_of_bullets
    if number_of_enemies == 0:
        if bossHP > 0 and is_over == False: 
            screen.blit(boss,(bossX,bossY))
            bullets1.append(Bullet1())
            bullets2.append(Bullet2())
            bullets3.append(Bullet3())
            if  now%40== 0:
                boss_Bullets1.append(boss_Bullet1())
                boss_Bullets2.append(boss_Bullet2())
                boss_Bullets3.append(boss_Bullet3())
                boss_Bullets4.append(boss_Bullet4())
                boss_Bullets5.append(boss_Bullet5())
                boss_Bullets6.append(boss_Bullet6())
                boss_Bullets7.append(boss_Bullet7())
                boss_Bullets8.append(boss_Bullet8())
                boss_Bullets9.append(boss_Bullet9())
                boss_Bullets10.append(boss_Bullet10())
                boss_Bullets11.append(boss_Bullet11())
        bossX += bossXstep
        B=0
        number_of_bullets=999
        show_bossHP()
        S=0 
        if bossX > 1550 or bossX < 185:
            bossXstep *= -1
        if bossHP < 0:
            bossHP = 0
        if bossHP == 0:#死亡加分
            B=2
            score+=R*(HP/1000)
            R=0
            
        

    
#敌人移动
def show_enmey():
    global time_eplased,now
    for e in enemies:
        if now > 5000:
            screen.blit(e.img,(e.x,e.y))
            e.x += e.xstep * time_eplased
            e.y += e.ystep * time_eplased
            if e.x > 1678 or e.x < 185:
                e.xstep *= -1
            if e.y > 900  or e.y < 100:
                e.ystep *= -1
            
#玩家子弹
class Bullet1():
    def __init__(self):
        self.img = pygame.image.load('bullet1.png')
        self.x = playerX - 5
        self.y = playerY - 20
        self.step = 30
    def hit(self):
        global score,number_of_enemies,bossHP
        for e in enemies:
            if (distance(self.x,self.y,e.x+20,e.y+20)<30):              
                score += 1
                if score <1000:
                    e.reset()
                else:
                    enemies.remove(e)
                    number_of_enemies-=1
        if B==0:
            if (distance(self.x+13,self.y+29,bossX+90,bossY+100)<130):  
                bossHP -= 1
                bullets1.remove(self)
bullets1 = []

class Bullet2():
    def __init__(self):
        self.img = pygame.image.load('bullet2.png')
        self.x = playerX + 72
        self.y = playerY - 20 
        self.step = 30
    def hit(self):
        global score,number_of_enemies,bossHP
        for e in enemies:
            if (distance(self.x,self.y,e.x,e.y)<30):             
                score += 1
                if score < 1000:
                    e.reset()
                else:
                    enemies.remove(e)
                    number_of_enemies-=1
        if B==0:
            if (distance(self.x+13,self.y+29,bossX+90,bossY+100)<130):  
                bossHP -= 1
                bullets2.remove(self)
bullets2 = []

class Bullet3():
    def __init__(self):
        self.img = pygame.image.load('bullet3.png')
        self.x = playerX + 34
        self.y = playerY - 40
        self.step = 30
    def hit(self):
        global score,number_of_enemies,bossHP
        for e in enemies:
            if (distance(self.x,self.y,e.x+20,e.y+20)<30):              
                score += 1
                if score < 1000:
                    e.reset()
                else:
                    enemies.remove(e)
                    number_of_enemies-=1  
        if B==0:
            if (distance(self.x+14,self.y+28,bossX+90,bossY+100)<150):  
                bossHP -= 1
                bullets3.remove(self)
bullets3 = []

def show_bullets():
    global score
    for b in bullets1:
        screen.blit(b.img,(b.x,b.y))
        b.hit()
        b.y -= b.step
        if b.y < 0:
            bullets1.remove(b)
    for c in bullets2:
        screen.blit(c.img,(c.x,c.y))
        c.hit()
        c.y -= c.step
        if c.y < 0:
            bullets2.remove(c)
    for d in bullets3:
        screen.blit(d.img,(d.x,d.y))
        d.hit()
        d.y -= d.step
        if d.y < 0:
            bullets3.remove(d)


#距离检测
def distance(bx,by,ex,ey):
    a = bx - ex
    b = by - ey
    return math.sqrt(a**2 + b**2)
    
#玩家移动  
def show_player():
    if now > 5000:
        screen.blit(playerImg,(playerX,playerY))
def move_player():
    global playerX,playerY
    a = playerX+45
    b = playerY+50
    playerX += playerXStep
    playerY += playerYStep
    if playerX > 1615:
        playerX = 1615
    if playerX < 182:
        playerX = 182
    if playerY > 880:
        playerY = 880
    if playerY < 100:
        playerY = 100
    def collision():
        global HP,bgImg,is_over,playerX,playerY,score,bossHP
        for e in enemies:
            if time_eplased > 0:
                if (distance(a,b,e.x+20,e.y+20)<60):              
                    HP -= 25
                    if HP <= 0:
                        is_over = True
                        enemies.clear()
                        bgImg =pygame.image.load('结束.png')
                        playerX=909
                        playerY=800
                        score = score
                        HP = 0
        if (distance(a,b,bossX+90,bossY+100)<185):
            if number_of_enemies == 0:
                HP = 0
    collision()

#按键      
def process_event(): 
    global playerXStep,playerYStep,playerX,playerY,now,lihuiX,B,lihuiY,bgImg,number_of_bullets,time_eplased,bgm
    for event in pygame.event.get():
        if event.type ==pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if time_eplased > 0:
                    if number_of_bullets > 0 and B == 1:
                        bullets1.append(Bullet1())
                        bullets2.append(Bullet2())
                        bullets3.append(Bullet3())
                        number_of_bullets -= B
        if mouseused:
            if event.type == pygame.MOUSEMOTION:
                a,b = pygame.mouse.get_pos()
                playerX = a - 45
                playerY = b - 45
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                clock = pygame.time.Clock()
                clock.tick(30)
                time_eplased = clock.tick(30)/100
                bgImg=pygame.image.load('5.png')
                lihuiX=210
                lihuiY=616
                now+=5000
                bgm = 'bg.flac'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_LEFT:
                playerXStep = -20
            if event.key == pygame.K_RIGHT:
                playerXStep = 20   
            if event.key == pygame.K_UP:
                playerYStep = -10
            if event.key == pygame.K_DOWN:
                playerYStep = 10
            if event.key == pygame.K_1:
                bgImg=pygame.image.load('bg.png')
            if event.key == pygame.K_2:
                bgImg=pygame.image.load('bg1.png')
            if event.key == pygame.K_3:
                bgImg=pygame.image.load('bg2.png')
            if event.key == pygame.K_4:
                bgImg=pygame.image.load('bg3.png')
            if event.key == pygame.K_5:
                bgImg=pygame.image.load('bg4.png')
            if event.key == pygame.K_6:
                bgImg=pygame.image.load('bg5.png')
            if event.key == pygame.K_7:
                bgImg=pygame.image.load('bg7.png')
            if event.key == pygame.K_q:
                bgm = 'n-buna - エピローグ.mp3'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_w:
                bgm = 'n-buna - モノローグ.mp3'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_e:
                bgm = 'n-buna - 白ゆきの独白.flac'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_r:
                bgm = 'ヨルシカ - 4 10.flac'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_t:
                bgm = 'ヨルシカ - 5 6.flac'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_y:
                bgm = 'ヨルシカ - 8 31.flac'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_u:
                bgm = 'ヨルシカ - 車窓.mp3'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_i:
                bgm = 'ヨルシカ - 海底、月明かり.mp3'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_o:
                bgm = 'ヨルシカ - 前世.flac'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_p:
                bgm = 'ヨルシカ - 夏、バス停、君を待つ.flac'
                pygame.mixer.music.load(bgm)
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(0.1)
            if event.key == pygame.K_SPACE:
                if time_eplased > 0:
                    if number_of_bullets > 0 and B == 1:
                        bullets1.append(Bullet1())
                        bullets2.append(Bullet2())
                        bullets3.append(Bullet3())
                        number_of_bullets -= B
            if event.key == pygame.K_ESCAPE:   
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYUP:
            playerXStep = 0
            playerYStep = 0
        
            
#游戏主循环
running = True
mouseused = True
while running:
    screen.blit(bgImg,(0,0))
    if time_eplased > 0:
        show_score()
        show_HP()
        show_number_of_bullets()
    show_player()
    screen.blit(lihuiImg,(lihuiX,lihuiY))
    move_player()
    show_enmey()
    show_bullets()
    process_event()
    check_is_over()
    score_time()
    bullets_score()
    show_boss_bullets()
    R_18()
    now += 1
    show_boss()
    pygame.display.update()