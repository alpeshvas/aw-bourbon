import csv
from geopy.geocoders import GoogleV3
import Keys
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
locator = GoogleV3(api_key=Keys.getkey(0))
rownum=0;
inputfile = "AW Products - Sheet1.csv"
ouptputfile = "Examplev1 - H Sheet.csv"
finalOutput = "Output.csv"
cityFile = "Cities.csv"
awReader=csv.DictReader(open(inputfile,'rb'),delimiter=',', quotechar='"')
lat="latitude"
lng="longitude"
inputFields= ['tour_group','attraction_world_id','is_group_ticket','description','image_url','city','neighbourhood','postal_code','region','country','multiple_region'
,'address','latitude','longitude','adult_price','child_price','group_price']
outputFields=Keys.getOutputFields()

finalOutputFields=[]
CityFields =['cityCode','cityName','countryCode','timezone','cityLat','cityLong']

cityWriter = csv.DictWriter(open(cityFile,'w'),fieldnames=CityFields,delimiter=',')
cityWriter.writeheader()
awWriter=csv.DictWriter(open(finalOutput,'w'),fieldnames=outputFields,delimiter=',', quotechar='"')
count =0
awWriter.writeheader()
mapdict={'Product Group Name':'tour_group','Product name':'tour_group','Summary':'description','Adult Price':'adult_price','Child Price':'child_price'
,'City':'city','Start point address city':'city','End point address city':'city'}

defaultVals={'Product type':"Tour",'e':'Default Category','Languages':'English','Schedule Type':'Fixed',
	'Duration Type':'Fixed','Hours(duration)':'1','Minutes(duration)':'1','Default availability':'UNLIMITED',
	'Hotel pickup provided':'No',
	'Profile Name':'General',
	'Start Date (YY-MM-DD)':'2017-01-01',
	'End Date  (YY-MM-DD)':'2017-01-01' }


keycount=0
curcount=0

# formatWriter =
def getDefaultInside(key):
	if key in defaultVals:
		return defaultVals[key]
	return ""

def updateLocator(i):
	locator=GoogleV3(api_key=Keys.getkey(0)) 
def getDefaultdata(row):
	data={}
	for key in outputFields:
		if key in mapdict:
			data[key]=row[mapdict[key]]
		else:
			data[key]=getDefaultInside(key)
	return data

def processWithlatlong(row,haslatlong=True):
	try:
		# print row[lat]
		# print row[lng]
		location= None	
		for x in xrange(1,10):
			try:
				if haslatlong:
					location=locator.reverse("%s,%s" %(row[lat],row[lng]))
				else:
					location=locator.geocode(row['tour_group'])
					location=locator.reverse("%s,%s" %(location.latitude,location.longitude))
				break
			except:
				keycount +=1
				updateLocator(keycount)
		data=getDefaultdata(row)
		# print location[0].raw
		data['Start point address line 1'] = location[0].address
		data['End point address line 1'] = location[0].address
		try:
			data['Neighbourhood'] = location[1].address
		except:
			pass
		for val in location[0].raw['address_components']:
			# print val
			for typ in val['types']:
				if typ == 'locality' and row['city'] == "":
					data['Start point address city'] = val['long_name']
					data['End point address city'] = val['long_name']
					break
				if typ == 'postal_code':
					data['Start point address postal code'] = val['long_name']
					data['End point address postal code'] = val['long_name']
					break
				if typ == 'neighborhood':
					data['Neighbourhood'] = val['long_name']
					break
				if typ == 'country':
					data['Start point address country'] = val['long_name']
					data['End point address country'] = val['long_name']
					break
				if typ == 'administrative_area_level_1':
					data['Start point address state'] = val['long_name']
					data['End point address state'] = val['long_name']
				if (typ == 'administrative_area_level_2' or typ == 'administrative_area_level_3' or typ == 'administrative_area_level_4') and ('Neighborhood' not in data):
					data['Neighbourhood'] = val['long_name']
	# print data
		awWriter.writerow(data)
		print data
		sleep(1)
	except:
		pass
limit =50
def processCity(curcity):
	location = None
	for x in xrange(1,10):
		try:
			location=locator.geocode(curcity)
			timezone=locator.timezone("%s,%s" %(location.latitude,location.longitude))
			location=locator.reverse("%s,%s" %(location.latitude,location.longitude))
			break
		except:
			pass
	# print location
	cityListCsv = {}
	cityListCsv['cityCode'] = curcity.upper().replace(" ","_")
	cityListCsv['cityName'] = curcity
	cityListCsv['cityLat'] = location[0].latitude
	cityListCsv['cityLong'] = location[0].longitude
	cityListCsv['timezone'] = timezone
	for val in location[0].raw['address_components']:
		for typ in val['types']:
			if typ == 'country':
				cityListCsv['countryCode'] = val['short_name']
				break

	cityWriter.writerow(cityListCsv)
	print cityWriter
cityList=set()
def update_old_sheet():
	i=0
	for row in awReader:
		print i
		if (row['latitude'] =="" or row['longitude'] == "" ):
			print row['tour_group']
		else:
			processWithlatlong(row)
			i +=1
		if i==10:
			break
update_old_sheet()
