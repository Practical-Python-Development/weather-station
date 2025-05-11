"""
Weather station module.

Containing parent class and som child classes with implementation for temperature and rain.
"""

class WeatherStation:
    ...


class TemperatureSensor(WeatherStation):

    def _generate_temperature_data_in_kelvin(self) -> float:
        return 293.15  # Constant for this example


class RainGauge(WeatherStation):

    def _generate_rain_data_in_mm(self) -> float:
        return 10.0  # Constant for this example

def simulate_reports(stations: list[WeatherStation]) -> list[str]:
    return [station.report() for station in stations]
