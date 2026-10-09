"""IoT Smart Home Automation - Raspberry Pi Pico W (MicroPython + Blynk)

- Reads temperature and humidity from a DHT11 sensor and sends them to Blynk
- Switches a bulb and a fan through a 2-channel relay module from the Blynk app

Blynk datastreams (change to match your Blynk template):
    V0 temperature (read)   V1 humidity (read)   V2 bulb switch   V3 fan switch
Wiring (change pins to match your circuit):
    DHT11 DATA -> GP16   Relay IN1 (bulb) -> GP14   Relay IN2 (fan) -> GP15
Copy BlynkLib.py (github.com/blynkkk/lib-python) and secrets.py onto the Pico W.
"""
import time

import BlynkLib
import dht
import network
from machine import Pin

from secrets import BLYNK_AUTH, WIFI_PASSWORD, WIFI_SSID

RELAY_ACTIVE_LOW = True  # most relay modules switch ON when the pin is LOW

bulb = Pin(14, Pin.OUT)
fan = Pin(15, Pin.OUT)
sensor = dht.DHT11(Pin(16))


def set_relay(pin, on):
    pin.value((not on) if RELAY_ACTIVE_LOW else on)


def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        time.sleep(1)
    print("Connected:", wlan.ifconfig()[0])


set_relay(bulb, False)  # start with everything OFF
set_relay(fan, False)
connect_wifi()
blynk = BlynkLib.Blynk(BLYNK_AUTH)


@blynk.on("V2")
def bulb_handler(value):
    set_relay(bulb, int(value[0]) == 1)


@blynk.on("V3")
def fan_handler(value):
    set_relay(fan, int(value[0]) == 1)


last_read = 0
while True:
    blynk.run()
    if time.ticks_diff(time.ticks_ms(), last_read) > 5000:  # every 5 s
        last_read = time.ticks_ms()
        try:
            sensor.measure()
            blynk.virtual_write(0, sensor.temperature())
            blynk.virtual_write(1, sensor.humidity())
        except OSError:
            print("DHT11 read failed")
