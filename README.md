
# piMpc

This script `ptouch.py` define 12 function on 6 button on Touch Phat. It detect short and long press on a button.

## About

The music player in my car is a crap. I decide to replace it by a mpc deamon.

This project run on a RaspberryPi 3 with Rasbian Lite (without gui).
I use a Phat DAC for improve audio quality (link at end) and Phat Touch for player control.

The raspberry is turned on at car unlock and take 13 seconds to begin to play music. 

## Button attribution

 ### Touch Enter :
 - Short press : Previous Song
 -  Long press : Toggle Play/Pause
 
 ### Touch Back :
 - Short press : Next Song
 -  Long press : Unused
 
 ### Touch A, B, C, D :
 - Short press : Play some genre of music
 -  Long press : Play a led animation
 
 ## Hardware 
 https://shop.pimoroni.com/products/touch-phat
 https://shop.pimoroni.com/products/phat-dac
 
## Documentation

https://learn.pimoroni.com/tutorial/phat/raspberry-pi-phat-dac-install
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-touch-phat
http://docs.pimoroni.com/touchphat/
https://github.com/pimoroni/touch-phat
