import sys
sys.path.append("./usr/local/lib/python3.9/dist-packages")
import usb.core
import board
import neopixel
import time
import USB_Device as dev
import XBox360_Driver as xb3d
import XBoxOne_Driver as xb1d
import Gamecube_Driver as gcd
import Goodwill_Driver as sd
import Dictionaries as dicts
import Light as light
import Input as inp
import random
import ColorCycling as cc
import Ripple as rip

NUMBER_OF_BACK_LIGHTS = 258
NUMBER_OF_FRONT_LIGHTS = 80
WHITE = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
OFF = (0, 0, 0)
PIANO_WIDTH = 1287

inputs = []
active_inputs = []
beams = []
back_pixels = neopixel.NeoPixel(board.D18, NUMBER_OF_BACK_LIGHTS)
front_pixels = neopixel.NeoPixel(board.D21, NUMBER_OF_FRONT_LIGHTS)
back_lights = []
front_lights = []
ripples = []

back_pixels.fill(RED)
front_pixels.fill(RED)
time.sleep(0.333)
back_pixels.fill(GREEN)
front_pixels.fill(GREEN)
time.sleep(0.333)
back_pixels.fill(BLUE)
front_pixels.fill(BLUE)
time.sleep(0.333)
back_pixels.fill(OFF)
front_pixels.fill(OFF)

for l in range(NUMBER_OF_BACK_LIGHTS):
    back_lights.append(light.Light(l, back_pixels, dicts.back_light_index_to_position[l]))

for l in range(NUMBER_OF_FRONT_LIGHTS):
    front_lights.append(light.Light(l, front_pixels))

for i in range(79):
    inputs.append(inp.Input(i))

xb360 = dev.Device(0x20d6, 0x200e, 0, 1)
xb1 = dev.Device(0x24c6, 0x541a, 0, 1)
gc1 = dev.Device(0x20d6, 0xa711, 0, 1)
gc2 = dev.Device(0x20d6, 0xa711, 0, 1, 1)
sc = dev.Device(0x0428, 0x4001, 0, 0)

cycler = cc.color_cycler()

def activate_inputs(readout, dictionary):
    for r in readout:
        index = dictionary[r]
        i = inputs[index]
        i.activate()

front_pixels.fill(GREEN)
back_pixels.fill(GREEN)
time.sleep(1)
front_pixels.fill(OFF)
back_pixels.fill(OFF)


while True:
    cycler.shift_color()
    #front_pixels.fill(cycler.get_color())
    active_inputs.clear()
    if len(ripples) < 5:
        r1 = xb3d.parse_input(xb360.get_device_readout())
        r2 = gcd.parse_input(gc1.get_device_readout())
        r3 = gcd.parse_input(gc2.get_device_readout())
        r4 = sd.parse_input(sc.get_device_readout())
        r5 = xb1d.parse_input(xb1.get_device_readout())
        activate_inputs(r1, dicts.xbox_360_buttons_to_index)
        activate_inputs(r2, dicts.gamecube_1_buttons_to_index)
        activate_inputs(r3, dicts.gamecube_2_buttons_to_index)
        activate_inputs(r4, dicts.goodwill_buttons_to_index)
        activate_inputs(r5, dicts.xbox_1_buttons_to_index)
        for i in inputs:
            if i.is_active():
                active_inputs.append(i)
            i.iterate()
            #print("Index: " + str(i.get_index()))
        #print("Number of active inputs: " + str(len(active_inputs)))
        #z = False
        for a in active_inputs:
            #beams.append(bm.LeftBeam(a.get_position()))
            #beams.append(bm.RightBeam(a.get_position()))
            for x in range(4):
                r = random.randint(0, NUMBER_OF_BACK_LIGHTS - 1)
                back_lights[r].toggle(cycler.get_color())
            if len(ripples) < 5:
                ripples.append(rip.Ripple(dicts.input_index_to_front_light_index[a.get_index()]))

    front_pixels.fill(OFF)
    for r in reversed(ripples):
        if r.left < NUMBER_OF_FRONT_LIGHTS:
            front_pixels[r.left] = cycler.get_color()
        if r.right >= 0:
            front_pixels[r.right] = cycler.get_color()
        r.iterate()
        if r.left >= NUMBER_OF_FRONT_LIGHTS and r.right < 0:
            ripples.remove(r)

            #if lights[r].is_on():
            #    active_lights.append(r)
            #else:
            #    active_lights.remove(r)
        #if (z == False):
        #    c = cycler.get_color()
        #    for l in active_lights:
        #        pixels[l] = c
        #    z = True
