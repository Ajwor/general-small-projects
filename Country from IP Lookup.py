#Country from IP Lookup 
#Enter an IP address and find the country that IP is registered in. Optional: Find the Ip automatically.


#uses ip2geotools to look up geolocation of an IP adress from a database, in this case DbIpCity
from ip2geotools.databases.noncommercial import DbIpCity

ipin = input('Please enter the IP address whoose country of registration you want to know: ')
country = DbIpCity.get(ipin, api_key='free').country
print('That IP address is registered in',country, '(Two letter country code)')

