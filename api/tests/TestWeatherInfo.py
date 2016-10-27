from unittest import TestCase

from api.service import Temperature
from ..service import WeatherInfo


class TestWeatherInfo(TestCase):
    def setUp(self):
        self.temperature = Temperature()

    def test_get_temperature_is_temperature(self):
        info = WeatherInfo(self.temperature)
        temperature = info.get_temperature()
        self.assertIsInstance(temperature, Temperature)
