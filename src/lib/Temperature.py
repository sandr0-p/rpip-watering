from machine import Pin, I2C
import utime
import AM2320


class Temperature:

    sensor: AM2320.AM2320 = AM2320.AM2320()
    lastRead: int = -1

    def __init__(self, sda: int = 18, scl: int = 19, i2c: int = 1) -> None:
        self.sensor = AM2320.AM2320(I2C(i2c, sda=Pin(sda), scl=Pin(scl)))

    def ReadTemperatur(self) -> float:
        self.Measure()
        return self.sensor.temperature()

    def ReadHumidity(self) -> float:
        self.Measure()
        return self.sensor.humidity()

    def Measure(self) -> None:
        if (utime.time() - self.lastRead) > 60 or self.lastRead == -1:
            self.sensor.measure()
            self.lastRead = utime.time()
