import csv
import Keys
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
rownum=0;
cityFile = "Cities_which_has_city.csv"

curCities=Keys.getCurrentCities()
CityFields =['cityCode','cityName','countryCode','timezone','cityLat','cityLong']
cityReader = csv.DictReader(open(cityFile,'rb'),delimiter=',')
count =0
curCities=Keys.getCurrentCities()
tab="\t"
tab2="\t\t"
boundary='"'
GenerateEnum=open("newCityEnums.txt",'w')
generatedCountry=open("newCountries.txt","w")
newCityListInPlainText=open("newCityInPlainText.txt",'w')
def nameFinalizer(curcity):
	finalCity=""
	for ch in curcity:
		# print ord(ch)
		if (ord(ch) >= 97 and ord(ch) <= 122):
			finalCity +=chr(ord(ch) - 32);
		elif ((ord(ch) >= 48 and ord(ch) <= 57) or (ord(ch) >= 65 and ord(ch) <= 90)):
			finalCity +=ch
		else:
			finalCity +="_"
	# print curcity+"-->"+finalCity
	return finalCity
citylist={}
countrySet=set()
def generateEnum():
	for city in cityReader:
		# print city
		if city['cityCode'] not in curCities:
			cityValues=city
			citylist[city['cityCode']]=cityValues
	print "\n\n\n\n\n\n"
	# print citylist
	for key,city in sorted(citylist.iteritems()):
		print key
		GenerateEnum.write( "\n" +tab+nameFinalizer(city['cityCode'])+"(")
		GenerateEnum.write( "\n" +tab2+boundary+city['cityName']+boundary+",")
		newCityListInPlainText.write(city['cityName']+"\n")
		print city['cityName']
		GenerateEnum.write( "\n" +tab2+"Country."+city['countryCode']+",")
		if(city['countryCode'] not in countrySet):
			generatedCountry.write("\nCountry."+city['countryCode']+",")
			countrySet.add(city['countryCode'])			
		GenerateEnum.write( "\n" +tab2+boundary+city['timezone']+boundary+",")
		GenerateEnum.write( "\n" +tab2+city['cityLat']+"d"+",")
		GenerateEnum.write( "\n" +tab2+city['cityLong']+"d"+",")
		GenerateEnum.write( "\n" +tab2+'""'+",")
		GenerateEnum.write( "\n" +tab2+'""'+",")
		GenerateEnum.write( "\n" +tab2+'""')
		GenerateEnum.write( "\n" +tab+"),")


generateEnum()
