import csv
import Keys
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
rownum=0;
cityFile = "Cities.csv"

curCities=Keys.getCurrentCities()
CityFields =['cityCode','cityName','countryCode','timezone','cityLat','cityLong']
cityReader = csv.DictReader(open(cityFile,'rb'),delimiter=',')
count =0
curCities=Keys.getCurrentCities()
tab="\t"
tab2="\t\t"
boundary='"'
GenerateEnum=open("newCityEnums.txt",'w')
def generateEnum():
	for city in cityReader:
		if city['cityCode'] not in curCities:
			GenerateEnum.write( "\n" +tab+city['cityCode']+"(")
			GenerateEnum.write( "\n" +tab2+boundary+city['cityName']+boundary+",")
			GenerateEnum.write( "\n" +tab2+"Country."+city['countryCode']+",")
			GenerateEnum.write( "\n" +tab2+boundary+city['timezone']+boundary+",")
			GenerateEnum.write( "\n" +tab2+city['cityLat']+"d"+",")
			GenerateEnum.write( "\n" +tab2+city['cityLong']+"d"+",")
			GenerateEnum.write( "\n" +tab2+'""'+",")
			GenerateEnum.write( "\n" +tab2+'""'+",")
			GenerateEnum.write( "\n" +tab2+'""'+",")
			GenerateEnum.write( "\n" +tab+city['cityCode']+"),")

generateEnum()
