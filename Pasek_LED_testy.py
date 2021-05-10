"""
from machine import Pin
from neopixel import NeoPixel
pin = Pin(0, Pin.OUT)    # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 8)    # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (255, 255, 255)  # set the first pixel to white
np.write()               # write data to all pixels
r, g, b = np[0]          # get first pixel colour
"""
# Można dodać później element specyfikacji urządzenia do odpowiedniej długości 
# ramion, czas działania itp.

import time
from time import sleep
# później zaimportować


def change_all(r, g, b):
    """
    for i in range(0, 8):
        np[i] = (r, g, b)
    """
    print(f"Pasek się świeci, kolor:({r}, {g}, {b})")
    return
# przypisanie zmiennych do testu


max_push = 80
min_push = 20
push_ups_numerator = 0
number = 5
pushing_up = 0  # 1 przy wznoszeniu się, 0 przy opadaniu
for i in range(100):  # Ma być 1200 razy
    distance = int(input("Podaj dystans: "))
    proste_plecy = int(input("Czy plecy są proste: "))
    if proste_plecy == 1:
        # sekcja odpowiedzialna za sygnalizację wykonania pompki
        if pushing_up == 0:
            if distance < min_push:
                change_all(255, 255, 0)
                push_ups_numerator += 1
                pushing_up = 1
        else:
            if distance > max_push:
                change_all(255, 255, 0)
                pushing_up = 0
    elif proste_plecy == 0:
        change_all(255, 0, 0)
    if push_ups_numerator == number:
        change_all(0, 255, 0)
    # np.write()
    time.sleep(0.050)

