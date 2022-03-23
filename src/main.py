from uos import mkdir
import utime
from uio import TextIOWrapper
from machine import Pin

from FIT800 import FIT800
from Light import Light
from Moisture import Moisture
from RGB1602 import RGB1602
from Reading import Reading
from Temperature import Temperature

led = Pin(25, Pin.OUT)

# lcd = RGB1602(16, 2)
temperature = Temperature()
light = Light()
moisture = Moisture()
pump = FIT800(15, 3.3)
reading = Reading()
log: TextIOWrapper

#try:
#    log = open("log/log.txt", "a")
#except OSError:
#    mkdir("log")
#    log = open("log/log.txt", "w")
#    log.write(reading.GetHeader())

def Blink():
    led.on()
    utime.sleep(0.5)
    led.off()

while True:
#    try:
        # Get readings
        reading = Reading()
        reading.humidity = temperature.ReadHumidity()
        reading.light = light.ReadVolt()
        reading.moisture = moisture.ReadPercent()
        reading.temperatur = temperature.ReadTemperatur()
        reading.time = utime.time()
        log.write(reading.ToCSV())
    
        Blink()
        utime.sleep(1)
#    except:
#        ex = sys.exc_info()[0]
#        log.write(f'Error: {ex}')

    # lcd.clear()
    # lcd.setCursor(0, 0)
    # lcd.printout("Soil Moisture")
    # lcd.setCursor(0, 1)
    # lcd.printout(f'{moisture.ReadPercent()} %')
    # utime.sleep(5)

    # lcd.clear()
    # lcd.setCursor(0, 0)
    # lcd.printout("Temperature")
    # lcd.setCursor(0, 1)
    # lcd.printout(f'{temperature.ReadTemperatur()} C')
    # utime.sleep(5)

    # lcd.clear()
    # lcd.setCursor(0, 0)
    # lcd.printout("Humidity")
    # lcd.setCursor(0, 1)
    # lcd.printout(f'{temperature.ReadHumidity()} %')
    # utime.sleep(5)

    # lcd.clear()
    # lcd.setCursor(0, 0)
    # lcd.printout("Light Level")
    # lcd.setCursor(0, 1)
    # lcd.printout(f'{light.ReadVolt()} V')
    # utime.sleep(5)

    # for i in range(60):
    #     lcd.clear()
    #     lcd.setCursor(0, 0)
    #     lcd.printout(f'T-{60-i} seconds')
    #     utime.sleep(1)
