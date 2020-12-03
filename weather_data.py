from requests import get


class WeatherData:
    __WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q=' \
                    '{city_name}&appid={API_KEY}&units=metric'

    def __init__(self, api_key):
        self.__API_KEY = api_key

    def __get_temperature_data(self, city_name='Tomsk'):
        response = get(url=self.__WEATHER_URL.format(API_KEY=self.__API_KEY,
                                                     city_name=city_name))
        self.__weather_data = response.json()

    def get_temperature_in_celsius(self, city_name):
        self.__get_temperature_data(city_name=city_name)
        try:
            return self.__weather_data['main']['temp']
        except KeyError:
            return 'Введено некорректное название города !'

