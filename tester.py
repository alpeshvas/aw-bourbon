import csv
from geopy.geocoders import GoogleV3
import Keys
locator = GoogleV3(api_key=Keys.getkey())
location=locator.geocode("Mexico")
timezone = locator.timezone("43.695279,7.264738")
location=locator.reverse("%s,%s" %(location.latitude,location.longitude))
print location