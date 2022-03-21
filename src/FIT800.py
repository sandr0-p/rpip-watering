import utime
from machine import Pin


class FIT800:

    voltage: float
    pump: Pin
    ml_s_V: float = 6.6

    def __init__(self, pin: int, voltage: float) -> None:
        """
        :param pin: The pin that controls the pump
        :type pin: int
        :param voltage: The voltage that drives the pump. This might be different from the Pin and MCU voltage if external power is used.
        :type voltage: int
        """
        self.voltage = voltage
        self.pump = Pin(pin, Pin.OUT)

    def on(self) -> None:
        """
        Turns the pump on and leaves it on.
        """
        self.pump.on()

    def off(self) -> None:
        """
        Turns the pump off.
        """
        self.pump.off()

    def drain_ml(self, drain: float) -> None:
        """
        Drains the given amount of milliliters

        :param drain: The amount of water that should be drained
        :type drain: float
        """
        ml_s: float = self.ml_s_V * self.voltage
        duration: float = drain / ml_s
        self.on()
        utime.sleep(duration)
        self.off()
