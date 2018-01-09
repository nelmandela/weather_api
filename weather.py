from __future__ import unicode_literals 
import json
import requests

#The class uses an public api from open weather map to get pressure,Maximum Temperatue, Minumun Temperature,Average Temperature
class CityWeather(object):
    __api_key = ''
    def __init__(self):
        self.__api_key = '98ea758ea09a1eebebf210af33fb25f5'


    def getData(self,city):
        '''
        The Get data from openweathermap.org and converts it into a dictionary
        '''

        return json.loads(requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+",uk&appid="+self.__api_key).text)     

    def getPressure(self,city):
        '''
        The function gets pressure of a city
        Usage: >>> getPressure('Nairobi')
               >>> 66.8
        '''
        try:
            return self.getData(city)['main']['pressure']  
        except Exception as e:
            return "Invalid City Name"


    def getMaxTemp(self,city):
        '''The function gets pressure of a city
        Usage: >>> getMaxTemp('Nairobi')
               >>> 66.8
        '''
        try:
            return 9/5 * (float(self.getData(city)['main']['temp_max']) - 273) + 32
        except Exception as e:
            return "Invalid City Name"

    def  getMinTemp(self,city):
        '''The function gets pressure of a city
        Usage: >>> getMinTemp('Nairobi')
               >>> 66.8
        '''
        try:
            return   9/5 * (float(self.getData(city)['main']['temp_min']) - 273) + 32
        except Exception as e:
            return "Invalid City Name"
    def getTemp(self,city):
        '''The function gets pressure of a city
        Usage: >>> getTemp('Nairobi')
               >>> 66.8
        '''
        try:
            return 9/5 * (float(self.getData(city)['main']['temp']) - 273) + 32
        except Exception  as e:
            return "Invalid City Name"

# git = CityWeather()
# print(git.getTemp('Nairobi, Kenya'))
# print(git.getMinTemp('Kisumu'))
# print(git.getPressure('Kisumu'))
# print(git.getMaxTemp('Kisumu'))
