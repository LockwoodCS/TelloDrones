from djitellopy import TelloSwarm
from time import sleep

swarm = TelloSwarm.fromIps([
    "192.168.178.42",
    "192.168.178.43",
    "192.168.178.44"])


swarm.connect()
swarm.takeoff()
sleep(10)
swarm.land()
swarm.end()

