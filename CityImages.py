import csv
import urllib2
import requests
import time
cityFile="../newCityInPlainText.txt"
baseUrl="http://www.attractionworld.com/images/static/banners/%s-region-banner.jpg"
cities = open(cityFile,'rb')
noImageExist = open("noImageExist.txt",'wb')
outDirc="/home/vas/myHeadO/AW-extraction/City-Image-Extraction/cityImages"
notExist=open("cityDoesnotexist.txt",'wb')
def cityWhichExist():
	for row in cities:
		row=row.rstrip()
		print "current city is "+row
		imageUrl=baseUrl %(row.lower().replace(' ',''),)
		print imageUrl
		request=requests.get(imageUrl)
		if request.status_code == 200:
			# imageFile=urllib2.urlopen(imageUrl)
			pass
			# with open(outDirc+"/"+row+".jpg",'wb') as outImage:
			# 	outImage.write(imageFile.read())
		else:
			imageUrl = baseUrl %(row.lower().replace(' ','-'))
			request=requests.get(imageUrl)
			if request.status_code == 200:
				# imageFile=urllib2.urlopen(imageUrl)
				# with open(outDirc+"/"+row+".jpg",'wb') as outImage:
					# outImage.write(imageFile.read())
				pass
			else:
				noImageExist.write(row+"\n")
				notExist.write("Url for city "+ row + " does not exist\n")
				notExist.write("url is "+imageUrl+"\n")		
def cityDoesNotExist():
	
	time.sleep(1)