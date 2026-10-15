import pyxel, random, time

pyxel.init(128, 128, title="Nuit du Code")
pyxel.load('4.pyxres')


#################### Initialisation ####################

orientation=0
mov=0
x=60
y=488
ycam=0
xcam=0
camdep=1
camdepy=1
camdepx=0.5
oiseau_liste=[]

tuiles_vides=[(0,0),(3,23),(5,23),(0,25),(1,25),(2,25),(4,24),(5,24),(16,26),(17,26),(16,27),(17,27),(16,28),(17,28),(16,29),(17,29),(0,28),(0,29),(2,27),(3,27),(2,28),(3,28),(2,29),(3,29),(9,28),(9,29),(10,28),(11,28),(12,28),(10,29),(11,29),(12,29)]
tuiles_grimper=[(4,28),(5,28),(6,28),(4,29),(5,29),(6,29),(13,28),(14,28),(15,28),(13,29),(14,29),(15,29)]
tuiles_semipleines=[(4,23),(6,23),(13,27),(14,27),(15,27),(4,27),(5,27),(6,27),(1,26),(2,26),(3,26),(3,25),(4,25),(5,25),(0,27),(1,27),(2,27),(3,27),(9,27),(10,27),(11,27),(12,27)]
tuiles_pleines=[(4,23),(6,23)]

saut=False
nbsaut=0
climbing=False
bloquer=False

menu=0
vie=3
cle_verte=0
cle_rouge=0
t0=0
t1=0

#################### Fonctions ####################

def move():
    global x,y,orientation
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
        x+=1
        orientation=0
    if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
        x-=1
        orientation=1

