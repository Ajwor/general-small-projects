#Unit Converter (temp, currency, volume, mass and more)
#Converts various units between one another. 
#The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.

from unit_converter.converter import converts
from currency_converter import CurrencyConverter
import re

def convert():
    while True:
        invalue = input("Please enter your input value (with units): ")
        outunit = input("Please enter the units you'd like to convert your input value to: ")
        try:
            conversion = converts(invalue,outunit)
            break
        except:
            try:
                c = CurrencyConverter()
                value = re.search(r"\d+", invalue).group()
                units = re.search(r"[a-zA-Z]+", invalue).group().upper()
                conversion = c.convert(value, units, outunit.upper())
                break
            except:
                pass
        print(f"The function failed to comprehend your inputs of {invalue} and {outunit}. Please try again.")
    print(float(conversion),outunit)


convert()
