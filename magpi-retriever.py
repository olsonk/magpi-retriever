import urllib

start_issue = 01				# edit this number for whatever issue you want to start with
current_issue = 46				# edit this number to the last issue you want to download

for i in range(current_issue-start_issue+1):	# calculates the number of issues it should download
	current = issue + i
	url = "https://www.raspberrypi.org/magpi-issues/MagPi%02d.pdf" % current
	filename = "MagPi%02d.pdf" % current
	
	urllib.urlretrieve(url, filename)	# files are downloaded to the same directory as this script
