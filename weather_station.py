"""
Weather station module.

Containing parent class and som child classes with implementation for temperature and rain.
"""

class WeatherStation:
    def __init__(self, name: str, longitude: float, latitude: float):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.unit = "not defined"

    def read_data(self) -> float:
        raise NotImplementedError("Child classes must implement read_data()")

    def convert_unit(self, value: float) -> float:
        return value  # Default: no conversion

    def report(self) -> str:
        raw_value = self.read_data()
        converted_value = self.convert_unit(raw_value)
        return (
            f"Weather station {self.name} at ({self.longitude}, {self.latitude}) "
            f"reports value: {converted_value:.2f} {self.unit}"
        )


class TemperatureSensor(WeatherStation):

    def _generate_temperature_data_in_kelvin(self) -> float:
        return 293.15  # Constant for this example


class RainGauge(WeatherStation):

    def _generate_rain_data_in_mm(self) -> float:
        return 10.0  # Constant for this example

def simulate_reports(stations: list[WeatherStation]) -> list[str]:
    return [station.report() for station in stations]
