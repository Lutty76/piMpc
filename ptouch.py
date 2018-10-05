import sys
import time
import touchphat
import os
import subprocess

button = {'Back':0,'A':0,'B':0,'C':0,'D':0,'Enter':0}
longPress = {'Back':False,'A':False,'B':False,'C':False,'D':False,'Enter':False}
lost = True

@touchphat.on_touch(['Back','A','B','C','D','Enter'])
def handle_touch(event):
    global button
    global longPress 
    start = time.time()
    pressed = True
    button[event.name] = time.time()
    longPress[event.name] = False

@touchphat.on_release(['Back','A','B','C','D','Enter'])
def handle_release(event):
    global button
    global longPress
    touchphat.led_off(event.name)
    button[event.name]=0
    handle_button(event.pad,longPress[event.name])

def handle_button(button,longPress):
    switcher={
            0:lambda: "Not a button",
            1:handle_enter,
            2:handle_a,
            3:handle_b,
            4:handle_c,
            5:handle_d,
            6:handle_back
            }
    switcher.get(button,lambda: "Invalid button")(longPress)

def handle_enter(longPress):
    if longPress:
        os.system('mpc toggle')
    else:
        os.system('mpc prev')

def handle_back(longPress):
    if longPress:
        os.system('mpc toggle')
    else:
        os.system('mpc next')

def handle_a(longPress):
    if longPress:
        k2000()
    else:
        os.system('mpc clear')
        os.system('mpc findadd genre Metal')
        os.system('mpc findadd genre \'Hard Rock\'')
        os.system('mpc findadd genre Classical')
        os.system('mpc play')
        touchphat.all_off()
        touchphat.led_on("A")

def handle_b(longPress):
    if longPress:
        center()
    else:
        os.system('mpc clear')
        os.system('mpc findadd genre Rock')
        os.system('mpc findadd genre Blues')
        os.system('mpc play')
        touchphat.all_off()
        touchphat.led_on("B")

def handle_c(longPress):
    if longPress:
        cycle()
    else:
        os.system('mpc clear')
        os.system('mpc findadd genre Metal')
        os.system('mpc findadd genre \'Hard Rock\'')
        os.system('mpc findadd genre Classical')
        os.system('mpc findadd genre Rock')
        os.system('mpc findadd genre Blues')
        os.system('mpc play')
        touchphat.all_off()
        touchphat.led_on("C")

def handle_d(longPress):
    if longPress:
        christmas()
    else:
        os.system('mpc clear')   
        os.system('mpc ls |mpc add')   
        os.system('mpc play')
        touchphat.all_off()
        touchphat.led_on("D")

def center():
    i=6
    while i>0:
        touchphat.all_off()
        touchphat.led_on(1)
        touchphat.led_on(6)
        time.sleep(0.12)
        touchphat.all_off()
        touchphat.led_on(2)
        touchphat.led_on(5)
        time.sleep(0.12)
        touchphat.all_off()
        touchphat.led_on(3)
        touchphat.led_on(4)
        time.sleep(0.12)
        i-=1
    global lost
    lost = True

def christmas():
    i=6
    while i>0:
        touchphat.all_off()
        touchphat.led_on(1)
        touchphat.led_on(3)
        touchphat.led_on(5)
        time.sleep(0.24)
        touchphat.all_off()
        touchphat.led_on(2)
        touchphat.led_on(4)
        touchphat.led_on(6)
        time.sleep(0.24)
        i-=1
    global lost
    lost = True

def cycle():
    i=3
    while i>0:
        for pad in ['Back','A','B','C','D','Enter']:
            touchphat.led_on(pad)
            time.sleep(0.12)
            touchphat.led_off(pad)
        i-=1
    global lost
    lost = True
    
def k2000():
    i=2
    while i>0:
        for pad in ['Back','A','B','C','D','Enter','D','C','B','A']:
            touchphat.led_on(pad)
            time.sleep(0.12)
            touchphat.led_off(pad)
        i-=1
    global lost
    lost = True
    
try:
    while True:
        if lost:
            lost = False
            p = subprocess.Popen(['mpc', 'playlist', '-f', '%genre%'],stdout=subprocess.PIPE)
            listGenre = subprocess.check_output(('sort','-u'), stdin=p.stdout).split('\n')
            touchphat.all_off()
            if 'Fusion' in listGenre :
                touchphat.led_on('D')
            elif 'Rock'  in listGenre and 'Classical' in listGenre :
                touchphat.led_on('C')
            elif 'Rock'  in listGenre :
                touchphat.led_on('B')
            else:
                touchphat.led_on('A')
           
        for pad in ['Back','A','B','C','D','Enter']:
            if button[pad] != 0:
                runtime = (time.time() - button[pad])
                if runtime > 0.5:
                    touchphat.led_on(pad)
                    longPress[pad] = True
                else:
                    touchphat.led_off(pad)
                
        time.sleep(0.1)
except KeyboardInterrupt():
    sys.exit()

