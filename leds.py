from ev3dev2.led import Leds
import time
Leds = Leds()
while True:
  leds.set_color("RIGHT", "RED")
  time.sleep(1)
  leds.set_color("LEFT", "AMBER")
