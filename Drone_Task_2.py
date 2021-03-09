from djitellopy import tello

from time import sleep

me = tello.Tello()

me.connect()

print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 0, 20, 0)
sleep(2)

me.send_rc_control(0, 0, 0, 0)
sleep(1)

n = int(0)
size = int(1)
while n <= 2:
    print(n)
    n+=1
    size +=1
    me.send_rc_control(0, 40, 0, 0)
    sleep(size)
    me.send_rc_control(0, 0, 0, 0)
    sleep(1)

    me.send_rc_control(0, 0, 40, 0)
    sleep(size)
    me.send_rc_control(0, 0, 0, 0)
    sleep(1)

    me.send_rc_control(0, -40, 0, 0)
    sleep(size)
    me.send_rc_control(0, 0, 0, 0)
    sleep(1)

    me.send_rc_control(0, 0, -40, 0)
    sleep(size)
    me.send_rc_control(0, 0, 0, 0)
    sleep(1)


else:
    me.send_rc_control(0, 0, 0, 100)
    sleep(4)
    me.send_rc_control(0, 0, 0, 0)
    sleep(3)
    me.land()
