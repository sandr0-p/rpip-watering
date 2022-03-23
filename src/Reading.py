class Reading:
    humidity: float
    light: float
    moisture: int
    temperatur: float
    time: int

    def GetHeader(self) -> str:
        """
        Returns the CSV header string for this class
        """
        output = "Time,"
        output += "Moisture,"
        output += "Temperature,"
        output += "Humidity,"
        output += "Light\n"
        return output

    def ToCSV(self) -> str:
        """
        Returns all values as a CSV string including a line break.
        Resets all values to -1
        """
        output = f'{self.time},'
        output += f'{self.moisture},'
        output += f'{self.temperatur},'
        output += f'{self.humidity},'
        output += f'{self.light}\n'

        self.humidity = -1
        self.light = -1
        self.moisture = -1
        self.temperatur = -1

        return output
