import utime
from machine import ADC


class Moisture:
    min: int
    max: int
    sensor: ADC
    conversion_factor = 3.3 / (65535)
    lastRead = -1
    lastMeasure = 0

    def __init__(self, adc: int = 26, min: int = 18657,  max: int = 48488) -> None:
        self.min = min
        self.max = max
        self.sensor = ADC(adc)

    def ReadPercent(self) -> int:
        self.Read()
        result: float = ((self.lastMeasure - self.max)
                         * 100) / (self.min - self.max)
        if result > 100:
            result = 100
        elif result < 0:
            result = 0
        return round(result)

    def ReadVolt(self) -> float:
        self.Read()
        return self.lastMeasure * self.conversion_factor

    def ReadRaw(self) -> float:
        self.Read()
        return self.lastMeasure

    def Read(self) -> None:
        if (utime.time() - self.lastRead) > 60 or self.lastMeasure == -1:
            self.lastMeasure = self.sensor.read_u16()
