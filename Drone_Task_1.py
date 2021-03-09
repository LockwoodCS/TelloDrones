from djitellopy import tello

from time import sleep

me = tello.Tello()

me.connect()

print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 0, 0, 0)
sleep(1)


#fly forward

me.send_rc_control(0, 40, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(1)
#Fly up

me.send_rc_control(0, 0, 40, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(1)

#Fly down and forward
me.send_rc_control(0, 60, -40, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(1)

#Fly up and forward

me.send_rc_control(0, 40, 60, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
sleep(1)

me.flip_forward()
sleep(1)


me.land()