def jump():
    global x,y,saut,nbsaut,tuiles_pleines,tuiles_semipleines
    if pyxel.btn(pyxel.KEY_SPACE) and pyxel.tilemap(0).pget(x//8,(y)//8) not in tuiles_semipleines:
        if pyxel.tilemap(0).pget((x+4)//8,y//8+1) in tuiles_semipleines:
            saut=True
    if saut==True:
        y-=2
        nbsaut+=1
        if nbsaut==20 or pyxel.tilemap(0).pget((x+4)//8,y//8) in tuiles_semipleines:
            saut=False
            nbsaut=0
    else:
        if pyxel.tilemap(0).pget((x+4)//8,y//8+1) not in tuiles_semipleines:
            y+=2

def climb():
    global x,y,climbing,tuiles_grimper
    if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_Z):
            if pyxel.tilemap(0).pget((x-6)//8,y//8) in tuiles_grimper or pyxel.tilemap(0).pget(x//8,y//8) in tuiles_grimper or pyxel.tilemap(0).pget((x+5)//8,y//8) in tuiles_grimper or pyxel.tilemap(0).pget((x-6)//8,y//8+1) in tuiles_grimper or pyxel.tilemap(0).pget(x//8,y//8+1) in tuiles_grimper or pyxel.tilemap(0).pget((x+5)//8,y//8+1) in tuiles_grimper:
                climbing=True
    if climbing==True:
        y-=3
        if pyxel.tilemap(0).pget((x-6)//8,y//8) not in tuiles_grimper and pyxel.tilemap(0).pget(x//8,y//8) not in tuiles_grimper and pyxel.tilemap(0).pget((x+5)//8,y//8) not in tuiles_grimper and pyxel.tilemap(0).pget((x-6)//8,y//8+1) not in tuiles_grimper and pyxel.tilemap(0).pget(x//8,y//8+1) not in tuiles_grimper and pyxel.tilemap(0).pget((x+5)//8,y//8+1) not in tuiles_grimper:
            climbing=False

def blockaside():
    global x,y,bloquer,tuiles_pleines
    if pyxel.tilemap(0).pget(x//8,(y+ 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7)//8) in tuiles_pleines:
        bloquer=True
        x+=1
    elif pyxel.tilemap(0).pget((x+6)//8,(y+ 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7)//8) in tuiles_pleines:
        bloquer=True
        x-=1
    else:
        bloquer=False

def oiseau_creation():
    global oiseau_liste
    if pyxel.frame_count%20 == 0:
        oiseau_liste.append([0,random.randint(0,488)])

def oiseau_deplacement():
    global oiseau_liste
    for oiseau in oiseau_liste:
        oiseau[0] += 1
        if oiseau[0]>504:
            oiseau_liste.remove(oiseau)

def collision_oiseau_perso():
    global vie, oiseau_liste,x,y
    for oiseau in oiseau_liste:
        if oiseau[0]-7<=x<=oiseau[0]+7 and oiseau[1]-7<=y<=oiseau[1]+7:
            x+=2
            


def parametre_menu():
    global menu,vie,orientation,x,y,tuiles_vides,sauter,tomber,gravity,menu,vie,ycam,xcam,camdepy,camdepx,oiseau_liste,saut,nbsaut,climbing,bloquer,cle_verte,cle_rouge,t0,t1,tuiles_vides,tuiles_grimper,tuiles_semivides,tuiles_pleines
    if menu==0:
        pyxel.camera(xcam,ycam)
        ycam=ycam+camdepy
        xcam=ycam+camdepx
        if ycam==384:
            ycam=0
            xcam=0
        if pyxel.btn(pyxel.KEY_RETURN):
            menu=1
            t0=time.time()
    if menu==1 and vie==0:
        menu=2
    if menu==1 and pyxel.tilemap(0).pget((x-6)//8,y//8)==(2,21):
        menu=3
        t1=time.time()
    if menu==2 and pyxel.btn(pyxel.KEY_RETURN):
        menu=0
        orientation=0
        x=60
        y=488
        tuiles_vides=[(0,0),(3,23),(5,23),(0,25),(1,25),(2,25),(4,24),(5,24),(16,26),(17,26),(16,27),(17,27),(16,28),(17,28),(16,29),(17,29),(0,28),(0,29),(2,27),(3,27),(2,28),(3,28),(2,29),(3,29),(9,28),(9,29),(10,28),(11,28),(12,28),(10,29),(11,29),(12,29)]
        tuiles_grimper=[(4,27),(5,27),(6,27),(4,28),(5,28),(6,28),(4,29),(5,29),(6,29),(13,27),(14,27),(15,27),(13,28),(14,28),(15,28),(13,29),(14,29),(15,29)]
        tuiles_semivides=[(13,27),(14,27),(15,27),(4,27),(5,27),(6,27),(1,26),(2,26),(3,26),(3,25),(4,25),(5,25),(0,27),(1,27),(2,27),(3,27),(9,27),(10,27),(11,27),(12,27)]
        tuiles_pleines=[(4,23),(6,23),(10,23),(11,23),(12,23)]
        menu=0
        vie=3
        saut=False
        nbsaut=False
        climbing=False
        ycam=0
        xcam=0
        camdepy=1
        camdepx=0.5
        cle_verte=0
        cle_rouge=0
        t0=time.time()

def cle_obtention():
    global cle_verte, cle_rouge
    if pyxel.tilemap(0).pget(x//8,y//8)==(5,24):
        cle_verte=1
        pyxel.tilemap(0).pset(x//8,y//8,(0,0))
    
    if pyxel.tilemap(0).pget(x//8,y//8)==(4,24):
        cle_rouge=1
        pyxel.tilemap(0).pset(x//8,y//8,(0,0))

def mort():
    global vie,y,x
    if y>500:
        vie-=1
        x=60
        y=488   

#################### RUN ####################

def update():
    parametre_menu()
    oiseau_creation()
    oiseau_deplacement()
    if menu==1:
        cle_obtention()
        collision_oiseau_perso()
        move()
        jump()
        climb()
        blockaside()
        oiseau_creation()
        oiseau_deplacement()
        mort()
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()


################### DRAW ####################
def draw():
    global menu,orientation
    pyxel.cls(0)
    if menu==0:
        pyxel.bltm(0,0,0,0,0,510,510)
        pyxel.text(xcam+45,ycam+50, "Welcome in ",7)
        pyxel.text(xcam+40,ycam+65, "Bird Climbing",7)
        pyxel.text(xcam+35,ycam+120, ">Press <enter> to play<",9)
        for oiseau in oiseau_liste:
            if 0<=pyxel.frame_count%40<20 <= 20:
                pyxel.blt(oiseau[0],oiseau[1],0, 24, 136, 8, 8, 5)
            if 20<=pyxel.frame_count%40<40 <= 40:
                pyxel.blt(oiseau[0],oiseau[1],0, 32, 136, 8, 8, 5)
    if menu==1:
        
        pyxel.camera(x-60,y-60)
        pyxel.bltm(x-60,y-60,0,x-60,y-60,504,504)
        if vie==3:
            pyxel.blt(x-60, y-60, 0, 48, 168, 8, 8, 5)
            pyxel.blt(x-51, y-60, 0, 48, 168, 8, 8, 5)
            pyxel.blt(x-42, y-60, 0, 48, 168, 8, 8, 5)
        if vie==2:
            pyxel.blt(x-60, y-60, 0, 48, 168, 8, 8, 5)
            pyxel.blt(x-51, y-60, 0, 48, 168, 8, 8, 5)
            pyxel.blt(x-42, y-60, 0, 56, 168, 8, 8, 5)
        if vie==1:
            pyxel.blt(x-60, y-60, 0, 48, 168, 8, 8, 5)
            pyxel.blt(x-51, y-60, 0, 56, 168, 8, 8, 5)
            pyxel.blt(x-42, y-60, 0, 56, 168, 8, 8, 5)
        for oiseau in oiseau_liste:
            if 0<=pyxel.frame_count%40<20 <= 20:
                pyxel.blt(oiseau[0],oiseau[1],0, 24, 136, 8, 8, 5)
            if 20<=pyxel.frame_count%40<40 <= 40:
                pyxel.blt(oiseau[0],oiseau[1],0, 32, 136, 8, 8, 5)
        if orientation==0:
            if saut==True:
                    pyxel.blt(x, y, 0, 16, 16, 8, 8, 5)
            if mov==1:
                if 0<=pyxel.frame_count%20<=10:
                    pyxel.blt(x, y, 0, 8, 16, 8, 8, 5)
                if 10<pyxel.frame_count%20<=20:
                    pyxel.blt(x, y, 0, 0, 16, 8, 8, 5)
            if mov==0:
                pyxel.blt(x, y, 0, 0, 16, 8, 8, 5)
        if orientation==1:
            if saut==True:
                    pyxel.blt(x, y, 0, 16, 24, 8, 8, 5)
            if mov==1:
                if 0<=pyxel.frame_count%20<=10:
                    pyxel.blt(x, y, 0, 8, 24, 8, 8, 5)
                if 10<pyxel.frame_count%20<=20:
                    pyxel.blt(x, y, 0, 0, 24, 8, 8, 5)
            if mov==0:
                pyxel.blt(x, y, 0, 0, 24, 8, 8, 5)
        
        if cle_verte==1:
            pyxel.tilemap(0).pset(1,3,(6,23))
            pyxel.tilemap(0).pset(2,3,(6,23))
            pyxel.tilemap(0).pset(3,3,(6,23))
            pyxel.tilemap(0).pset(4,3,(6,23))
            pyxel.tilemap(0).pset(5,3,(6,23))
            pyxel.tilemap(0).pset(6,3,(6,23))
            pyxel.tilemap(0).pset(7,3,(6,23))
            pyxel.tilemap(0).pset(8,3,(6,23))
            pyxel.tilemap(0).pset(9,3,(6,23))
            pyxel.tilemap(0).pset(10,3,(6,23))
            pyxel.tilemap(0).pset(11,55,(6,23))
            pyxel.tilemap(0).pset(12,55,(6,23))
            pyxel.tilemap(0).pset(13,55,(6,23))
            pyxel.tilemap(0).pset(14,55,(6,23))
            pyxel.tilemap(0).pset(15,55,(6,23))
            pyxel.tilemap(0).pset(16,55,(6,23))
            pyxel.tilemap(0).pset(17,55,(6,23))
            pyxel.tilemap(0).pset(18,55,(6,23))
            pyxel.tilemap(0).pset(19,55,(6,23))
            pyxel.tilemap(0).pset(20,55,(6,23))
            pyxel.tilemap(0).pset(21,55,(6,23))
            pyxel.tilemap(0).pset(17,43,(6,23))
            pyxel.tilemap(0).pset(18,42,(6,23))
            pyxel.tilemap(0).pset(19,41,(6,23))
            pyxel.tilemap(0).pset(20,40,(6,23))
            pyxel.tilemap(0).pset(21,39,(6,23))
            pyxel.tilemap(0).pset(22,39,(6,23))
            pyxel.tilemap(0).pset(23,39,(6,23))
            pyxel.tilemap(0).pset(24,39,(6,23))
            pyxel.tilemap(0).pset(25,39,(6,23))
            pyxel.tilemap(0).pset(26,39,(6,23))
            pyxel.tilemap(0).pset(27,39,(6,23))
            pyxel.tilemap(0).pset(28,39,(6,23))
            pyxel.tilemap(0).pset(29,39,(6,23))
            pyxel.tilemap(0).pset(30,39,(6,23))
            pyxel.tilemap(0).pset(31,39,(6,23))
            pyxel.tilemap(0).pset(32,39,(6,23))
            pyxel.tilemap(0).pset(33,39,(6,23))
            pyxel.tilemap(0).pset(34,39,(6,23))
            pyxel.tilemap(0).pset(35,39,(6,23))
            pyxel.tilemap(0).pset(36,39,(6,23))
            pyxel.tilemap(0).pset(37,39,(6,23))
            pyxel.tilemap(0).pset(51,39,(6,23))
            pyxel.tilemap(0).pset(56,38,(6,23))
            pyxel.tilemap(0).pset(56,39,(6,23))
            pyxel.tilemap(0).pset(61,37,(6,23))
            pyxel.tilemap(0).pset(61,38,(6,23))
            pyxel.tilemap(0).pset(61,39,(6,23))
            pyxel.tilemap(0).pset(36,26,(6,23))
            pyxel.tilemap(0).pset(37,26,(6,23))
            pyxel.tilemap(0).pset(38,26,(6,23))
            pyxel.tilemap(0).pset(46,24,(6,23))
            pyxel.tilemap(0).pset(46,25,(6,23))
            pyxel.tilemap(0).pset(46,26,(6,23))
            pyxel.tilemap(0).pset(39,19,(6,23))
            pyxel.tilemap(0).pset(40,19,(6,23))
            pyxel.tilemap(0).pset(41,19,(6,23))
            pyxel.tilemap(0).pset(42,19,(6,23))
            pyxel.tilemap(0).pset(43,19,(6,23))
            pyxel.tilemap(0).pset(44,19,(6,23))
        if cle_rouge==1:
            pyxel.tilemap(0).pset(4,1,(4,23))
            pyxel.tilemap(0).pset(4,2,(4,23))
            pyxel.tilemap(0).pset(8,1,(4,23))
            pyxel.tilemap(0).pset(8,2,(4,23))
            pyxel.tilemap(0).pset(11,3,(4,23))
            pyxel.tilemap(0).pset(11,4,(4,23))
            pyxel.tilemap(0).pset(11,5,(4,23))
            pyxel.tilemap(0).pset(11,6,(4,23))
            pyxel.tilemap(0).pset(11,7,(4,23))
            pyxel.tilemap(0).pset(11,8,(4,23))
            pyxel.tilemap(0).pset(11,9,(4,23))
            pyxel.tilemap(0).pset(22,10,(4,23))
            pyxel.tilemap(0).pset(23,10,(4,23))
            pyxel.tilemap(0).pset(24,10,(4,23))
            pyxel.tilemap(0).pset(25,10,(4,23))
            pyxel.tilemap(0).pset(26,10,(4,23))
            pyxel.tilemap(0).pset(48,21,(4,23))
            pyxel.tilemap(0).pset(49,21,(4,23))
            pyxel.tilemap(0).pset(50,21,(4,23))
            pyxel.tilemap(0).pset(43,26,(4,23))
            pyxel.tilemap(0).pset(44,26,(4,23))
            pyxel.tilemap(0).pset(45,26,(4,23))
            pyxel.tilemap(0).pset(33,26,(4,23))
            pyxel.tilemap(0).pset(34,26,(4,23))
            pyxel.tilemap(0).pset(35,26,(4,23))
            pyxel.tilemap(0).pset(48,34,(4,23))
            pyxel.tilemap(0).pset(49,34,(4,23))
            pyxel.tilemap(0).pset(50,34,(4,23))
            pyxel.tilemap(0).pset(51,34,(4,23))
            pyxel.tilemap(0).pset(51,34,(4,23))
            pyxel.tilemap(0).pset(52,34,(4,23))
            pyxel.tilemap(0).pset(53,34,(4,23))
            pyxel.tilemap(0).pset(54,34,(4,23))
            pyxel.tilemap(0).pset(55,34,(4,23))
            pyxel.tilemap(0).pset(56,34,(4,23))
            pyxel.tilemap(0).pset(57,34,(4,23))
            pyxel.tilemap(0).pset(58,34,(4,23))
            pyxel.tilemap(0).pset(59,34,(4,23))
            pyxel.tilemap(0).pset(60,34,(4,23))
            pyxel.tilemap(0).pset(0,31,(4,23))
            pyxel.tilemap(0).pset(0,32,(4,23))
            pyxel.tilemap(0).pset(0,33,(4,23))
            pyxel.tilemap(0).pset(0,34,(4,23))
            pyxel.tilemap(0).pset(0,35,(4,23))
            pyxel.tilemap(0).pset(0,36,(4,23))
            pyxel.tilemap(0).pset(0,37,(4,23))
            pyxel.tilemap(0).pset(0,38,(4,23))
            pyxel.tilemap(0).pset(0,39,(4,23))
            pyxel.tilemap(0).pset(0,40,(4,23))
            pyxel.tilemap(0).pset(0,41,(4,23))
            pyxel.tilemap(0).pset(0,42,(4,23))
            pyxel.tilemap(0).pset(0,43,(4,23))
            pyxel.tilemap(0).pset(1,43,(4,23))
            pyxel.tilemap(0).pset(2,43,(4,23))
            pyxel.tilemap(0).pset(3,43,(4,23))
            pyxel.tilemap(0).pset(4,43,(4,23))
            pyxel.tilemap(0).pset(5,43,(4,23))
            pyxel.tilemap(0).pset(2,40,(4,23))
            pyxel.tilemap(0).pset(3,40,(4,23))
            pyxel.tilemap(0).pset(3,39,(4,23))
            pyxel.tilemap(0).pset(3,38,(4,23))
            pyxel.tilemap(0).pset(1,37,(4,23))
            pyxel.tilemap(0).pset(3,37,(4,23))
            pyxel.tilemap(0).pset(3,36,(4,23))
            pyxel.tilemap(0).pset(3,35,(4,23))
            pyxel.tilemap(0).pset(2,34,(4,23))
            pyxel.tilemap(0).pset(3,34,(4,23))
            pyxel.tilemap(0).pset(4,34,(4,23))
            pyxel.tilemap(0).pset(5,34,(4,23))
            pyxel.tilemap(0).pset(6,34,(4,23))
            pyxel.tilemap(0).pset(7,34,(4,23))
            pyxel.tilemap(0).pset(8,34,(4,23))
            pyxel.tilemap(0).pset(1,31,(4,23))
            pyxel.tilemap(0).pset(2,31,(4,23))
            pyxel.tilemap(0).pset(3,31,(4,23))
            pyxel.tilemap(0).pset(4,31,(4,23))
            pyxel.tilemap(0).pset(5,31,(4,23))
            pyxel.tilemap(0).pset(6,31,(4,23))
            pyxel.tilemap(0).pset(7,31,(4,23))
            pyxel.tilemap(0).pset(8,31,(4,23))
        
        if cle_verte==0:
            pyxel.tilemap(0).pset(27,43,(5,24))
            pyxel.tilemap(0).pset(1,3,(5,23))
            pyxel.tilemap(0).pset(2,3,(5,23))
            pyxel.tilemap(0).pset(3,3,(5,23))
            pyxel.tilemap(0).pset(4,3,(5,23))
            pyxel.tilemap(0).pset(5,3,(5,23))
            pyxel.tilemap(0).pset(6,3,(5,23))
            pyxel.tilemap(0).pset(7,3,(5,23))
            pyxel.tilemap(0).pset(8,3,(5,23))
            pyxel.tilemap(0).pset(9,3,(5,23))
            pyxel.tilemap(0).pset(10,3,(5,23))
            pyxel.tilemap(0).pset(11,55,(5,23))
            pyxel.tilemap(0).pset(12,55,(5,23))
            pyxel.tilemap(0).pset(13,55,(5,23))
            pyxel.tilemap(0).pset(14,55,(5,23))
            pyxel.tilemap(0).pset(15,55,(5,23))
            pyxel.tilemap(0).pset(16,55,(5,23))
            pyxel.tilemap(0).pset(17,55,(5,23))
            pyxel.tilemap(0).pset(18,55,(5,23))
            pyxel.tilemap(0).pset(19,55,(5,23))
            pyxel.tilemap(0).pset(20,55,(5,23))
            pyxel.tilemap(0).pset(21,55,(5,23))
            pyxel.tilemap(0).pset(17,43,(5,23))
            pyxel.tilemap(0).pset(18,42,(5,23))
            pyxel.tilemap(0).pset(19,41,(5,23))
            pyxel.tilemap(0).pset(20,40,(5,23))
            pyxel.tilemap(0).pset(21,39,(5,23))
            pyxel.tilemap(0).pset(22,39,(5,23))
            pyxel.tilemap(0).pset(23,39,(5,23))
            pyxel.tilemap(0).pset(24,39,(5,23))
            pyxel.tilemap(0).pset(25,39,(5,23))
            pyxel.tilemap(0).pset(26,39,(5,23))
            pyxel.tilemap(0).pset(27,39,(5,23))
            pyxel.tilemap(0).pset(28,39,(5,23))
            pyxel.tilemap(0).pset(29,39,(5,23))
            pyxel.tilemap(0).pset(30,39,(5,23))
            pyxel.tilemap(0).pset(31,39,(5,23))
            pyxel.tilemap(0).pset(32,39,(5,23))
            pyxel.tilemap(0).pset(33,39,(5,23))
            pyxel.tilemap(0).pset(34,39,(5,23))
            pyxel.tilemap(0).pset(35,39,(5,23))
            pyxel.tilemap(0).pset(36,39,(5,23))
            pyxel.tilemap(0).pset(37,39,(5,23))
            pyxel.tilemap(0).pset(51,39,(5,23))
            pyxel.tilemap(0).pset(56,38,(5,23))
            pyxel.tilemap(0).pset(56,39,(5,23))
            pyxel.tilemap(0).pset(61,37,(5,23))
            pyxel.tilemap(0).pset(61,38,(5,23))
            pyxel.tilemap(0).pset(61,39,(5,23))
            pyxel.tilemap(0).pset(36,26,(5,23))
            pyxel.tilemap(0).pset(37,26,(5,23))
            pyxel.tilemap(0).pset(38,26,(5,23))
            pyxel.tilemap(0).pset(46,24,(5,23))
            pyxel.tilemap(0).pset(46,25,(5,23))
            pyxel.tilemap(0).pset(46,26,(5,23))
            pyxel.tilemap(0).pset(39,19,(5,23))
            pyxel.tilemap(0).pset(40,19,(5,23))
            pyxel.tilemap(0).pset(41,19,(5,23))
            pyxel.tilemap(0).pset(42,19,(5,23))
            pyxel.tilemap(0).pset(43,19,(5,23))
            pyxel.tilemap(0).pset(44,19,(5,23))
        if cle_rouge==0:
            pyxel.tilemap(0).pset(61,36,(4,24))
            pyxel.tilemap(0).pset(4,1,(3,23))
            pyxel.tilemap(0).pset(4,2,(3,23))
            pyxel.tilemap(0).pset(8,1,(3,23))
            pyxel.tilemap(0).pset(8,2,(3,23))
            pyxel.tilemap(0).pset(11,3,(3,23))
            pyxel.tilemap(0).pset(11,4,(3,23))
            pyxel.tilemap(0).pset(11,5,(3,23))
            pyxel.tilemap(0).pset(11,6,(3,23))
            pyxel.tilemap(0).pset(11,7,(3,23))
            pyxel.tilemap(0).pset(11,8,(3,23))
            pyxel.tilemap(0).pset(11,9,(3,23))
            pyxel.tilemap(0).pset(22,10,(3,23))
            pyxel.tilemap(0).pset(23,10,(3,23))
            pyxel.tilemap(0).pset(24,10,(3,23))
            pyxel.tilemap(0).pset(25,10,(3,23))
            pyxel.tilemap(0).pset(26,10,(3,23))
            pyxel.tilemap(0).pset(48,21,(3,23))
            pyxel.tilemap(0).pset(49,21,(3,23))
            pyxel.tilemap(0).pset(50,21,(3,23))
            pyxel.tilemap(0).pset(43,26,(3,23))
            pyxel.tilemap(0).pset(44,26,(3,23))
            pyxel.tilemap(0).pset(45,26,(3,23))
            pyxel.tilemap(0).pset(33,26,(3,23))
            pyxel.tilemap(0).pset(34,26,(3,23))
            pyxel.tilemap(0).pset(35,26,(3,23))
            pyxel.tilemap(0).pset(48,34,(3,23))
            pyxel.tilemap(0).pset(49,34,(3,23))
            pyxel.tilemap(0).pset(50,34,(3,23))
            pyxel.tilemap(0).pset(51,34,(3,23))
            pyxel.tilemap(0).pset(51,34,(3,23))
            pyxel.tilemap(0).pset(52,34,(3,23))
            pyxel.tilemap(0).pset(53,34,(3,23))
            pyxel.tilemap(0).pset(54,34,(3,23))
            pyxel.tilemap(0).pset(55,34,(3,23))
            pyxel.tilemap(0).pset(56,34,(3,23))
            pyxel.tilemap(0).pset(57,34,(3,23))
            pyxel.tilemap(0).pset(58,34,(3,23))
            pyxel.tilemap(0).pset(59,34,(3,23))
            pyxel.tilemap(0).pset(60,34,(3,23))
            pyxel.tilemap(0).pset(0,31,(3,23))
            pyxel.tilemap(0).pset(0,32,(3,23))
            pyxel.tilemap(0).pset(0,33,(3,23))
            pyxel.tilemap(0).pset(0,34,(3,23))
            pyxel.tilemap(0).pset(0,35,(3,23))
            pyxel.tilemap(0).pset(0,36,(3,23))
            pyxel.tilemap(0).pset(0,37,(3,23))
            pyxel.tilemap(0).pset(0,38,(3,23))
            pyxel.tilemap(0).pset(0,39,(3,23))
            pyxel.tilemap(0).pset(0,40,(3,23))
            pyxel.tilemap(0).pset(0,41,(3,23))
            pyxel.tilemap(0).pset(0,42,(3,23))
            pyxel.tilemap(0).pset(0,43,(3,23))
            pyxel.tilemap(0).pset(1,43,(3,23))
            pyxel.tilemap(0).pset(2,43,(3,23))
            pyxel.tilemap(0).pset(3,43,(3,23))
            pyxel.tilemap(0).pset(4,43,(3,23))
            pyxel.tilemap(0).pset(5,43,(3,23))
            pyxel.tilemap(0).pset(2,40,(3,23))
            pyxel.tilemap(0).pset(3,40,(3,23))
            pyxel.tilemap(0).pset(3,39,(3,23))
            pyxel.tilemap(0).pset(3,38,(3,23))
            pyxel.tilemap(0).pset(1,37,(3,23))
            pyxel.tilemap(0).pset(3,37,(3,23))
            pyxel.tilemap(0).pset(3,36,(3,23))
            pyxel.tilemap(0).pset(3,35,(3,23))
            pyxel.tilemap(0).pset(2,34,(3,23))
            pyxel.tilemap(0).pset(3,34,(3,23))
            pyxel.tilemap(0).pset(4,34,(3,23))
            pyxel.tilemap(0).pset(5,34,(3,23))
            pyxel.tilemap(0).pset(6,34,(3,23))
            pyxel.tilemap(0).pset(7,34,(3,23))
            pyxel.tilemap(0).pset(8,34,(3,23))
            pyxel.tilemap(0).pset(1,31,(3,23))
            pyxel.tilemap(0).pset(2,31,(3,23))
            pyxel.tilemap(0).pset(3,31,(3,23))
            pyxel.tilemap(0).pset(4,31,(3,23))
            pyxel.tilemap(0).pset(5,31,(3,23))
            pyxel.tilemap(0).pset(6,31,(3,23))
            pyxel.tilemap(0).pset(7,31,(3,23))
            pyxel.tilemap(0).pset(8,31,(3,23))
        
            
    if menu==2:
        pyxel.camera(0,0)
        pyxel.blt(0,0,2,0,0,128,128,0)
        pyxel.text(40,50, "Game Over",7)
        pyxel.text(15,60, ">Press <enter> to replay<",7)
    
    if menu==3:
        pyxel.camera(0,0)
        pyxel.blt(0,0,2,0,0,128,128,0)
        pyxel.text(50,50, "You win !",7)
        pyxel.text(5,60, "You did a time of "+str(round(t1-t0))+" seconds !",7)
        pyxel.text(15,70, ">Press <enter> to replay<",7)
        
        if round(t1-t0)<=100:
            pyxel.blt(60,40,2,16,128,8,8)
        if  100<round(t1-t0)<=140:
            pyxel.blt(60,40,2,8,128,8,8)
        if round(t1-t0)>140:
            pyxel.blt(60,40,2,0,128,8,8)
            
        
    
pyxel.run(update, draw)
