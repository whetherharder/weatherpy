from unittest import TestCase
from ..service import IWeatherInfo
from ..service import WeatherInfo
from ..service import WeatherSevice

from nose import with_setup

city = 'Moscow'


class TestWeatherService(TestCase):
    def setUp(self):
        self.service = WeatherSevice()

    def test_get_weather_by_city_not_none(self):
        info = self.service.get_info(city)
        self.assertIsNotNone(info)

    def test_get_weather_by_city_is_weatherinfo(self):
        info = self.service.get_info(city)
        self.assertIsInstance(obj=info, cls=IWeatherInfo)
