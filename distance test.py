from djitellopy import tello
from time import sleep
global speed

speed = 50


me = tello.Tello()
me.connect()
me.takeoff()


me.send_rc_control(0, 0, 0, 0)
sleep(30)

me.land()