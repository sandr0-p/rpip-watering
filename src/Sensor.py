import _thread
from machine import Pin
import utime
import RGB1602
import Temperature
import Light
import Moisture

lcd = RGB1602.RGB1602(16, 2)
temperature = Temperature.Temperature()
light = Light.Light()
moisture = Moisture.Moisture()

pump = Pin(15, Pin.OUT)


def Pump() -> None:
    moist = moisture.ReadPercent()
    print(moist)
    if moist < 50:
        pump.on()
        utime.sleep(5)
        pump.off()
    utime.sleep(10)


_thread.start_new_thread(Pump, ())

while True:
    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout("Soil Moisture")
    lcd.setCursor(0, 1)
    lcd.printout(f'{moisture.ReadPercent()} %')
    utime.sleep(5)

    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout("Temperature")
    lcd.setCursor(0, 1)
    lcd.printout(f'{temperature.ReadTemperatur()} C')
    utime.sleep(5)

    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout("Humidity")
    lcd.setCursor(0, 1)
    lcd.printout(f'{temperature.ReadHumidity()} %')
    utime.sleep(5)

    lcd.clear()
    lcd.setCursor(0, 0)
    lcd.printout("Light Level")
    lcd.setCursor(0, 1)
    lcd.printout(f'{light.ReadVolt()} V')
    utime.sleep(5)

    for i in range(60):
        lcd.clear()
        lcd.setCursor(0, 0)
        lcd.printout(f'T-{60-i} seconds')
        utime.sleep(1)
