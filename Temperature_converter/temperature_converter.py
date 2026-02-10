class TemperatureConverter:
    temperature: float
    def __init__(self):
        self.temperature = 0.0

    def setTemperature(self, temp: float) -> None:
        self.temperature = float(temp)

    def toCelsius(self) -> float:
        return self.temperature

    def toFahrenheit(self) -> float:
        return (self.temperature * 9 / 5) + 32

    def toKelvin(self) -> float:
        return self.temperature + 273.15
