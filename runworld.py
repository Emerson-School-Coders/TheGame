#Runworld.py
#created by ealgase
#Learn how to make a world
#-------------------------
import time,random,os
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
        livesfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/lives.tgs"),'x')
        goldfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/gold.tgs"),'x')
        damagemfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/damagem.tgs"),'x')
        healthmfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/healthm.tgs"),'x')
        ebhealthfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/ebhealth.tgs"),'x')
        specialfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/special.tgs"),'x')
        xpfile1=open(os.path.expanduser("~/.ealgase/TheGame/saves/xp.tgs"),'x')
        lives=1
        gold=1
        damagem=1
        healthm=1
        ebhealth=0
        xp=0
        special=[]
        save()
        livesfile1.close()
        goldfile1.close()
        damagemfile1.close()
        healthmfile1.close()
        ebhealthfile1.close()
        specialfile1.close()
        xpfile1.close()
def runworld(world):
    load()
    worldfile=open(os.path.expand("~/.ealgase/TheGame/world"))
    for line in worldfile:
        if line[:3]=='xp,':
            xp+=int(line[3:])
        elif line[:4]=='say,':
            print(line[4:])
        elif line[:5]=='gold,':
            gold+=int(line[5:])
        elif line[:8]=='damagem,':
            damagem+=int(line[8:])
        elif line[:8]=='healthm,':
            health+=int(line[8:])
        elif line[:9]=='ebhealth,':
            damagem+=int(line[9:])
        elif line[:8]=='special,':
            special.append(line[8:])
