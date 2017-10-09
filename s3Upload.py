from boto.s3.connection import S3Connection
conn=S3Connection()
bucket = conn.get_bucket('tourlandish')
# print myBucket.list()
def upload(filepath,filename):
	print filepath
	key="cities/"+filename+"/images/mobile/morning.jpg"
	print filename
	k=bucket.new_key(key)
	# print k
	k.set_contents_from_filename(filepath)
	# print k

