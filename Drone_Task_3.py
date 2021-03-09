from djitellopy import tello
import DroneFunctions as df
from time import sleep
global speed
me = tello.Tello()

def forward(x):
    time = x/20
    me.send_rc_control(0, 50, 0, 0)
    sleep(time)


me.connect()
me.takeoff()
sleep(5)
df.forward(30)
sleep(5)
me.land()




