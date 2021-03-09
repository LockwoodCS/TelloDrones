from djitellopy import tello

from time import sleep

me = tello.Tello()

me.connect()

print(me.get_battery())

me.takeoff()


me.send_rc_control(0, 50, 0, 0) #Move forward with 50% speed

sleep(3) #Executes the above command for 3 seconds

me.send_rc_control(0, 0, 0, 0) #Gets drone to stop moving before landing

me.land()