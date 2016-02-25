import pygame
import hcsr04sensor.sensor as eyes
import microstacknode.hardware.gps.l80gps as mst
gps = mst.L80GPS()
coords = gps.get_gpgll()
from pygame.locals import *
from sense_hat import SenseHat
sh = SenseHat()
TRIG = 20
ECHO = 21
TEMP =20
pygame.init()
pygame.display.set_mode((640, 480))

def sonic():
    d = eyes.Measurement(TRIG,ECHO,TEMP, 'metric', 1)
    sh.show_message(str(round(d.raw_distance(sample_size=3), 0)))#int(raw_input())))
def humidity():
    h = sh.get_humidity()
    sh.show_message(str(int(h)))

def pressure():
    p = sh.get_pressure()
    sh.show_message(str(int(p)))


def temp():
    t = sh.get_temperature()
    sh.show_message(str(int(t)))

def gps():
    
    lat = coords['latitude']
    lon = coords['longitude']
    sh.show_message(str(round(float(lat), 4)))
    sh.show_message(str(round(float(lon), 4)))
    print(lat, lon)


while True:
    
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                temp()
            elif event.key == K_UP:
                humidity()
            elif event.key == K_LEFT:
                pressure()
            elif event.key == K_RETURN:
                sonic()
            elif event.key == K_RIGHT:
                gps()
