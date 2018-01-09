import unittest

from weather import CityWeather

#test class for CityWeather class
class TestCityWeather(unittest.TestCase):

    def setUp(self):
        '''
        Intializes the CityWeather class 
        '''
        self.weather = CityWeather()
    
    def test_for_invalid_city_name(self):
        '''
        test for invalid city 
        '''
        return self.assertEqual(self.weather.getMaxTemp('sssssssssssssssss'),'Invalid City Name', msg=None)

    def test_for_invalid_input_type(self):
        '''
        Test for invalid input type
        '''
        return self.assertRaises(self.weather.getPressure(34.0))

    def test_for_return_type(self):
        '''
        Tests for correct return type
        '''
        return self.assertEqual(type(self.weather.getMinTemp('Nakuru')),type(10.0),msg='Invalid return type')


if __name__ == '__main__':
    unittest.main()
        