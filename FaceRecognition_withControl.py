from djitellopy import tello

import KeypressModule as kp

from time import sleep
import time
import cv2

d = 0
kp.init()

me = tello.Tello()

me.connect()

print(me.get_battery())
global img
me.streamon()

def getKeyboardInput():

    lr, fb, ud, yv = 0, 0, 0, 0

    speed = 50

    if kp.getKey("LEFT"):lr = -speed
    elif kp.getKey("RIGHT"): lr = speed
    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed
    if kp.getKey("w"):ud = speed
    elif kp.getKey("s"):ud = -speed
    if kp.getKey("a"):yv = -speed
    elif kp.getKey("d"): yv = speed
    if kp.getKey("q"): me.land();sleep(3)
    if kp.getKey("e"): me.takeoff()

    return [lr, fb, ud, yv]
w, h = 360, 240

fbRange = [6200, 6800]

pid = [0.5, 0.5, 0]

pError = 0

def findFace(img):

    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListC = []

    myFaceListArea = []

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cx = x + w // 2

        cy = y + h // 2

        area = w * h

        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

        myFaceListC.append([cx, cy])

        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:

        i = myFaceListArea.index(max(myFaceListArea))

        return img, [myFaceListC[i], myFaceListArea[i]]

    else:

        return img, [[0, 0], 0]


while True:

    vals = getKeyboardInput()

    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame

    img = me.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info = findFace(img)

    cv2.imshow("Drone Stream", img)

    cv2.waitKey(1)
    sleep(0.05)
