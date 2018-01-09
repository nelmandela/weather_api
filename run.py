#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.
Usage:
    weather_app minimumtempreture <city>
    weather_app tempreture <city> 
    weather_app maximumtempreture <city> 
    weather_app pressure <city>
    weather_app (-i | --interactive)
    weather_app (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""
import sys
import cmd
from docopt import docopt, DocoptExit
from weather import CityWeather
city_weather = CityWeather()
def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    intro = 'Welcome to City Weather commandline application.'
    prompt = '>>> '
    file = None


    @docopt_cmd
    def do_pressure(self,arg):
        """Usage: pressure <city>"""
        print(city_weather.getPressure(arg['<city>']))

    @docopt_cmd
    def do_tempreture(self,arg):
        """Usage: tempreture <city>"""
        print(city_weather.getTemp(arg['<city>']))


    @docopt_cmd
    def do_minimumtempreture(self,arg):
        """Usage: minimumtempreture <city>"""
        print(city_weather.getMinTemp(arg['<city>']))

    @docopt_cmd
    def do_maximumtempreture(self,arg):
        """Usage: maximumtempreture <city>"""
        print(city_weather.getMaxTemp(arg['<city>']))

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    MyInteractive().cmdloop()

print(opt)