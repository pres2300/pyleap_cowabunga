import board
import digitalio
import time
import neopixel
from adafruit_ble import BLERadio

radio = BLERadio()
print("scanning")
for entry in radio.start_scan(timeout=10, minimum_rssi=-80):
    name = entry.complete_name
    if name !=None:
        print(name)

print("scan done")


led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)


while True:
    led.value = True
    pixels[0] = (0, 10, 0)
    time.sleep(1)
    led.value = False
    pixels[0] = (10, 0, 0)
    time.sleep(1)

