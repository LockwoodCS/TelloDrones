from djitellopy import tello
import cv2
from time import sleep

me = tello.Tello()

me.connect()

print(me.get_battery())
global img
me.streamon()
d = 0
while d<15: #takes 15 images

    img = me.get_frame_read().frame

    img = cv2.resize(img, (360, 240))

    cv2.imshow("Drone Stream", img)
    filename = "C:\\Users\\jlockwood\\PycharmProjects\\TelloDroneProject\\images\\image_%d.jpg"%d #saves images to a file path with a image_# naming
    cv2.imwrite(filename, img)
    cv2.waitKey(1)
    sleep(5) #sets the delay between taking images
    d+=1
    if d ==15:
        break
