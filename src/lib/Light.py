from machine import ADC


class Light:
    sensor: ADC
    conversion_factor = 3.3 / (65535)

    def __init__(self, pin: int = 27) -> None:
        self.sensor = ADC(pin)

    def ReadRaw(self) -> int:
        """Returns the raw value of the light sensor"""
        return self.sensor.read_u16()

    def ReadVolt(self) -> float:
        """Return the value of the light sensor as Volt"""
        return self.sensor.read_u16()*self.conversion_factor
