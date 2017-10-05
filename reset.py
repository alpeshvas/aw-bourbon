import csv
import data
import mysql.connector
citfile="newCityInPlainText.txt"
cities=open(citfile,"r")
cnx = mysql.connector.connect(user=data.getUser(), password=data.getPass() ,database='tourlandish')
cursor = cnx.cursor()

delete_tour_group = ("DELETE FROM tour_group Where city = %s")
delete_tour = ("DELETE FROM tour Where startpoint_address_city = %s")
delete_calipso_tour = ("DELETE FROM calipso_tour Where startpoint_address_city = %s")

# Insert new employee
categories=["Bestsellers","New Arrivals","Trending"]
for city in cities:
	city=city.rstrip()
	for category in categories:
		print city
		data=(city+": "+category,category,city.lower(),"1")
		print (delete_tour_group, (city.lower(),))
		cursor.execute(delete_tour_group, (city.lower(),))
		cursor.execute(delete_tour_group, (city.lower(),))
		cursor.execute(delete_calipso_tour, (city.lower(),))
		
		
cnx.commit()
cursor.close()
cnx.close()
