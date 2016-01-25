#Created by Ealgase
#The AdventureGame
#The real version
#Created in python3
#index.py
###
#Import the modules
import random
import time
import os
from menu import menu,cls
from runworld import runworld
#Making global vars
global lives
global gold
global damagem
global healthm
global ebhealth
global xp
global special
lives=1
gold=1
damagem=1
healthm=1
ebhealth=0
xp=0
special=[]
#Rendscreen
def rendscreen(text):
    cls()
    print("--------------------------------------------------------------------------------")
    print("Gold: "+ str(gold) + " Lives: " + str(lives) + " XP: "+ str(xp))
    print("Special items: "+str(special))
    print("--------------------------------------------------------------------------------")
    print(text)
#Saving
def save():
    livesfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/lives.tgs"),'w')
    goldfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/gold.tgs"),'w')
    damagemfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/damagem.tgs"),'w')
    healthmfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/healthm.tgs"),'w')
    ebhealthfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/ebhealth.tgs"),'w')
    specialfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/special.tgs"),'w')
    xpfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/xp.tgs"),'w')
    livesfile.write(str(lives))
    goldfile.write(str(gold))
    damagemfile.write(str(damagem))
    healthmfile.write(str(healthm))
    ebhealthfile.write(str(ebhealth))
    xpfile.write(str(xp))
    for item in special:
        specialfile.write(item)
        specialfile.write(',')
    specialfile.write('\b')
    livesfile.close()
    goldfile.close()
    damagemfile.close()
    healthmfile.close()
    ebhealthfile.close()
    specialfile.close()
    xpfile.close()
#Loading
def load():
    #Load the saves
    if os.path.isfile(os.path.expanduser("~/.ealgase/TheGame/saves.tgs")):
        livesfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/lives.tgs"))
        goldfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/gold.tgs"))
        damagemfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/damagem.tgs"))
        healthmfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/healthm.tgs"))
        ebhealthfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/ebhealth.tgs"))
        specialfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/special.tgs"))
        xpfile=open(os.path.expanduser("~/.ealgase/TheGame/saves/xp.tgs"))
        lives=int(livesfile.read())
        gold=int(goldfile.read())
        damagem=int(damagemfile.read())
        healthm=int(healthmfile.read())
        ebhealth=int(ebhealthfile.read())
        xp=int(xpfile.read())
        special=[]
        for item in specialfile.read().split(','):
            special.append(item)
        livesfile.close()
        goldfile.close()
        damagemfile.close()
        healthmfile.close()
        ebhealthfile.close()
        specialfile.close()
        xpfile.close()
    else:
        hello=open(os.path.expanduser("~/.ealgase/TheGame/saves.tgs"),'w')
        hello.close()
        livesfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/lives.tgs"),'w')
        goldfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/gold.tgs"),'w')
        damagemfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/damagem.tgs"),'w')
        healthmfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/healthm.tgs"),'w')
        ebhealthfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/ebhealth.tgs"),'w')
        specialfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/special.tgs"),'w')
        xpfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/xp.tgs"),'w')
        livesfile1.close()
        goldfile1.close()
        damagemfile1.close()
        healthmfile1.close()
        ebhealthfile1.close()
        specialfile1.close()
        xpfile1.close()
        lives=1
        gold=1
        damagem=1
        healthm=1
        ebhealth=0
        xp=0
        special=[]
        save()
#Kick off the game!
option=menu([['Play Tutorial','T'],['Play Game','P'],['Exit','E']],1,'What would you like to do?')
if option=='T':
    #Do the tutorial
    import tutorial
    print("You've finished the tutorial!")
    print("Time to start the real game in 10 seconds")
    time.sleep(1)
    print("Time to start the real game in 9 seconds")
    time.sleep(1)
    print("Time to start the real game in 8 seconds")
    time.sleep(1)
    print("Time to start the real game in 7 seconds")
    time.sleep(1)
    print("Time to start the real game in 6 seconds")
    time.sleep(1)
    print("Time to start the real game in 5 seconds")
    time.sleep(1)
    print("Time to start the real game in 4 seconds")
    time.sleep(1)
    print("Time to start the real game in 3 seconds")
    time.sleep(1)
    print("Time to start the real game in 2 seconds")
    time.sleep(1)
    print("Time to start the real game in 1 second")
    time.sleep(1)
    cls()
elif option=='P':
    #Play da game
    pass
else:
    #Pretty simple
    exit()
print('Loading Saves')
load()
print('Done.')
print('Loading worlds')
world=open(os.path.expanduser("~/.ealagse/TheGame/world/worldlist.tgc"),'w')
worldcontent=world.read()
for item in worldcontent.split('nextworld'):
    worlds.append(item)
world.close()
for item in worlds:
    worldtemp=open(os.path.expanduser(item))
    worlditemtemp=[]
    for item in worldtemp.split(','):
        worlditemtemp.append(item)
    worlditems.append(worlditemtemp)
#####Example worlds file
####Name: snowy.wrd
####snowy,2,example1-example2
#####Example ~/.ealagse/TheGame/world/worldlist.tgc
####~/.ealgase/TheGame/world/snowy.wrdnextworld~/.ealgase/TheGame/world/dry.wrdnextworld~/.ealgase/TheGame/world/main.wrd
for item in worlditems:
    worldtemplist=[]
    worldtemplist.append(item[0])
    for item1 in item[2]:
        itemsplit=item1.split('-')
        worldtemplist.append(itemsplit)
    worldreallist.append(worldtemplist)
worldtuples=[]
for item in worldreallist:
    worldtuplestemp.append(item[0])
    i=0
    for item1 in item:
       i+=1
       worldtuplestemptemp=[]
       if i==1:
           pass
       else:
           worldtuplestemptemp.append(item1)
    worldtuplestemp.append(worldtuplestemptemp)
    worldtuples.append(worldtuplestemp)
game=1
world=0
worldrange=len(worldtuples)
while game==1:
    worldchange=random.randint(1,100)
    if worldchange==1:
        world=random.randint(0,worldrange-1)
        print("Changing world to "+worldtuples[world][0]+".")
        xp+=20
    worldtouse=worldtuples[world][1]
    moves=len(worldtouse-1)
    move=random.randint(0,moves)
    runworld(worldtouse[move])
