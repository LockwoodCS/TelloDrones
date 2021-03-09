from djitellopy import tello
me = tello.Tello()
from time import sleep


def forward(x):
    time = x/20
    me.send_rc_control(0, 50, 0, 0)
    sleep(time)


