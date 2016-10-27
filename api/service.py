from abc import ABCMeta, abstractmethod, abstractproperty


class WeatherSevice:
    def get_info(self, city):
        info = WeatherInfo()
        return info


class IWeatherInfo():
    __metaclass__ = ABCMeta

    @abstractproperty
    def temperature(self):
        pass


class WeatherInfo(IWeatherInfo):
    temperature = None

    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature


class Temperature(object):
    pass
