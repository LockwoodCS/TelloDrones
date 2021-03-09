from djitellopy import tello
from threading import Thread
from time import sleep
import cv2
me = tello.Tello()

me.connect()

print(me.get_battery())
global img


me.streamon()
sleep(10)

img = me.get_frame_read().frame

# img = cv2.resize(img, (360, 240))

cv2.imshow("Drone Stream", img)

cv2.waitKey(1)

me.takeoff()

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
me.land()

cv2.destroyAllWindows()

